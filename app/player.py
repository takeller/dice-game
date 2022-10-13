class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self._score = 0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str) is False:
            raise ValueError("Name must be a string")

        if len(name.strip()) == 0:
            raise ValueError("Name must be at least 1 character long")
        self._name = name

    @property
    def score(self) -> int:
        return self._score

    def add_points(self, amount: int) -> None:
        self._score += amount
        print(f"{self.name} has gained {amount}. Total score is now {self.score} points")

    def lose_points(self, amount: int) -> None:
        self._score -= amount
        print(f"{self.name} has lost {amount}. Total score is now {self.score} points")