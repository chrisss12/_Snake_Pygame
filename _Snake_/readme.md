Snake game (using pygame library)

In the snake game, the player uses the arrow keys to move its body around the board.
When the snake eats an apple then it will grow. After eating the food the new apple
appears in random place. The game ends when the snake goes outside
the board (hits the wall) or moves into itself.

The control keys are:

"up"
"down"
"left"
"right".

Snake game step by step implementation:
1. Display the board (with grid) with snake inside (snake in the center of the board)
2. Display an apple on the board in random place
3. Snake control using keyboard
4. Writing the current score in the board, detection of eating food
5. Detection of situation on board (collision with the wall or itself)
6. Lengthening (growing longer), recreating food in random place
