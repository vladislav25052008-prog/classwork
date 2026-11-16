# from idlelib.debugobj_r import remote_object_tree_item
# from os import name
#
#
# class BankAccount:
#     def __init__(self, owner, balance):
#         self._owner = owner
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         return self.__balance
#
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"top up {amount} uah")
#
#     def show_info(self):
#         print(f"owner: {self._owner} top up {self.__balance} uah")
#
#
#
#
# class PremiumAccount(BankAccount):
#     def __init__(self,owner,balance,cashback):
#         super().__init__(owner,balance)
#         self._cashback = cashback
#
#     def show_info(self):
#         super().show_info()
#         print(f"Owner: {self._owner}, Cashback: {self._cashback}")
#
# account = PremiumAccount('Max',5000,5)
# account.deposit(1000)
# account.show_info()
#
# print(account.balance)
#
#
#
# class User:
#     @staticmethod
#     def validate_password(password):
#         if password == 'qwerty1':
#             return len(password) >= 6 and any(c.isdigit() for c in password)
#
#
#
#
# print(User.validate_password("hello"))
# print(User.validate_password("qwerty1"))
#
#
#
# class Player:
#     total_players = 0
#     def __init__(self,name):
#         self._name = name
#         Player.total_players += 1
#
#     @classmethod
#     def show_total(cls):
#         print(f" total players {cls.total_players}")
#
#
# player1 = Player("Max")
# player2 = Player("jane")
# player3 = Player("bob")
#
#
# Player.show_total()
#
#
# class Product:
#     discount = 10
#
#
#     def __init__(self,name,price):
#         self._name = name
#         self._price = price
#
#     def final_price(self):
#         return self._price * (1 - self.discount /100)
#
#
#
#     @classmethod
#     def change_discount(cls,value):
#         cls.discount = value
#
#
#     @staticmethod
#     def is_valid_price(price):
#         return price > 0
#
# pr1 = Product("milk",100)
# pr2 = Product("meat",200)
#
#
# print(pr1.final_price())
# print(pr2.final_price())
# print(pr1.is_valid_price(pr2.final_price()))
#
#
# class Temperature:
#     absolute_zero = -273.15
#
#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return c * 9 / 5 + 32
#
#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return (f - 32) * 5/9
#
#     @staticmethod
#     def is_valid_temperature(c):
#         return c < Temperature.absolute_zero
#
# print(Temperature.celsius_to_fahrenheit(25))
# print(Temperature.fahrenheit_to_celsius(77))
# print(Temperature.is_valid_temperature(-300))



class User:
    total_users = 0

    def __init__(self,username,password):
        if not User.validate_password(password):
            raise ValueError(f"invalid password {password}")
        self._username = username
        self.__password = password
        User.total_users += 1

    def check_password(self,password):
        return password == self.__password

    @staticmethod
    def validate_password(password):
        return len(password) >= 8 and any(c.isdigit() for c in password)

    @classmethod
    def show_total_users(cls):
        print(f"total users: {cls.total_users} ")

class Admin(User):
    def __init__(self,username,password):
        super().__init__(username,password)
        self.is_admin = True

    def delete_user(self,username):
        print(f" admin {self._username} deleting user {username} ")


user1 = User("olena", "qwerty123")
user2 = User("taras", "password2024")

admin = Admin("Wanquish", "admin12345")


print(user1.check_password("qwerty123"))   # True
print(user1.check_password("12345"))

admin.delete_user("taras")

User.show_total_users()




