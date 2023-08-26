from random import randint
from time import sleep
from os import system

class GamePlay():
    def __init__(self):
        self.bet_amt = 0
        self.counter = 1
        self.rounds = 5
        self.balance = 6
        self.dice1 = self.Dice()
        self.dice2 = self.Dice()
        self.records = {}
        self.gameplay()
    

    # place bet amount
    def bet(self):
        try:
            self.bet_amt = int(input(f"You have ${self.balance}. Please enter a bet amount (max is $4): "))
            
            # check for blank values
            if not self.bet_amt:
                raise ValueError
            
            # check bet_amt is valid
            if (self.bet_amt > self.balance) or (self.bet_amt < 1) or (self.bet_amt > 4):
                raise ValueError
        except:
            print("Invalid bet amount. Please try again.\n")
            self.bet()        

    
    # checks the result of the roll
    def check_win(self):
        '''Takes the bet amount from the player's balance then rolls the dice.
            If the dice values are the same, the player gets triple their bet amount
            If the dice values are sequential, the players gets double their bet amount
            Else, they lose their bet amount
        '''
        self.balance -= self.bet_amt
        d1 = self.dice1.roll()
        d2 = self.dice2.roll()

        if (d1 == d2):
            earn = self.bet_amt * 3
            self.balance += earn
            loss = 0
            print(f"You earn ${earn}.")
        elif (abs(d1 - d2) == 1):
            earn = self.bet_amt * 2
            self.balance += earn
            loss = 0
            print(f"You earn ${earn}.")

        else:
            loss = self.bet_amt
            earn = 0
            print(f"You lost ${loss}.")

        
        self.records [self.counter] = (self.bet_amt,d1,d2,earn,loss)


    #starts the game
    def gameplay(self):
        name = input("\nPlease enter your name: ")   

        # wait 1 second then clear the screen 
        sleep(1)
        system("CLS")    

        print(f"Welcome {name} to Dice Poker.")
        # print("\n\nHow to play:")
        # print("You'll be given a bank balance of $6 and five rounds to win extra cash. For each round, you will place a bet and two dices will be rolled.")
        # print("If the values on the dices are sequential then you will double your bet amount. If the values are equal, you will triple your bet amount.")
        # print("Else, you will forfeit your bet amount. You'll play until all five rounds have lapsed or your bank balance is depleted.")
        # print("Good luck")

        # sleep(15)
        # system("CLS")

        while self.counter <= self.rounds:
            if (self.balance == 0):
                print("You have no money remaining.")
                break
            
            self.bet()
            self.check_win()
            self.counter += 1
     
        print("\nGame has ended.\n")
        sleep(5)
        system("CLS")
        self.results(name)
        self.score_board(name)
        self.replay()
    

    # gives the user the option to play again
    def replay(self):
        '''Asks user if they would like to play again
           If yes, the program starts over.
           If no, the program ends.
           Any other values throws an error and the user is asked again.
        '''
        choice = input("\nWould you like to play again? Y/N: ").lower()
        if choice == "y":
            main()
        elif choice == "n":
            print("Thank you for playing. Good bye!")
        else:
            print("Choice not recognised. Try again.")
            self.replay()


    # displays the player's records and ending balance
    def results(self, name):
        for key, values in self.records.items():
            amt,roll1,roll2,earn,loss = values
            print(f"Round {key}: Bet amount - {amt}, Dice 1 - {roll1}, Dice 2 - {roll2}, Earn - {earn}, Loss - {loss}")
        
        print(f"{name}, you have ${self.balance} remaining.\n")
        sleep(8)
        system("CLS")


    # displays the game's leaderboard
    def score_board(self, name,):
        position = 1
        leaderboard = {
            "Jake Sully" : 22,
            "Gamora Galaxy" : 21,
            "Peter Quill" : 20,
            "Madmax" : 20,
            "Cinderella" : 20,
            "Tom Jerry" : 19,
            "Hermoine" : 18,
            "Bella Swan" : 18,
            "Naruto" : 16,
            "Anya Forger" : 16
        }

        leaderboard[name] = self.balance
        print("\n\nLEADER BOARD")

        # print leaderboard
        lb_sorted = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True) 
        for k,v in lb_sorted:
            print(f"{position}. Name: {k} \t Score: {v}")
            position += 1

        sleep(8)
        system("CLS")


    # nested Dice class
    class Dice():
        # Omit __init__() since we will be using only static methods.
                
        # roll dice function (chooses a random number between 1 and 6 inclusively)
        def roll(self):
            return randint(1,6)


# initializes the game object
def main():
    GamePlay()


# calls the main function to start the game
if __name__ == "__main__":
    main()
