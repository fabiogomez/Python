from Dog import Dog
from Cat import Cat

if __name__ == "__main__":
    obj = Dog("Tommy", 2, "Labrador")
    obj.bark()

    cat = Cat("Kitty", 10, "Persian")
    cat.meow()
    print(cat.getAge())
    #print(cat.__age) # AttributeError: 'Cat' object has no attribute '__age'
