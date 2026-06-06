class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, name):
        self.name = name
        self.engine = Engine()   # Composition (Car HAS-A Engine)

    def drive(self):
        print(self.name, "is driving")
        self.engine.start()


my_car = Car("Toyota")
my_car.drive()