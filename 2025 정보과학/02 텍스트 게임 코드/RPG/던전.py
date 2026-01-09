import random
import time


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.gold = 0
        self.potions = 1

    def attack(self):
        return random.randint(10, 20)

    def heal(self):
        if self.potions > 0:
            heal_amount = 30
            self.hp = min(self.hp + heal_amount, self.max_hp)
            self.potions -= 1
            print(f"🧪 포션을 사용했습니다! (체력 +{heal_amount}, 남은 포션: {self.potions})")
        else:
            print("❌ 포션이 없습니다!")

    def show_status(self):
        print(f"\n📊 [{self.name}] HP: {self.hp}/{self.max_hp} | Gold: {self.gold} | 🧪: {self.potions}")


def battle(player):
    monster_hp = random.randint(30, 60)
    print(f"\n⚔️ 야생의 슬라임(HP: {monster_hp})이 나타났다!")
    time.sleep(1)

    while monster_hp > 0 and player.hp > 0:
        player.show_status()
        print(f"👻 슬라임 HP: {monster_hp}")
        action = input("행동을 선택하세요 (1:공격, 2:포션, 3:도망) > ")

        if action == "1":
            damage = player.attack()
            monster_hp -= damage
            print(f"🗡️ 당신의 공격! 슬라임에게 {damage}의 데미지!")
        elif action == "2":
            player.heal()
            # 힐을 해도 몬스터는 공격함
        elif action == "3":
            if random.random() > 0.5:
                print("💨 무사히 도망쳤습니다!")
                return
            else:
                print("😓 도망치지 못했습니다!")
        else:
            print("잘못된 입력입니다.")
            continue

        time.sleep(0.5)

        # 몬스터 반격
        if monster_hp > 0:
            monster_dmg = random.randint(5, 15)
            player.hp -= monster_dmg
            print(f"💥 슬라임의 공격! 당신은 {monster_dmg}의 피해를 입었습니다.")

    if player.hp > 0:
        gold_drop = random.randint(10, 50)
        player.gold += gold_drop
        print(f"\n🎉 슬라임을 물리쳤습니다! {gold_drop} 골드를 얻었습니다.")


def game_loop():
    print("🏰 어둠의 던전에 오신 것을 환영합니다.")
    name = input("모험가의 이름을 입력하세요: ")
    player = Player(name)

    turn = 1
    while player.hp > 0:
        print(f"\n--- [Turn {turn}] ---")
        print("무엇을 하시겠습니까?")
        choice = input("1: 탐험하기  2: 상태확인  3: 휴식(체력회복)  4: 종료 > ")

        if choice == "1":
            print("🚶 어두운 통로를 걷습니다...")
            time.sleep(1.5)
            event = random.randint(1, 10)

            if event <= 5:  # 50% 확률로 전투
                battle(player)
            elif event <= 8:  # 30% 확률로 아이템 발견
                print("📦 낡은 상자를 발견했습니다!")
                if random.choice([True, False]):
                    player.potions += 1
                    print("🧪 포션을 1개 획득했습니다!")
                else:
                    gold = random.randint(5, 20)
                    player.gold += gold
                    print(f"💰 {gold} 골드를 발견했습니다!")
            else:  # 20% 확률로 함정
                dmg = random.randint(5, 10)
                player.hp -= dmg
                print(f"📌 앗! 함정을 밟았습니다. {dmg}의 피해를 입었습니다.")

        elif choice == "2":
            player.show_status()

        elif choice == "3":
            print("⛺ 잠시 휴식을 취합니다... (HP +10)")
            player.hp = min(player.hp + 10, player.max_hp)
            time.sleep(1)

        elif choice == "4":
            print("🚪 게임을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다.")

        turn += 1

    if player.hp <= 0:
        print("\n💀 당신은 던전에서 쓰러졌습니다... GAME OVER")


if __name__ == "__main__":
    game_loop()