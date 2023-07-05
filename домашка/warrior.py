import random
class Воин:
    def __init__(self, name, hp, damage):
        self.name = name  # str
        self.hp = hp  # int
        self.damage = damage  # int

    def hit(self, Юнит):
        Юнит.hp -= self.damage
        if Юнит.hp > 0:
            print(f'"{self.name}" атаковал "{Юнит.name}". У "{Юнит.name}" осталось {Юнит.hp} здоровья')
        else:
            print(f'"{self.name}" атаковал "{Юнит.name}". "{Юнит.name}" убит')
            Юнит.hp = 0
        return Юнит.hp


from random import randint as rnd

Юнит1 = Воин('Воин севера', 100, 20)
Юнит2 = Воин('Воин юга', 100, 20)
Юниты = [Юнит1, Юнит2]

while True:
    attack_index = rnd(0, 1)  # Кто атакует
    target_index = (attack_index + 1) % 2  # Кого атакует
    target_hp = Юниты[attack_index].hit(Юниты[target_index])
    if target_hp == 0:
        print(f'"{Юниты[attack_index].name}" Победил!')
        break