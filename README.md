# Software Development Assessment 2

## Specification
You should use all the programming concepts that you have been taught to implement a dice game called Dice Poker. In this game, the computer rolls two standard six-sided dice and you bet on the outcome. The outcome is the configuration of the numbers rolled (explanation below). 

### Game flow
You start with some money in your bank. You play a number of rounds, where for each round you place a bet and the computer rolls the dice, checks the result and modifies your bank balance. After certain conditions, the game ends and you're presented with some final information shown as a message box.

### Placing bets
Before the computer rolls the dice, you can bet some money from your bank.
If the numbers are sequential (e.g. 1 and 2, 5 and 4, etc. Not 6 and 1), you earn double your bet.
If the numbers are identical (rolling doubles), you earn triple your bet.
Otherwise, you win nothing therefore you lose the amount of money you bet.
Before placing a bet, the computer should inform you of your current bank balance.

### Additional rules
When the game starts you are given $6 in your bank. Each bet costs $1 and you are allowed to make up to five bets before the game ends. The game will end if you run out of money, or you have no more attempts left (you made all five bets). At the end of the game, you will be told which of these conditions has ended the game.

### Results display
Once the game has finished (all bets have been placed or you ran out of money) the computer will collate and display the results in a single message box, comprised by:
- One row per bet, displaying your bet, the numbers rolled, the amount of money earned or lost for that bet.
- One row at the end, displaying the amount of money that you have remaining in your bank at the end of the game.

### Advanced features (optional, but count towards your marks)
#### Variable bet amount
Allow the user to change how much they would like to bet and change the amount you win accordingly. Allow bets between $1 and $4 (integers only)

#### High score table
Create a high score table. The more money you have remaining in your bank at the end of the game the higher up the table you will be. In order to implement this, players will have to enter their name before they play. The high score table should be displayed as a separate message box after the results have been displayed at the end of the game ([Results Display](#results-display))
