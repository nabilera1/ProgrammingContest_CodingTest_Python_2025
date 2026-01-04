
import threading
import time
import random
from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class Holding:
    shares: int = 0
    avg_cost: float = 0.0

    def buy(self, qty: int, price: float):
        if qty <= 0:
            return
        total_cost = self.avg_cost * self.shares + price * qty
        self.shares += qty
        self.avg_cost = total_cost / self.shares

    def sell(self, qty: int, price: float) -> float:
        if qty <= 0 or qty > self.shares:
            return 0.0
        proceeds = price * qty
        self.shares -= qty
        if self.shares == 0:
            self.avg_cost = 0.0
        return proceeds

@dataclass
class Stock:
    id: int
    name: str
    sector: str
    region: str
    price: float
    base_volatility: float = 0.02
    daily_drift: float = 0.0
    change_pct: float = 0.0
    trend_memory: List[float] = field(default_factory=list)

    def apply_change(self, pct: float):
        old = self.price
        self.price = max(0.01, self.price * (1.0 + pct))
        self.change_pct = (self.price / old) - 1.0
        self.trend_memory.append(self.change_pct)
        if len(self.trend_memory) > 10:
            self.trend_memory.pop(0)

@dataclass
class NewsEffect:
    text: str
    expires_at: float
    sector_mult: Dict[str, float] = field(default_factory=dict)
    region_mult: Dict[str, float] = field(default_factory=dict)
    stock_mult: Dict[str, float] = field(default_factory=dict)
    spillover: float = 0.0

    def is_active(self) -> bool:
        return time.time() < self.expires_at

