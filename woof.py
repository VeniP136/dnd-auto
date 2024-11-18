import random

class Stats():
    
    def __init__(self, hp, atak, atak_rate, kd):
        self.hp = hp
        self.atak = atak
        self.atak_rate = atak_rate
        self.kd = kd

    @staticmethod
    def count_atack(atack_formula):
        atack_formula = atack_formula.replace("+", "d")
        atack_formula = atack_formula.split("d")
        if len(atack_formula) == 1:
            atack_score = int(atack_formula[0])
        else:
            atack_score = int(atack_formula[0]) * random.randint(1, int(atack_formula[1])) + int(atack_formula[2])
         
        return atack_score

# вынести в модуль
class Battle:

    @staticmethod
    def fight(P1, P2):
        # Обработка атак первого игрока
        for attack_rate, attack in zip(P1.atak_rate, P1.atak):
            if Stats.count_atack(attack_rate) > P2.kd:
                damage = Stats.count_atack(attack)
                P2.hp -= damage
                if P2.hp <= 0:
                    return "win p1"

        # Обработка атак второго игрока
        for attack_rate, attack in zip(P2.atak_rate, P2.atak):
            if Stats.count_atack(attack_rate) > P1.kd:
                damage = Stats.count_atack(attack)
                P1.hp -= damage
                if P1.hp <= 0:
                    return "win p2"
        
        # Если оба игрока ещё живы, продолжаем бой
        return Battle.fight(P1, P2)

    @staticmethod
    def series_fight():
        for p1 in [Bear1, Bear2]:
            result = Battle.fight(p1, Clerk)
            if result == "win p1":
                return "win p1"
        return "win p2"



# 🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
# 🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
# 🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
# 🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
# 🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🦍🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
# 🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
# 🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
# 🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
# 🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌

trying = 10000
winrate = 0
for i in range(trying):

    Bear1 = Stats(34, ["1d8+4", "2d6+4"], ["1d20+6", "1d20+6"], 11)
    Bear2 = Stats(34, ["1d8+4", "2d6+4"], ["1d20+6", "1d20+6"], 11)
    Clerk = Stats(36, ["1d8+4", "2d6+5"], ["1d20+6", "1d20+7"], 18)
    if Battle.series_fight() == "win p2":
        winrate += 1
print(f"Вероятность победы жреца {winrate / trying * 100}%")
input()