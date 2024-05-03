import random

class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(0, self.attack_power)
        other.health -= damage
        print(f"{self.name} наносит {damage} урона {other.name}. Оставшееся здоровье {other.name}: {other.health}")

    def is_alive(self):
        return self.health > 0

def game_round(player, computer):
    player.attack(computer)
    if computer.is_alive():
        computer.attack(player)
    else:
        print(f"{computer.name} побежден!")
        return False

    if not player.is_alive():
        print(f"{player.name} побежден!")
        return False

    return True

def start_game():
    player_name = input("Введите имя вашего героя: ")
    player = Hero(player_name, 100, 20)
    computer = Hero("Компьютерный герой", 100, 15)

    turn = 0
    while player.is_alive() and computer.is_alive():
        turn += 1
        print(f"\nРаунд {turn}")
        if not game_round(player, computer):
            break

    if player.is_alive():
        print(f"\nПоздравляем! {player.name} выиграл!")
    else:
        print(f"\nИгра окончена. {computer.name} победил.")

start_game()