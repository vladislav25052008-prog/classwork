class Printer:
    def print_document(self,document):
        print(f"printing {document}")

class Scanner:
    def scan_document(self,document):
        print(f"scanning {document}")

class MultiFunctionDevice(Printer,Scanner):
    pass


aio = MultiFunctionDevice()

aio.print_document("group.pdf")
aio.scan_document("scan_passport.jpg")


class Character:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def show_info(self):
        print(f"name: {self.name} health: {self.health}")

class Warrior(Character):
    def attack(self):
        print(f"{self.name} attack with sword!")

class Mage(Character):
    def cast_spell(self):
        print(f"{self.name} cast a spell!")


class BattleMage(Warrior, Mage):
    pass

hero = BattleMage("Arthas", 100)
hero.attack()
hero.cast_spell()
hero.show_info()
print(BattleMage.mro())
