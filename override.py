class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        

        def eat(self):
            print("Rice , Meat , Fish")

class Cricket_Player(Person):
    def __init__(self, name, age, height, weight, team):
        super().__init__(name, age, height, weight)
        self.team = team

    def eat(self):
        print("Protein , Vegetables , Meat")    

    def play_cricket(self):
        print("Playing cricket for", self.team)            