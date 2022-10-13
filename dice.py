from random import randint


class Dice:
    def __init__(self, sides: int) -> None:
        self.sides = sides

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
    def is_max_roll(self, roll: int) -> bool:
        return roll == self.sides

    def roll(self) -> int:
        return randint(1, self.sides)
        