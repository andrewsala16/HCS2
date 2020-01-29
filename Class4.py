# Andrew Sala
# 4B

import random

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
    def __init__(self):
        self.rank = Card.rank[random.randint(0, len(Card.rank)-1)]
        self.suit = Card.suits[random.randint(0,3)]
        self.value = Card.value_calc(self)
    def value_calc(self):
        if self.rank == "J" or "Q" or "K":
            return 10
        elif self.rank == "A":
            return 11
        else:
            return self.value

class Hand:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.value = (card1.value, card2.value)

def play():
    card1 = Card()
    card2 = Card()
    card3 = Card()
    card4 = Card()
    myHand = Hand(card1, card2)
    otherHand = Hand(card3, card4)
    value1 = myHand.value
    value2 = otherHand.value
    print("Your cards are", myHand)
    print("CPU cards are", otherHand)
    if value1 > value2:
        print("YOU WIN")
    elif value1 == value2:
        print("Draw")
    elif value2 > value1:
        print("YOU LOST")

play()
