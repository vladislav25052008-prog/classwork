class Brain:
    def think(self):
        print("The brain is thinking")


class Heart:
    def beat(self):
        print("The heart is beating")


class Legs:
    def walk(self):
        print("The legs are walking")


class Hands:
    def take(self):
        print("The hands are taking an object")


class Human(Brain, Heart, Legs, Hands):
    def __init__(self, name):
        self.name = name

    def live(self):
        print(f"Human {self.name}:")
        self.think()
        self.beat()
        self.walk()
        self.take()


human = Human("John")
human.live()
