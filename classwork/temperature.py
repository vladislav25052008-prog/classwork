class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius


    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Celsius is less than -273.15")
        self.__celsius = value

    def to_fahrenheit(self):
        return round(self.celsius * 9 / 5 + 32, 2)



t = Temperature(25)
print(t.celsius , t.to_fahrenheit())

t.celsius = 100
print(t.celsius, t.to_fahrenheit())

t.celsius = -273.15
print(t.celsius, t.to_fahrenheit())


