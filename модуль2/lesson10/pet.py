class Pet:
    has_tail = True
    legs = 4
    name = None
    ears = True


    def __str__(self):
        return f"y {self.name} {self.legs} ноги и {'есть хвост' if self.has_tail else 'хвоста нет'}."\
               f"у него {'есть ушки' if self.ears else 'нет ушек'}."

    def sound(self):
        pass


class Dog(Pet):
    name = "Bulat"

    def sound(self):
        return "gav!"


print(Dog())
print(Dog().sound())


class Frog(Pet):
    has_tail = False
    ears = False
    name = "pepe"

    def sound(self):
        return "kva!"



print(Frog(), Frog().sound())