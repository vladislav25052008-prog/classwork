class Student:
    def __init__(self, name, grade = 0):
        self.name = name
        self.__grade = 0
        self.set_grade(grade)

    def set_grade(self, value):
        if 0 <= value <= 12:
            self.__grade = value
        else:
            print(f"incorrect grade: {value}. grade must be between 0 and 12")

    def get_grade(self):
        return self.__grade

    def show_info(self):
        print(f"student: {self.name}, grade: {self.__grade}")


s1 = Student("Ivan", 9)
s1.show_info()

s1.set_grade(10)
s1.show_info()

s1.set_grade(13)
s1.set_grade(-1)
print("grade: ", s1.get_grade())

s2 = Student("Oleg", 15)
s2.show_info()
