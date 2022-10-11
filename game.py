from dice import Dice
from player import Player


class PlayGame:
    def __init__(self, name1, name2, goal, dice) -> None:
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self._goal = goal
        self.dice = Dice(dice)

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, goal: int) -> None:
        if isinstance(goal, int) is False:
            raise ValueError("goal must be an integer")
        elif goal < 1:
            raise ValueError("goal must be greater than 0")
            
        self._goal = goal

    def play(self) -> None:
        while True:
            p1_roll = self.dice.roll()
            p2_roll = self.dice.roll()

            if p1_roll == p2_roll:
                continue
            elif p1_roll > p2_roll:
                self.player1.add_points(p1_roll)
            else:
                self.player2.add_points(p2_roll)

            if self.player1.score > self.goal:
                print(f"{self.player1.name}: {self.player1.score}")
                break
            elif self.player2.score > self.goal:
                print(f"{self.player2.name}: {self.player2.score}")
                break
