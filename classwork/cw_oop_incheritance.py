class Animal:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self._color = color

    def show_info(self):
        print("name:", self._name)
        print("age:", self._age)
        print("color:", self._color)

class Cat(Animal):
    pass


class Dog(Animal):
    pass






class Cow(Animal):
    pass



cat = Cat("murka", 3, "ruby")
dog = Dog("barsik", 5, "black")
cow = Cow("byryonka", 7, "white-black")

cat.show_info()
dog.show_info()
cow.show_info()



class Vehicle:
    def __init__(self, name, speed):
        self._name = name
        self._speed = speed

    def move(self):
        print(f"{self._name} moving with speed {self._speed} km/h")


class Car(Vehicle):
    def move(self):
        print(f"car {self._name} moving with speed {self._speed} km/h")

    def honk(self):
        print("beep-beep!")


class Bicycle(Vehicle):
    def move(self):
        print(f"bicycle {self._name} spin pedals with speed {self._speed} km/h")

    def ring_bell(self):
        print("ding-dong!")


vehicle = Vehicle("Transport", 50)
car = Car("Toyota", 120)
bike = Bicycle("Ukraine", 25)

vehicle.move()
car.move()
car.honk()
bike.move()
bike.ring_bell()


class Person:
    def __init__(self, name):
        self._name = name


    def show_info(self):
        print("name:", self._name)
        


class Student(Person):
    def __init__(self, name,group):
        super().__init__(name)
        self._group = group

st = Student("John", "itstep")
st.show_info()
