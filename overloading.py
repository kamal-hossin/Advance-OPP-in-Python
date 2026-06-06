class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    # Method Overloading using default parameter
    def eat(self, food=None):
        if food is None:
            print("Rice, Meat, Fish")
        else:
            print(f"Eating {food}")


class Cricket_Player(Person):
    def __init__(self, name, age, height, weight, team):
        super().__init__(name, age, height, weight)
        self.team = team

    # Overridden + overloaded method
    def eat(self, food=None):
        if food is None:
            print("Protein, Vegetables, Meat")
        else:
            print(f"Cricketer eats {food}")

    def play_cricket(self):
        print("Playing cricket for", self.team)



sakib = Cricket_Player("Sakib", 36, 5.9, 72, "Bangladesh")

sakib.eat()
sakib.eat("Chicken")

sakib.play_cricket()