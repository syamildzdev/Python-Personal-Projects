import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        return '\n'.join([card.__str__() for card in self.deck])
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        if self.aces > 0:
            if self.value > 21:
                self.value -= 10
                self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet():
    while True:
        try:
            bet = int(input('Place your bet ')) 
        except:
            print("Unexpected error! Please try again ")
        else:
            break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        try:
            hit_or_stand = str(input('Hit or Stand? Enter h for Hit and s for Stand'))
        except:
            print('Please try again')
        else:
            if hit_or_stand.lower() == 'h':
                hit(deck,hand)
            elif hit_or_stand.lower() == 's':
                playing = False
            break                

def show_some(player,dealer):
    print("Player's hand :")
    for item in player.cards:
        print(f'\t{item}')
    print(f'\tTotal={player.value} \n')
    print("Dealer's hand :")
    print('\t'+ str(dealer.cards[0]))
    print(f'\tTotal={dealer.value}')            