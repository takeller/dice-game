import pytest

from app.game import PlayGame

def test_basic():
    assert 2 == 2

class TestPlayGame:
    def test_can_initialize(self):
        game = PlayGame('Player1', 'Player2', 25, 5)

        assert isinstance(game, PlayGame)

class TestPlayGamePlay:
    def test_can_play_game(self):
        game = PlayGame('Player1', 'Player2', 25, 5)
        game.play()

        assert game.player1.score >= game.goal or game.player2.score >= game.goal

class TestPlayGameInputValidation:
    def test_cant_initialize_with_non_string_player_name(self):
        with pytest.raises(ValueError):
            game = PlayGame(1, 'Player2', 25, 5)
            
        with pytest.raises(ValueError):
            game = PlayGame('Player1', 1, 25, 5)

    def test_cant_initialize_with_empty_player_name(self):
        with pytest.raises(ValueError):
            game = PlayGame("", 'Player2', 25, 5)
            
        with pytest.raises(ValueError):
            game = PlayGame('Player1', "", 25, 5)

    def test_cant_initialize_with_all_whitespace_player_name(self):
        with pytest.raises(ValueError):
            game = PlayGame(" ", 'Player2', 25, 5)
            
        with pytest.raises(ValueError):
            game = PlayGame('Player1', "     ", 25, 5)

    def test_cant_initialize_with_non_int_goal(self):
        with pytest.raises(ValueError):
            game = PlayGame("Player1", 'Player2', '25', 5)

    def test_cant_initialize_with_goal_less_than_one(self):
        with pytest.raises(ValueError):
            game = PlayGame("Player1", 'Player2', 0, 5)

        with pytest.raises(ValueError):
            game = PlayGame("Player1", 'Player2', -5, 5)

    def test_cant_initialize_with_non_int_dice(self):
        with pytest.raises(ValueError):
            game = PlayGame("Player1", 'Player2', 0, '5')

    def test_cant_initialize_with_dice_less_than_two(self):
        with pytest.raises(ValueError):
            game = PlayGame("Player1", 'Player2', 0, 1)

        with pytest.raises(ValueError):
            game = PlayGame("Player1", 'Player2', 0, -51)


