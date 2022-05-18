class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def eat(self):
        print("Eating")
    
    def sleep(self):
        print("Sleeping")
    
    def reproduce(self):
        print("Reproducing")

    def getAge(self):
        return self.__age