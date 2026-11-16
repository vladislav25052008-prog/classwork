class Ship:
    def __init__(self, name, length, speed):
        self.name = name
        self.length = length
        self.speed = speed

    def sail(self):
        print(f"{self.name} is sailing at {self.speed} knots")

    def info(self):
        print(f"ship: {self.name}, length: {self.length} m, speed: {self.speed} knots")


class Frigate(Ship):
    def __init__(self, name, length, speed, helicopters):
        super().__init__(name, length, speed)
        self.helicopters = helicopters

    def escort(self):
        print(f"frigate {self.name} is escorting vessels")

    def info(self):
        super().info()
        print(f"helicopters: {self.helicopters}")


class Destroyer(Ship):
    def __init__(self, name, length, speed, torpedoes):
        super().__init__(name, length, speed)
        self.torpedoes = torpedoes

    def attack(self):
        print(f"destroyer {self.name} is attacking with torpedoes")

    def info(self):
        super().info()
        print(f"torpedoes: {self.torpedoes}")


class Cruiser(Ship):
    def __init__(self, name, length, speed, guns):
        super().__init__(name, length, speed)
        self.guns = guns

    def fire(self):
        print(f"cruiser {self.name} is firing {self.guns} guns")

    def info(self):
        super().info()
        print(f"guns: {self.guns}")


frigate = Frigate("Hetman Sahaidachny", 123, 32, 1)
frigate.info()
frigate.sail()
frigate.escort()
print()

destroyer = Destroyer("Storm", 150, 33, 8)
destroyer.info()
destroyer.attack()
print()

cruiser = Cruiser("Ukraine", 186, 32, 4)
cruiser.info()
cruiser.fire()
