from Animal import Animal

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        
    def bark(self):
        print("Woof!")
        
    def eat(self):
        print("Eating")
        
    def sleep(self):
        print("Sleeping")
        
    def reproduce(self):
        print("Reproducing")



