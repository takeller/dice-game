# dice-game

### How to use
- Clone to your machine
- Navigate into dice-game directory
- Enter python shell: $python3
- Import PlayGame class: from game import PlayGame
- Initialize game: game = PlayGame(player1, player2, goal, dice) 
    - player 1: Name of player 1, String
    - player 2: Name of player 2, String
    - goal: Target score to win the game, Integer. Must be greater than 0
    - dice: Number of sides of the dice used to play the game, Integer. Must be greater than 1
- Play game: game.play()