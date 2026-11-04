# Приклад без ООП
# student = {
#     "name": "Іван",
#     "age": 18,
#     "grade": 90
# }
#
#
# def show_student(student):
#     print(student["name"])
#     print(student["grade"])
#
#
# def change_grade(student, new_grade):
#     student["grade"] = new_grade
#
#
# show_student(student)
# change_grade(student, 95)
# show_student(student)
#
#

#
# class Student:
#    def __init__(self, name, age, grade):
#        self.name = name
#        self.age = age
#        self.grade = grade
#
#
#    def show_info(self):
#        print(self.name, self.grade)
#
#
#    def change_grade(self, new_grade):
#        self.grade = new_grade
#
#
#
#
# student = Student("Іван", 18, 90)
#
#
# student.show_info()
# student.change_grade(95)
# student.show_info()


class Car:
    pass


car1 = Car()
car1.brand = 'BMW'
car1.color = 'black'
print(car1.brand)
print(car1.color)
print(car1.__dict__)
car2 = Car()
car2.brand = "Toyota"
print(car2.brand)
# print(car2.color)


print(car1)
print(car2)
print(type(car1))
print(type(car2))

number = 1

print(1)
print("qwet")


class Student:
    school = 'Itstep'

    def __init__(self, name):
        self.name = name
        self.age = 0

    def show_info(self):
        print(self.name)
        print(self.age)

    def change_age(self, new_age):
        self.age = new_age


st1 = Student('Max')
st1.change_age(20)
st1.show_info()

st2 = Student('Ben')
st2.show_info()


class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def show_info(self):
        print(self.name)
        print(self._price)

    @property
    def price(self):    #getter
        return  self._price

    @price.setter
    def price(self, new_price):   # setter
        if new_price <= 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price



product1 = Product('iphone18', 1000)
product1.show_info()

product1.price = 2000

product1.price = -100
product1.show_info()


class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount cannot be negative")
            return

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount cannot be negative")
            return

        if amount > self.__balance:
            print("Amount cannot be greater than balance")
            return
        self.__balance -= amount

    def show_balance(self):
        return f"Balance: {self.__balance}"


account = BankAccount(100)

account.deposit(500)
account.withdraw(300)
account.__balance = -1000
print(account.show_balance())
print(account.__dict__)


class Calculator:
    def __double(self, num1):
        return num1 * 2

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def multi(self, num1, num2):
        return num1 * num2

    def calculate(self, number):
        return self.__double(number) + 33


calc = Calculator()
print(calc.calculate(2))


