import json
from abc import ABC, abstractmethod

class ShapeInterface(ABC):
    @abstractmethod
    def area(self):
        pass

class ThreeDimensionalShapeInterface(ABC):
    @abstractmethod
    def volume(self):
        pass

class ManageShapeInterface(ABC):
    @abstractmethod
    def calculate(self):
        pass
    



class Square(ShapeInterface, ManageShapeInterface):
    
    def __init__(self, length: int):
        self.length = length

    def area(self):
        return self.length * self.length

    def calculate(self):
        return self.area()

class Circle(ShapeInterface, ManageShapeInterface):

    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def calculate(self):
        return self.area()


class Cuboid(ShapeInterface, ThreeDimensionalShapeInterface, ManageShapeInterface):

    def __init__(self, length: int):
        self.length = length

    def area(self):
        return 6 * (self.length * self.length)
    def volume(self):
        return self.length ** 3
    def calculate(self):
        return self.area()


class AreaCalculator:

    def __init__(self, shapes: list):
        self.shapes = shapes

    def sum(self):
        area = [0] * len(self.shapes)
        for idx, shape in enumerate(self.shapes):
            if isinstance(shape, ManageShapeInterface):
                area[idx] = shape.calculate()
            
            
        return sum(area)

class VolumeCalculator(AreaCalculator):

    def __init__(self, shapes: list):
        self.shapes = shapes

    def sum(self):
        volume = [0] * len(self.shapes)
        for idx, shape in enumerate(self.shapes):
            if isinstance(shape, ThreeDimensionalShapeInterface):
                volume[idx] = shape.volume()
            
            
        return sum(volume)

class SumCalculatorOutputter:
    _calculator = None
    def __init__(self, calculator: AreaCalculator):
        self._calculator = calculator

    def JSON(self):
        return json.dumps({"sum": "{:.2f}".format(self._calculator.sum())})
    def HTML(self):
        return "<h1>{:.2f}</h1>".format(self._calculator.sum())

    


area_calculator = AreaCalculator([Square(2), Circle(3), Square(4)])
volume_calculator = VolumeCalculator([Square(2), Circle(3), Cuboid(4)])

output = SumCalculatorOutputter(area_calculator)
output2 = SumCalculatorOutputter(volume_calculator)

print(output.JSON())
print(output.HTML())

print(output2.JSON())
print(output2.HTML())

class DBConnectionInterfaz(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLConnection(DBConnectionInterfaz):
    def connect(self):
        print("MySQL connection")

class PasswordReminder:
    _db_connection = None
    def __init__(self, db_connection: DBConnectionInterfaz):
        self._db_connection = db_connection

    def send_password(self):
        self._db_connection.connect() 

