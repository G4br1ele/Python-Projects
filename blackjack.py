import random

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
suits = ("Hearts", "Spades", "Cloves", "Diamonds")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
          "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10,
          "King": 10, "Ace": 11}


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


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


class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bet = 0
        self.hand = []
        self.value = 0
        self.aces = 0

    def add_card(self, new_deck):
        self.hand.append(new_deck.remove_one())
        self.value += self.hand[-1].value
        if self.hand[-1].rank == "Ace":
            self.aces += 1
        self.adjust_for_aces()
        print(self.name + " has been dealt a " + str(self.hand[-1]))

    def select_bet(self):
        while True:
            try:
                self.bet = int(input("Select your bet: "))
            except TypeError:
                print("Please enter a valid number")
            else:
                if self.bet > self.money:
                    print("You do not have enough money")
                else:
                    break

    def adjust_for_aces(self):
        if self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def hit(self, new_deck, player1, dealer):
        answer = ""
        while answer not in ("Y", "N"):
            answer = input("Would you like to hit? (Y/N) ").upper()
        if answer == "Y":
            self.add_card(new_deck)
            print(f"Your hand is now worth {player1.value}")
        else:
            while dealer.value < 17:
                dealer.add_card(new_deck)
                print(f"Dealer's hand is now worth {dealer.value}")

    def win_bet(self):
        self.money += self.bet

    def lose_bet(self):
        self.money -= self.bet


def win_check(player1, dealer):
    hand_on = True
    if player1.value > 21:
        print(f"{player1.name} has gone Bust!")
        player1.lose_bet()
        hand_on = False
    elif player1.value == 21:
        print(f"{player1.name} you win with 21!")
        player1.win_bet()
        hand_on = False
    elif dealer.value > 21:
        print("Dealer has gone Bust!")
        player1.win_bet()
        hand_on = False
    elif dealer.value >= 17 and player1.value > dealer.value:
        print(f"{player1.name} has won with a score of {player1.value}")
        player1.win_bet()
        hand_on = False
    elif dealer.value > player1.value:
        print(f"Dealer has beat {player1.name} with {dealer.value}")
        player1.lose_bet()
        hand_on = False
    else:
        pass
    return hand_on


def replay():
    answer = ""
    while answer not in ("Y", "N"):
        answer = input("Play again? (Y/N) ").upper()
    if answer == "Y":
        player1.hand = []
        player1.value = 0
        player1.aces = 0
        dealer.hand = []
        dealer.value = 0
        dealer.aces = 0
        main()
    else:
        print(f"You leave the Blackjack table with ${player1.money}")
        pass


def main():
    if player1.money > 0:
        # Create and shuffle deck
        new_deck = Deck()
        new_deck.shuffle_deck()
        print(f"Welcome to the BlackJack Table! You have ${player1.money}")
        # Let player select a bet
        player1.select_bet()
        # Deal 2 cards to player and 1 to dealer
        player1.add_card(new_deck)
        player1.add_card(new_deck)
        dealer.add_card(new_deck)
        print(f"Your hand is now worth: {player1.value}")
        print(f"Dealer hand is now worth: {dealer.value}")
        # Start a loop and ask if player wants to hit
        game_on = True
        while game_on:
            player1.hit(new_deck, player1, dealer)
            if not win_check(player1, dealer):
                game_on = False
        # Reset the hand, value and aces of player and dealer
        replay()
    else:
        print("You are out of money!")
        quit()


if __name__ == "__main__":
    # Define players
    player1 = Player(str(input("Welcome! Choose your name: ")), 100)
    dealer = Player("Dealer", 0)
    # Run program
    main()
