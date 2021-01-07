class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def make_sound(self):
        print('Print the actual animal sound')


class Dog(Pet):
    def __init__(self, name, owner, fur_colour):
        super().__init__(name, owner)
        self.fur_colour = fur_colour
    def make_sound(self):
            print("BARK!!")

class Cat(Pet):
    def __init__(self, name, owner, fur_colour):
        super().__init__(name, owner)
        self.fur_colour = fur_colour
    def make_sound(self):
        print("MEOW!!")

my_dog = Dog("Sandy", "Daisy", "White")
my_dog.make_sound()
print(my_dog.__dict__)
my_cat = Cat("Fluffy", "Daisy", "Brown")
my_cat.make_sound()
print(my_cat.__dict__)

