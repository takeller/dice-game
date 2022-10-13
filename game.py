from dice import Dice
from player import Player


class PlayGame:
    def __init__(self, name1: str, name2: str, goal: int, dice: int) -> None:
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.goal = goal
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

            if self.dice.is_max_roll(p2_roll):
                self.player1.lose_points(p1_roll)

            if self.dice.is_max_roll(p1_roll):
                self.player2.lose_points(p2_roll)

            if self.is_winner(self.player1):
                self.print_win_message(self.player1)
                break
            elif self.is_winner(self.player2):
                self.print_win_message(self.player2)
                break

    def is_winner(self, player: Player) -> bool:
        if player.score >= self.goal:
            return True

        return False

    def print_win_message(self, player: Player) -> None:
        print(f"{player.name}: {player.score}")
