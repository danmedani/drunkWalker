drunkWalker
===========

This game is a simulation of drunken numbers wandering around a 2 dimentional board. When these numbers run into each other, they combine and continue walking. The game ends when there's only 1 drunken number left. There's no strict winning or losing this game. You make your own rules. 

To generate a game file, do something like this:

python game_file_gen.py 10 10 0.3 1 1 > gameFile1

  Arg 1: height of board
  
  Arg 2: width of board
  
  Arg 3: chance of a non-zero number appearing in any given board position
  
  Args 4, 5: if we're going to put a number in a spot, make the number a random one between [arg4, arg5] - inclusive
  

And then to run the game, do something like this:

python game.py gameFile1 0.1

  Arg 1: game file name
  
  Arg 2: seconds between game iterations
  
  
Feel free to modify and make this cooler.

Have fun
