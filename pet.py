class Pet:
    def __init__(self, name, hunger, energy, happiness):
        self.name = name
        self.hunger = hunger # int
        self.energy = energy # int
        self.happiness = happiness # int
        self.tricks =[] # list of strings

    def eat(self):
        self.hunger = max(0, self.hunger -4)
        self.happiness = min(10, self.happiness + 1)
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)


    def play(self):
        self.energy = min(10, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)


    def get_status(self):
        print(f"--{self.name}'s status")
        print(f"-- Hunger: {self.hunger} ")
        print(f"-- Energy: {self.energy} ")
        print(f"-- Happiness: {self.happiness} ")
    
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name}'s learned a new trick -- {trick}!")

    def show_tricks(self):
        print(f"come on boy, {''.join(self.tricks)} ")
