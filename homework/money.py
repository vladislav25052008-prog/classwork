class Money:
    def __init__(self, whole=0, cents=0):
        self.whole = whole
        self.cents = cents

    def set_whole(self, whole):
        self.whole = whole

    def set_cents(self, cents):
        self.cents = cents

    def show(self):
        print(f"{self.whole}.{self.cents:02d}")


class Product(Money):
    def __init__(self, name, whole, cents):
        super().__init__(whole, cents)
        self.name = name

    def decrease_price(self, whole, cents):
        total = (self.whole * 100 + self.cents) - (whole * 100 + cents)
        if total < 0:
            total = 0
        self.whole = total // 100
        self.cents = total % 100

    def show(self):
        print(f"{self.name}: {self.whole}.{self.cents:02d}")


money = Money(10, 50)
money.show()
money.set_whole(20)
money.set_cents(75)
money.show()

product = Product("Milk", 42, 90)
product.show()
product.decrease_price(5, 95)
product.show()