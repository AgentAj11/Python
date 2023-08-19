class Farmer:
    """This is a farmer's class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.profession = "farming"
        self.farm_size = "50000 sq meter"
        self.crops = {
            'fruits' : ['Grapes', 'Mango', 'Banana'],
            'vegetables' : ['Potato', 'Sweet Potato', 'Pumpkin'],
            'tree' : ['Teek', 'Sal']
        }

    def farm_info(self):
        print(f"Name of farmer : {self.name}")
        print(f"Farmer's age : {self.age}")
        print(f"Favourite profession : {self.profession}")
        print(f"Farm size : {self.farm_size}")
        print(f"Annual major crops : {self.crops}")

    def sowen_crops(self):
        return self.crops

    def harvest(self):
        return ['Potato', 'Sweet Potato', 'Pumpkin', 'Grapes', 'Mango', 'Banana']


farmer1 = Farmer("Ajay Gaurav", 21.5)

farmer1.farm_info()

print(f"Crops sowed by {farmer1.name} : {farmer1.sowen_crops()}")
print(f"{farmer1.name}'s harvest = {farmer1.harvest()}")


