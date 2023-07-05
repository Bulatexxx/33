class Pet:

    def __init__(self, has_tail, legs, name, ears):
        self.has_tail = True
        self.legs = 4
        self.name = None
        self.ears = True

    def __str__(self):
        return f"y {self.name} {self.legs} ноги и {'есть хвост' if self.has_tail else 'хвоста нет'}." \
        f"у него {'есть ушки' if self.ears else 'нет ушек'}."

    def sound(self):
        pass

# class Dog(Pet):
#     def __init__(self, legs, name, ears):
#         super().__init__(name=name, legs=legs, ears=ears, has_tail=True)
#
#
# dog = Dog(4, 'Bulat', True)
# print(dog)

# pet1 =  Pet(has_tail=True, legs=4, name="Bulat", ears=True)


class Cat(Pet):
    def __init__(self, has_tail, legs, name):
        super().__init__(has_tail=has_tail, legs=legs, name=name, ears=True)


cat = Cat(True, 4, 'Solomon')
print(cat)