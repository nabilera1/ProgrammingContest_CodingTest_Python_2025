import random
from typing import List, Optional

# ------------------------------
# 도메인 모델
# ------------------------------
class Inventory:
    """구성(Composition): 캐릭터가 인벤토리를 '가지고' 있다."""
    def __init__(self):
        self.items: List["Item"] = []

    def add(self, item: "Item"):
        self.items.append(item)

    def use_first(self, owner: "Character", kind: type) -> bool:
        """처음으로 발견한 해당 타입 아이템을 사용"""
        for i, it in enumerate(self.items):
            if isinstance(it, kind):
                it.use(owner)
                del self.items[i]
                return True
        return False

    def __str__(self):
        # 보기 좋게 묶어서 출력
        names = {}
        for it in self.items:
            names[type(it).__name__] = names.get(type(it).__name__, 0) + 1
        return ", ".join(f"{k} x{v}" for k, v in names.items()) or "(비어 있음)"


class Item:
    """아이템 기본형(인터페이스 역할)"""
    def use(self, owner: "Character"):
        raise NotImplementedError


class Potion(Item):
    def __init__(self, heal=20):
        self.heal = heal

    def use(self, owner: "Character"):
        owner.hp = min(owner.max_hp, owner.hp + self.heal)
        print(f"💊 포션 사용! HP가 {self.heal} 회복되어 {owner.hp}/{owner.max_hp}")


class Character:
    """부모 클래스: 공통 속성과 동작"""
    def __init__(self, name: str, hp: int, atk: int):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.base_atk = atk
        self.inv = Inventory()

    @property
    def alive(self) -> bool:
        return self.hp > 0

    def attack(self, other: "Character") -> int:
        """자식이 오버라이딩할 메서드(다형성 포인트)"""
        dmg = self.base_atk
        other.hp = max(0, other.hp - dmg)
        return dmg

    def status(self):
        print(f"{self.name}  HP {self.hp}/{self.max_hp}  인벤토리[{self.inv}]")

    def __str__(self):
        return f"{self.name}(HP:{self.hp}/{self.max_hp}, ATK:{self.base_atk})"


class Warrior(Character):
    """전사: 일정 확률로 치명타"""
    def attack(self, other: "Character") -> int:
        crit = random.random() < 0.25
        dmg = self.base_atk * (2 if crit else 1)
        other.hp = max(0, other.hp - dmg)
        print("⚔️  치명타!" if crit else "⚔️  공격!")
        return dmg


class Mage(Character):
    """마법사: 마나 개념 없이 랜덤 강화 마법"""
    def attack(self, other: "Character") -> int:
        boost = random.randint(0, self.base_atk)  # 0~ATK 추가
        dmg = self.base_atk + boost
        other.hp = max(0, other.hp - dmg)
        print(f"✨ 강화 마법(+{boost}) 발동!")
        return dmg


# ------------------------------
# 적 몬스터
# ------------------------------
class Slime(Character):
    """슬라임: 약하지만 회복 점액(저확률)"""
    def attack(self, other: "Character") -> int:
        regen = random.random() < 0.2
        if regen:
            heal = 5
            self.hp = min(self.max_hp, self.hp + heal)
            print("🟢 슬라임이 점액으로 체력을 회복(+5)!")
        dmg = self.base_atk
        other.hp = max(0, other.hp - dmg)
        return dmg


class Goblin(Character):
    """고블린: 간혹 훔치기(포션을 빼앗음)"""
    def attack(self, other: "Character") -> int:
        steal = random.random() < 0.15
        if steal and other.inv.use_first(other, Potion):  # 포션이 있으면 '사용시켜' 버림
            print("🧪 고블린이 포션을 빼앗아 강제로 사용하게 했다!")
        dmg = self.base_atk + random.randint(0, 2)
        other.hp = max(0, other.hp - dmg)
        return dmg


# ------------------------------
# 게임 루프
# ------------------------------
class Game:
    def __init__(self, player: Character):
        self.player = player
        # 시작 아이템
        self.player.inv.add(Potion(heal=25))
        self.round = 1

    def spawn_enemy(self) -> Character:
        if random.random() < 0.5:
            return Slime("슬라임", 30, 5)
        return Goblin("고블린", 35, 6)

    def turn(self, enemy: Character):
        print("\n[메뉴] 1)공격  2)포션사용  3)상태  4)도망")
        choice = input("선택: ").strip()
        if choice == "1":
            dmg = self.player.attack(enemy)
            print(f"→ {self.player.name}가 {enemy.name}에게 {dmg} 피해")
        elif choice == "2":
            used = self.player.inv.use_first(self.player, Potion)
            if not used:
                print("사용할 포션이 없습니다.")
        elif choice == "3":
            self.player.status()
        elif choice == "4":
            if random.random() < 0.6:
                print("🏃 도망 성공! 다음 전투로 넘어갑니다.")
                enemy.hp = 0  # 강제 종료
            else:
                print("도망 실패!")
        else:
            print("잘못된 입력입니다.")

    def enemy_phase(self, enemy: Character):
        if enemy.alive:
            dmg = enemy.attack(self.player)
            print(f"← {enemy.name}의 반격! {dmg} 피해")

    def reward(self):
        # 보상: 낮은 확률로 포션
        if random.random() < 0.4:
            self.player.inv.add(Potion(heal=20))
            print("🎁 전리품: 포션(+20) 획득!")

    def play(self):
        print("=== 미니 던전: 다형성 체험판 ===")
        while self.player.alive:
            enemy = self.spawn_enemy()
            print(f"\n--- 라운드 {self.round} ---")
            print(f"적 등장: {enemy}")
            while enemy.alive and self.player.alive:
                self.turn(enemy)
                self.enemy_phase(enemy)
                print(f"상태 | 플레이어HP {self.player.hp}/{self.player.max_hp}  적HP {enemy.hp}/{enemy.max_hp}")
            if not self.player.alive:
                print("\n💀 패배... 다음에 다시 도전하세요.")
                break
            print(f"\n✅ {enemy.name} 격퇴!")
            self.reward()
            self.round += 1
        print("\n게임 종료. 플레이해주셔서 감사합니다!")


# ------------------------------
# 실행 스크립트
# ------------------------------
def choose_job() -> Character:
    print("직업 선택: 1)전사  2)마법사")
    while True:
        p = input("번호 입력: ").strip()
        if p == "1":
            return Warrior("전사", hp=60, atk=10)
        if p == "2":
            return Mage("마법사", hp=50, atk=8)
        print("다시 입력하세요.")

if __name__ == "__main__":
    random.seed()  # 매 실행마다 다른 난수
    player = choose_job()
    Game(player).play()