class GameState:
    def __init__(self):
        self.cash: float = 1000.0
        self.lock = threading.RLock()
        self.running = True

        self.stocks: List[Stock] = self._init_stocks()
        self.holdings: Dict[int, Holding] = {s.id: Holding() for s in self.stocks}
        self.active_news: List[NewsEffect] = []
        self.last_news_time: float = 0.0

        self.price_tick_sec = 1.0
        self.news_interval_sec = 15.0
        self.news_duration_sec = 35.0

        # 승패 기준
        self.win_target: float = 10000.0
        self.lose_threshold: float = 0.0

    def _init_stocks(self) -> List[Stock]:
        names = [
            (0, 'NEO ENT', 'ENT', 'KOR', 50.0),
            (1, 'K-STAR MEDIA', 'ENT', 'KOR', 30.0),
            (2, 'GLOBAL BEATS', 'ENT', 'GLB', 40.0),
            (3, 'QBYTE TECH', 'IT', 'KOR', 120.0),
            (4, 'ORBITAL SOFT', 'IT', 'GLB', 200.0),
            (5, 'HANSEM CHIP', 'IT', 'KOR', 85.0),
        ]
        stocks = []
        for sid, name, sector, region, price in names:
            drift = random.uniform(-0.0005, 0.0005)
            vol = random.uniform(0.012, 0.028)
            stocks.append(Stock(sid, name, sector, region, price, vol, drift))
        return stocks

    # 총자산 계산
    def total_assets(self) -> float:
        with self.lock:
            total_value = self.cash
            for s in self.stocks:
                h = self.holdings[s.id]
                if h.shares > 0:
                    total_value += s.price * h.shares
            return total_value

    # 승패 판정
    def check_end_condition(self) -> Optional[str]:
        ta = self.total_assets()
        if ta >= self.win_target:
            self.running = False
            return f"승리: 총자산 {ta:.2f}원 달성 (목표 {self.win_target:.0f}원)"
        if ta <= self.lose_threshold:
            self.running = False
            return f"패배: 총자산 {ta:.2f}원 (기준 {self.lose_threshold:.0f}원 이하)"
        return None

    def _compose_news(self) -> NewsEffect:
        now = time.time()
        kind = random.choice(['idol', 'scandal', 'chip_breakthrough', 'regulation', 'export_boom', 'ceo_resign'])
        duration = self.news_duration_sec

        if kind == 'idol':
            ent_stocks = [s for s in self.stocks if s.sector == 'ENT']
            target = random.choice(ent_stocks)
            text = f"속보: {target.name} 아이돌 급성장! 차트 싹쓸이 기대"
            return NewsEffect(
                text=text,
                expires_at=now + duration,
                stock_mult={target.name: +0.40},
                sector_mult={'ENT': -0.07},
                spillover=0.002,
            )
        elif kind == 'scandal':
            target = random.choice(self.stocks)
            text = f"단독: {target.name} 내부 비리 의혹 제기"
            return NewsEffect(
                text=text,
                expires_at=now + duration,
                stock_mult={target.name: -0.23},
                spillover=0.001,
            )
        elif kind == 'chip_breakthrough':
            text = "헤드라인: 차세대 반도체 공정 돌파구… IT 전반 수혜 기대"
            return NewsEffect(
                text=text,
                expires_at=now + duration,
                sector_mult={'IT': +0.17},
            )
        elif kind == 'regulation':
            text = "속보: 국내 엔터 규제 강화 발표… 수익성 우려"
            return NewsEffect(
                text=text,
                expires_at=now + duration,
                sector_mult={'ENT': -0.09},
                region_mult={'KOR': -0.02},
            )
        elif kind == 'export_boom':
            text = "뉴스: 수출 호조에 글로벌 증시 훈풍"
            return NewsEffect(
                text=text,
                expires_at=now + duration,
                region_mult={'GLB': +0.13},
            )
        elif kind == 'ceo_resign':
            target = random.choice(self.stocks)
            text = f"속보: {target.name} CEO 전격 사임"
            return NewsEffect(
                text=text,
                expires_at=now + duration,
                stock_mult={target.name: -0.20},
            )
        return NewsEffect(text="시장 혼조세", expires_at=now + duration, spillover=0.0)

    def _aggregate_news_boost(self, stock: Stock) -> float:
        boost = 0.0
        self.active_news = [n for n in self.active_news if n.is_active()]
        for n in self.active_news:
            if stock.name in n.stock_mult:
                boost += n.stock_mult[stock.name]
            if stock.sector in n.sector_mult:
                boost += n.sector_mult[stock.sector]
            if stock.region in n.region_mult:
                boost += n.region_mult[stock.region]
            boost += n.spillover
        return boost / max(1, int(self.news_duration_sec))

    def price_tick(self):
        with self.lock:
            for s in self.stocks:
                news_boost = self._aggregate_news_boost(s)
                noise = random.gauss(0, s.base_volatility * 0.6)
                pct = s.daily_drift + noise + news_boost
                s.apply_change(pct)

    def maybe_emit_news(self):
        now = time.time()
        if now - self.last_news_time >= self.news_interval_sec:
            news = self._compose_news()
            self.active_news.append(news)
            self.last_news_time = now
            print(f"\n[뉴스] {news.text} (효력 {int(self.news_duration_sec)}초)")

    def buy_stock(self, stock_id: int, qty: int) -> Optional[str]:
        with self.lock:
            stock = self._get_stock(stock_id)
            if stock is None:
                return "해당 번호의 주식이 없습니다."
            cost = stock.price * qty
            if qty <= 0:
                return "매수 수량은 1주 이상이어야 합니다."
            if cost > self.cash:
                return f"현금이 부족합니다. 필요: {cost:.2f}, 보유: {self.cash:.2f}"
            self.cash -= cost
            self.holdings[stock.id].buy(qty, stock.price)
        end_msg = self.check_end_condition()
        return end_msg or f"매수 완료: {stock.name} {qty}주 @{stock.price:.2f}"

    def sell_stock(self, stock_id: int, qty: int) -> Optional[str]:
        with self.lock:
            stock = self._get_stock(stock_id)
            if stock is None:
                return "해당 번호의 주식이 없습니다."
            h = self.holdings[stock.id]
            if qty <= 0:
                return "매도 수량은 1주 이상이어야 합니다."
            if qty > h.shares:
                return f"보유 수량 부족. 보유: {h.shares}주"
            proceeds = h.sell(qty, stock.price)
            self.cash += proceeds
        end_msg = self.check_end_condition()
        return end_msg or f"매도 완료: {stock.name} {qty}주 @ {stock.price:.2f} → {proceeds:.2f} 입금"

    def _get_stock(self, stock_id: int) -> Optional[Stock]:
        for s in self.stocks:
            if s.id == stock_id:
                return s
        return None

    def summary_stocks(self) -> str:
        lines = ["\n[시장] 매수 가능한 주식 목록:"]
        lines.append("ID  이름                부문  지역   가격      변동   추세")
        lines.append("--  ------------------  ----  ----  -------   -----   ---")
        for s in self.stocks:
            arrow = '↑' if s.change_pct > 0 else ('↓' if s.change_pct < 0 else '-')
            pct = f"{s.change_pct*100:+.2f}%"
            lines.append(f"{s.id:<3} {s.name:<18} {s.sector:<4}  {s.region:<4}  {s.price:>7.2f}  {pct:>7}   {arrow}")
        lines.append("\n매수 방법: buy <ID> <수량> (예: buy 3 10)")
        lines.append("매도 방법: sell <ID> <수량> (예: sell 1 5)")
        return "\n".join(lines)

    def portfolio_info(self) -> str:
        with self.lock:
            total_value = 0.0
            lines = ["\n[자산] 보유 현황:"]
            lines.append(f"현금: {self.cash:.2f}")
            lines.append("ID  이름                보유주  평단가    현재가    평가손익   수익률")
            lines.append("--  ------------------  -----  -------  -------  --------  ------")
            for s in self.stocks:
                h = self.holdings[s.id]
                if h.shares > 0:
                    eval_value = s.price * h.shares
                    pnl = (s.price - h.avg_cost) * h.shares
                    rr = 0.0 if h.avg_cost <= 0 else (s.price / h.avg_cost - 1.0) * 100
                    total_value += eval_value
                    lines.append(
                        f"{s.id:<3} {s.name:<18} {h.shares:>5}  {h.avg_cost:>7.2f}  {s.price:>7.2f}  {pnl:>8.2f}  {rr:>6.2f}%"
                    )
            lines.append(f"총 평가액(현금 제외): {total_value:.2f}")
            lines.append(f"총자산(현금 포함): {total_value + self.cash:.2f}")
            return "\n".join(lines)

