class User:
    def __init__(self, health):
        self.health = health

    def attack(self, target):
        pass

    def take_damage(self, damage):
        self.health -= damage
#
# class mag(User):
#     def __init__(self, health, legs, name):
#         super().__init__(has_tail=has_tail, legs=legs, name=name, ears=True)




class Mage(User):
    def __init__(self, health, mana):
        super().__init__(health)
        self.mana = mana
    def cast_spell(self, spell_name, target):
        if self.mana >= spell_name.mana_cost:
            spell_name.cast(target)
            self.mana -= spell_name.mana_cost
        else:
            print("Not enough mana to cast spell")
class Warrior(User):
    def __init__(self, health, strength):
        super().__init__(health)
        self.strength = strength

    def attack(self, target):
        damage = self.strength
        target.take_damage(damage)


class Archer(User):
    def __init__(self, health, agility):
        super().__init__(health)
        self.agility = agility

    def attack(self, target):
        damage = self.agility
        target.take_damage(damage)