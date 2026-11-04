# class Car:
#     pass
#
# car1 = Car()
# car1.brand = "BMW"
# car1.color = "black"
# print(car1.brand)
# print(car1.color)
# print(car1.__dict__)

# car2 = Car()
# car2.brand = "toyota"
# print(car2.brand)
# print(car2.color)
# print(car2.__dict__)

# print(car1)
# print(car2)
# print(type(car1))
# print(type(car2))




class Student:
    school = "ITstep"

    def __init__(self,name):
        self.name = name
        self.age = 0

    def show_info(self):
        print(self.name)
        print(self.age)

    def change_age(self,new_age):
        self.age = new_age


st1 = Student("max")
st1.change_age(20)
st1.show_info()



st2 = Student("ben")
st2.change_age(30)
st2.show_info()


