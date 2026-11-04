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


