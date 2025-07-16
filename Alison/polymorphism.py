class Movements:
    @classmethod
    def move(self, thing):
        thing.walk()

class Bird:
    def walk(self):
        print("hopping...")

class Mammal:
    def walk(self):
        print("running...")

bird = Bird()
dog = Mammal()

Movements.move(bird)
Movements.move(dog)