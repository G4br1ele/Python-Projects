import random

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
suits = ("Hearts", "Spades", "Cloves", "Diamonds")
values = {"Two": 2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    
class Deck:
    
    def __init__(self):
        self.all_cards = []
        for rank in ranks:
            for suit in suits:
                self.all_cards.append(Card(rank, suit))
    
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        
    def remove_one(self):
        return self.all_cards.pop()
    
    def __str__(self):
        return str(len(self.all_cards))
    
class Player:
    
    def __init__(self, name):
        self.name = name
        self.cards = []
        
    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)
            
    def remove_card(self):
        return self.cards.pop()
    
def replay():
    answer = ""
    while answer not in ("Y", "N"):
        answer = input("Would you like to play again? (Y/N) ").upper()
    if answer == "Y":
        main()
    else:
        pass
    
    
def main():
    # set up the game
    player1 = Player(str(input("Player 1 choose your name: ")))
    player2 = Player("Computer")
    
    new_deck = Deck()
    new_deck.shuffle_deck()
    
    for num in range(26):
        player1.cards.append(new_deck.remove_one())
        player2.cards.append(new_deck.remove_one())
                
    game_on = True
    round_number = 0
    
    while game_on:
        # play the game
        round_number += 1
        print(f"Round {round_number}")
        
        if len(player1.cards) == 0:
            print(f"{player1.name} is out of cards!")
            print("Computer has won!")
            game_on = False
            break
        
        if len(player2.cards) == 0:
            print("Computer is out of cards!")
            print(f"{player1.name} has won!")
            game_on = False
            break
        
        player1_hand = []
        player1_hand.append(player1.remove_card())
        
        player2_hand = []
        player2_hand.append(player2.remove_card())
        
        war = True
        
        while war:
            
            if player1_hand[-1].value > player2_hand[-1].value:
                player1.add_cards(player1_hand)
                player1.add_cards(player2_hand)
                war = False
                
            elif player1_hand[-1].value < player2_hand[-1].value:
                player2.add_cards(player1_hand)
                player2.add_cards(player2_hand)
                war = False
                
            else:
                
                print("WAR!")
                
                if len(player1.cards) < 3:
                    print(f"{player1.name} does not have enough cards for the war!")
                    print("Computer has won!")
                    game_on = False 
                    break
                    
                elif len(player2.cards) < 3:
                    print("Computer does not have enough cards for the war!")
                    print(f"{player1.name} has won!")
                    game_on = False 
                    break
                    
                else:
                    for num in range(3):
                        player1_hand.append(player1.remove_card())
                        player2_hand.append(player2.remove_card())
                        break
    
    replay()
                    
if __name__ == "__main__":
    main()   
            