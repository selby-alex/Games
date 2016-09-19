
import random
import itertools
import pdb

suits = 'cdhs'
ranks = '23456789TJQKA'
deck = [card for card in itertools.product(ranks, suits)]#*4 ## add in multiple decks to play

random.shuffle(deck)

def cardDeal():
	card = deck.pop()
	return card	

def chickenDinner(player, dealer):
	print("player score: %s, dealer score: %s" % (player.score, dealer.score))
	if player.score > 21:
		print("Player busts")
		#player.bet *= 0
	elif player.score == 21 and len(player.hand) == 2:
		print("Player blackjack!")
		#player.bet *= 2.5
	elif player.score > dealer.score or dealer.score > 21:
		print("Player wins!")
		#player.bet *= 2
	elif player.score < dealer.score:
		print("Player loses.")
		#player.bet *= 0
	elif player.score == dealer.score:
		print("Game draw.")
		#player.bet *= 1
	else:
		print("how did we get here?")

class player:
	chips = 300
	score = 0
	ace = False
	action = 'deal'
	hand = []

	def deal(self):
		cardDeal(self.hand)
		print(hand)

	def newGame(self):
		while len(self.hand) < 2:
			self.hand.append(cardDeal())

	def handCalc(self):
		if self.score < 22:
			self.score = 0
			for val, suit in self.hand:
				#for face in ['T','J','Q','K']:
				if val == 'A':
					self.ace = True
				elif val in ['T','J','Q','K']:
					self.score += 10
				else:
					self.score += int(float(val))
				#print(self.score)

			if self.ace:
				if self.score + 11 > 21:
					self.score += 1
				else:
					self.score += 11
			self.ace = False
			return

	def playerInput(self):
		self.handCalc()
		if self.score < 22:
			print(self.hand)
			if self.score == 21:
				print("Player has %s, dealer assumes stay." % (self.score))
				self.action = 'Stay'
			else:
				print("Dealer hand: %s & one face down." % str(house.hand[0][0]))
				print(("Current hand sum: %s") % (self.score))	
				self.action = raw_input('''What would you like to do?
Hit
Stay
>''') 
				self.playerAction()

	def playerAction(self):
		if self.score < 22 or self.action != 'Stay':
			if self.action == 'deal':
				self.newGame()
				self.handCalc()
				self.playerInput()
			elif self.action == 'Hit':
				self.hand.append(cardDeal())
				self.playerInput()
				self.handCalc()
			elif self.action == 'Stay':
				print("Stayed at %s" % (self.score))
			else:
				print("Incorrect input.")
				self.playerInput()
		else:
			print("you broke 2")


class dealer:
	hand = []
	ace = False
	hand = []
	score = 0
	action = 'deal'
	chip = 200
	bet = 0

	def deal(self):
		cardDeal(self.hand)
		print(hand)

	def newGame(self):
		while len(self.hand) < 2:
			self.hand.append(cardDeal())
			self.handCalc()
		#self.bet = raw_input('How much will you bet? > ')

	def handCalc(self):
		self.score = 0
		if self.hand[0][0] == 'A':
			print("Would you like to buy insurance?")
			for val, suit in self.hand:
				if val == 'A':
					self.ace = True
				elif val in ['T','J','Q','K']:
					self.score += 10
				else:
					self.score += int(float(val))

			if self.ace:
				if self.score + 11 > 21:
					self.score += 1
				else:
					self.score += 11
		else:
			for val, suit in self.hand:
				if val == 'A':
					self.ace = True
				elif val in ['T','J','Q','K']:
					self.score += 10
				else:
					self.score += int(float(val))

			if self.ace:
				if self.score + 11 > 21:
					self.score += 1
				else:
					self.score += 11

	def dealerAction(self):
		print("Dealer reveals: %s" % (self.hand))
		while self.action == 'deal':
			if self.score == 21 and len(self.hand) == 2:
				print("Dealer blackjack.")
			elif self.score < 17 and self.action == 'deal':
				self.hand.append(cardDeal())
				print("Dealer hits %s, %s" % (str(self.score), self.hand))
				self.handCalc()
			elif self.score > 21:
				print("Dealers busts at %s" % (self.score))
				self.action = None
			else:
				print("Dealer Stays at %s" % (self.score))
				self.action = None

player1 = player()
house = dealer()
player1.newGame()
house.newGame()
#print "Dealer hand is: " + str(house.hand[1])
player1.playerAction()
house.dealerAction()

if player1.score > 21:
	print("Final hand %s, break at %s" % (player1.hand, player1.score))
else:
	print("Player stayed at %s, hand was %s" % (player1.score, player1.hand))

chickenDinner(player1, house)

#dealer.newGame()
#dealer.checkScore()