# 1
import math


class Counter:
    value = 0

    def increase(self):
        Counter.value += 1

    def decrease(self):
        Counter.value -= 1

    def show(self):
        print(f"Поточне значення: {Counter.value}")


c1 = Counter()
c2 = Counter()
c1.show()
c1.increase()
c1.increase()
c1.show()


# 2
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f"title: {self.title}, author: {self.author}, pages: {self.pages}")


    def is_long(self):
        return self.pages > 300

book1 =Book("Shadows of Ourselfs", "Joe Black", 120)
book2 = Book("Viyna i Myr", "Lev Tolstoy", 1200)

book2.show_info()
print("long book", book2.is_long())


book1.show_info()
print("short book", book1.is_long())

# 3

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"balanced top up {amount} uah")
        else:
            print("top up might be more than 0")


    def show_balance(self):
        print(f"owner: {self.owner}, balance: {self.balance} uah")



account1 = BankAccount("ivan", 1000)
account2 = BankAccount("olena", 200)
account1.deposit(100)
account2.deposit(200)
account1.show_balance()
account2.show_balance()
account1.deposit(-100)




class Calculator:
    def __double(self, number):
        return number * 2

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def calculate(self, number):
        return self.__double(number) + 33

calc = Calculator()
print(calc.calculate(2))