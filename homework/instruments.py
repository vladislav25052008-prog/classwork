class Instrument:
    def __init__(self, name):
        self.name = name

    def play(self):
        raise NotImplementedError("the play method must be implemented in a subclass")


# 2
class StringInstrument(Instrument):
    def play(self):
        print(f"{self.name}: towww-tooow")


class WindInstrument(Instrument):
    def play(self):
        print(f"{self.name}: toot-toot-toot")


class PercussionInstrument(Instrument):
    def play(self):
        print(f"{self.name}: boom-boom")


# 3
class Guitar(StringInstrument):
    def __init__(self):
        super().__init__("guitar")

    def tune(self):
        print("the guitar is tuned")


class Flute(WindInstrument):
    def __init__(self):
        super().__init__("flute")


class Drum(PercussionInstrument):
    def __init__(self):
        super().__init__("drum")


# 4
guitar = Guitar()
flute = Flute()
drum = Drum()

guitar.tune()
for instrument in (guitar, flute, drum):
    instrument.play()
print()


# 5
class HybridInstrument(StringInstrument, WindInstrument, PercussionInstrument):
    def __init__(self):
        super().__init__("Hybrid")

    def play(self):
        StringInstrument.play(self)
        WindInstrument.play(self)
        PercussionInstrument.play(self)


# 6
hybrid = HybridInstrument()
hybrid.play()