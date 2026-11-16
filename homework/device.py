class Device:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def turn_on(self):
        print(f"{self.brand} turned on")

    def turn_off(self):
        print(f"{self.brand} turned off")

    def info(self):
        print(f"device: {self.brand}, power: {self.power} W")


class CoffeeMachine(Device):
    def __init__(self, brand, power, water_volume):
        super().__init__(brand, power)
        self.water_volume = water_volume

    def make_coffee(self):
        print("Coffee is ready")

    def info(self):
        super().info()
        print(f"Water volume: {self.water_volume} л")


class Blender(Device):
    def __init__(self, brand, power, speeds):
        super().__init__(brand, power)
        self.speeds = speeds

    def blend(self):
        print("blender mixed products")

    def info(self):
        super().info()
        print(f"speeds: {self.speeds}")


class MeatGrinder(Device):
    def __init__(self, brand, power, productivity):
        super().__init__(brand, power)
        self.productivity = productivity

    def grind(self):
        print("meatgrinder grinds a meat")

    def info(self):
        super().info()
        print(f"productivity: {self.productivity} kg/m")


coffee = CoffeeMachine("DeLonghi", 1450, 1.8)
coffee.info()
coffee.turn_on()
coffee.make_coffee()
print()

blender = Blender("Philips", 450, 5)
blender.info()
blender.blend()
print()

grinder = MeatGrinder("Bosch", 1500, 1.7)
grinder.info()
grinder.grind()

