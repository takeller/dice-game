from random import randint


class Dice:
    def __init__(self, sides: int) -> None:
        self._sides = sides

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, sides: int) -> None:
        if isinstance(sides, int) is False:
            raise ValueError("Sides must be an integer")
        elif sides < 2:
            raise ValueError("Sides must be greater than 1")

        self._sides = sides

    @property
    def max_roll(self):
        return self.sides 

    def roll(self) -> int:
        return randint(1, self.sides)
        