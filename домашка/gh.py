import random
class Warrior:
    def __init__(self):
        self.hp_warrior = 0

warrior_1 = Warrior()
warrior_2 = Warrior()
warrior_1.hp_warrior = 100
warrior_2.hp_warrior = 100

while True:
    who_beats = random.randint(0, 10)


    if warrior_1.hp_warrior == 0:
        print('Победил рома')
        break
    elif warrior_2.hp_warrior == 0:
        print('Победил саша')
        break
    elif who_beats < 6:
        warrior_2.hp_warrior -= 20
        print('саша ударяет рому')
        print(f'У ромы осталось {warrior_2.hp_warrior} здоровья\n')
    elif who_beats > 5:
        warrior_1.hp_warrior -= 20
        print('рома ударяет сашу')
        print(f'У саши осталось {warrior_1.hp_warrior} здоровья\n')