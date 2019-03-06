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


def take_bet(chips):
	while True:
		try:
			chips.bet = int(input('Place your bet ')) 
		except:
			print("Please enter the amount of your bet in numbers")
		else:
			if chips.bet > chips.total:
				print("Sorry, your bet can't exceed ",chips.total)
			else:
				break

def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing  # to control an upcoming while loop

	while True:
		x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

		if x[0].lower() == 'h':
			hit(deck,hand)  # hit() function defined above
		elif x[0].lower() == 's':
			print("Player stands. Dealer is playing.")
			playing = False
		else:
			print("Sorry, please try again.")
			continue
		break

def show_some(player,dealer):
	print("\nPlayer's hand :")
	for item in player.cards:
		print(f'\t{item}')
	print(f'\tTotal={player.value} \n')
	
	total_dealer = 0
	print("Dealer's hand :")
	for index in range(0,len(dealer.cards)-1):
		print(f'\t{dealer.cards[index]}')
		total_dealer += values[dealer.cards[index].rank]
	print(f'\tTotal={total_dealer}')
	
def show_all(player,dealer):
	print("\nPlayer's hand :")
	for item in player.cards:
		print(f'\t{item}')
	print(f'\tTotal={player.value} \n')
	
	print("Dealer's hand :")
	for item in dealer.cards:
		print(f'\t{item}')
	print(f'\tTotal={dealer.value}')

def player_busts(chips):
	chips.lose_bet()
	print('\nDommage! You busts!')

def player_wins(chips):
	chips.win_bet()
	print('\nCongratulations! You won the round!')

def dealer_busts(chips):
	chips.win_bet()
	print('\nDealer busts! Congratulations! You won the round!')
	
def dealer_wins(chips):
	chips.lose_bet()
	print('\nDealer wins!')
	
def push():
	print("\nDealer and Player tie! It's a push.")    

def main():
	global playing

	while True:
		# Print an opening statement
		print("Welcome to BlackJack. Let's have some fun, shall we?")

		# Create & shuffle the deck, deal two cards to each player
		deck = Deck()
		deck.shuffle()
		
		player = Hand()
		dealer = Hand()
		
		player.add_card(deck.deal())
		dealer.add_card(deck.deal())
		player.add_card(deck.deal())
		dealer.add_card(deck.deal())
			
		# Set up the Player's chips
		player_chips = Chips()
		print(f"You have {player_chips.total} chips. Have fun!")
		
		# Prompt the Player for their bet
		take_bet(player_chips)
		
		# Show cards (but keep one dealer card hidden)
		show_some(player,dealer)
		
		while playing:  # recall this variable from our hit_or_stand function
			
			# Prompt for Player to Hit or Stand
			hit_or_stand(deck,player)
			
			# Show cards (but keep one dealer card hidden)
			show_some(player,dealer)
			
			# If player's hand exceeds 21, run player_busts() and break out of loop
			if player.value > 21:
				player_busts(player_chips)
				break
				
				
		# If Player hasn't busted, play Dealer's hand until Dealer reaches 17
		if player.value <= 21:
			while dealer.value < 17:
				hit(deck,dealer)

			# Show all cards
			show_all(player,dealer)

			# Run different winning scenarios
			if (player.value == 21 and dealer.value == 21) or (player.value > 21 and dealer.value > 21):
				push()
			elif player.value == 21:
				player_wins(player_chips)
			elif dealer.value == 21:
				dealer_wins(player_chips)
			elif player.value > 21:
				player_busts(player_chips)
			elif dealer.value > 21:
				dealer_busts(player_chips)
			elif (player.value > dealer.value):
				player_wins(player_chips)
			elif (dealer.value > player.value):
				dealer_wins(player_chips)

		# Inform Player of their chips total 
		print(f"You have {player_chips.total} chips")
		# Ask to play again
		play = str(input('Do you want to play again?, enter y/n : '))
		print('\n')

		while not (play[0].lower() == 'y' or play[0].lower() == 'n'):
			play = str(input('Please enter y/n : '))

		if play[0].lower() == 'y':
			playing = True
			continue
		else:
			print("Thanks for playing!")
			break

if __name__ == '__main__':

	main()