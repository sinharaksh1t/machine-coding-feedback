from random import randint


class Dice:
    def __init__(self, sides=6):
        if sides <= 0:
            raise ValueError("sides must be a positive integer")
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)