def market_loop(state: GameState):
    while state.running:
        time.sleep(state.price_tick_sec)
        state.price_tick()
        state.maybe_emit_news()
        end_msg = state.check_end_condition()
        if end_msg:
            print("\n" + end_msg)
            break

def print_help():
    print("""
명령어 안내:
  s                : 주식 목록/가격 보기
  i                : 내 자산/수익률 보기
  buy <ID> <수량>  : 주식 매수
  sell <ID> <수량> : 주식 매도
  help             : 명령어 도움말
  q                : 종료
""")

def main():
    random.seed()
    state = GameState()
    t = threading.Thread(target=market_loop, args=(state,), daemon=True)
    t.start()

    print("--주식 시뮬레이션 게임--")
    print(f"승리 조건: 총자산 {state.win_target:.0f}원 이상 달성 시 즉시 승리 종료")
    print(f"패배 조건: 총자산 {state.lose_threshold:.0f}원 이하가 될 경우 즉시 패배 종료")
    print_help()

    while state.running:
        try:
            raw = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n종료합니다.")
            break

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()

        if cmd == 'q':
            state.running = False
            break
        elif cmd == 'help' or cmd == 'h':
            print_help()
        elif cmd == 's':
            print(state.summary_stocks())
        elif cmd == 'i':
            print(state.portfolio_info())
        elif cmd == 'buy':
            if len(parts) != 3:
                print("사용법: buy <ID> <수량>")
                continue
            try:
                sid = int(parts[1])
                qty = int(parts[2])
            except ValueError:
                print("ID와 수량은 정수여야 합니다.")
                continue
            msg = state.buy_stock(sid, qty)
            if msg:
                print(msg)
        elif cmd == 'sell':
            if len(parts) != 3:ㅗ
                print("사용법: sell <ID> <수량>")
                continue
            try:
                sid = int(parts[1])
                qty = int(parts[2])
            except ValueError:
                print("ID와 수량은 정수여야 합니다.")
                continue
            msg = state.sell_stock(sid, qty)
            if msg:
                print(msg)
        else:
            print("알 수 없는 명령입니다.")

    state.running = False
    print("게임을 종료합니다.")

if __name__ == '__main__':
    main()
