import random
import sys

class Card(object):
    """ Author
        Represents a standard playing card."""

    def __init__(self,suit=0,rank=2):
        " Author "
        self.suit = suit
        self.rank = rank


    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        " Author "
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __repr__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self,other):
        return cmp((self.suit,self.rank),
                   (other.suit,other.rank))
        
class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in [0,1,2,3]:
            for rank in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
                self.cards.append(Card(suit,rank))
        
    def __str__(self):
        string=[]
        for card in self.cards:
            string.append(str(card))
        return ', '.join(string)

    def add_card(self,card):
        self.cards.append(card)

    def deal_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        self.shuffle()
        for card in range(num):
            hand.add_card(self.deal_card())

    def deal_hands(self, hands, num):
        assert hands * num <= len(self.cards), "Not enough cards..."
        allhands = []
        for hand in range(hands):
            hand = Hand()
            self.move_cards(hand, num)
            allhands.append(hand)
        return allhands

                
            
class Hand(Deck):
    " Represents a players hand (their cards) "

    def __init__(self, label = ''):
        self.cards = list()
        self.label = label


def find_defining_class(obj, meth_name):
    " Author "
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty     

    
if __name__ == '__main__':

    print sys.argv
    
        

