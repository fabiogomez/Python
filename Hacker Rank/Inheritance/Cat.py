from Animal import Animal

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def meow(self):
        print("Meow")
        
    def eat(self):
        print("Eating")
        
    def sleep(self):
        print("Sleeping")
        
    def reproduce(self):
        print("Reproducing")


