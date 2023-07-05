class user:
    def __init__(self, health, ataks, damage):
        self.health = health
        self.ataks = ataks
        self.damage = damage

    def __str__(self):
        return self.health

    def shoot(self, user):
        pass

    def health_down(self, damage):
        print(f'Усть пробитие', по нам попали на {damage} урона)
        self.armor -= damage





class T34(Tank):
    pass


class Mouse(Tank):
    pass

t34.shoot(mouse)
mouse.shoot

