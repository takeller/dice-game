# dice-game

### How to use
- Clone to your machine
- Navigate into dice-game directory
- Enter python shell: $python3
- Import PlayGame class: from app.game import PlayGame
- Initialize game: game = PlayGame(player1, player2, goal, dice) 
    - player 1: String. Name of player 1
    - player 2: String. Name of player 2
    - goal: Integer. Target score to win the game. Must be greater than 0
    - dice: Integer. Number of sides of the dice used to play the game. Must be greater than 1
- Play game: game.play()


### Tests
- Tests are ran using pytest
- Use a virtual environment or have pytest install system wide
- From dice-game directory call $pytest