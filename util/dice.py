#! python3

from random import randint

class Dice():

    def __init__(self, dType):
        self.dieType = dType

    def roll(self, times=None):
        result = 0

        if times is not None:
            for i in range (0, times):
                result += randint(1, self.dieType)
        else:
            result = randint(1, self.dieType)

        return result

    def roll_list(self, times=None):
        result = []

        if times is not None:
            for i in range (0, times):
                result.append(randint(1, self.dieType))
        else:
            result.append(randint(1, self.dieType))

        return result

d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
d100 = Dice(100)
