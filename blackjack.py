
import random
import itertools
import pdb
import sys

suits = 'cdhs'
ranks = '23456789TJQKA'
deck = [card for card in itertools.product(ranks, suits)]#*4 ## add in multiple decks to play

random.shuffle(deck)

def cardDeal():
	card = deck.pop()
	return card	

def handClear(player, dealer):
	player.action = 'deal'
	player.bet = 0
	player.hand = []
	dealer.action = 'deal'
	dealer.hand = []


def chickenDinner(player, dealer):
	print("player score: %s, dealer score: %s" % (player.score, dealer.score))
	if player.score > 21:
		player.bet *= -1
		print("Player busts")
	elif player.score == 21 and len(player.hand) == 2:
		player.bet *= 2.5
		print("Player blackjack!")
	elif player.score > dealer.score or dealer.score > 21:
		player.bet *= 2
		print("Player wins!")
	elif player.score < dealer.score:
		player.bet *= -1
		print("Player loses.")
	elif player.score == dealer.score:
		player.bet *= 0
		print("Game draw.")
	else:
		print("how did we get here?")
	player.chips += player.bet


class player:
	chips = 300
	score = 0
	ace = False
	bet = 0
	action = 'deal'
	hand = []

	def newGame(self):
		while len(self.hand) < 2:
			self.hand.append(cardDeal())

	def betting(self):
		while self.bet == 0:
			user = raw_input('''Place bet or press ENTER to cashout
>''')
			if not user:
				sys.exit()
			elif user.isdigit():
				if int(user) < 10:
					print("Table minimum is 10")
				elif int(user) > self.chips:
					print("You only have %s credits" % (self.chips))
				else:
					self.bet = int(user)
					print("You bet %s" % (self.bet))
			else:
				print("invalid input.")

	def deal(self):
		cardDeal(self.hand)
		print(hand)		

	def handCalc(self):
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
					self.ace = False
				else:
					self.score += 11	
					self.ace = False

	def playerInput(self):
		self.handCalc()
		if self.score < 22:
			print(self.hand)
			if self.score == 21:
				print("Player has %s, dealer assumes stay." % (self.score))
				self.action = 'stay'
			else:
				print("Dealer hand: %s & one face down." % str(house.hand[0][0]))
				print(("Current hand sum: %s") % (self.score))	
				self.action = raw_input('''What would you like to do?
HIT or STAY
>''').lower()
				self.playerAction()

	def playerAction(self):
		while self.bet == 0:
			self.betting()

		if self.score < 22 or self.action != 'stay':
			if self.action == 'deal':
				self.handCalc()
				self.playerInput()
			elif self.action == 'hit':
				self.hand.append(cardDeal())
				self.playerInput()
				self.handCalc()
			elif self.action == 'stay':
				print("Stayed at %s" % (self.score))
			else:
				print("Incorrect input.")
				self.playerInput()
		else:
			print("you broke 2")


class dealer:
	ace = False
	hand = []
	score = 0
	action = 'deal'

	def newGame(self):
		while len(self.hand) < 2:
			self.hand.append(cardDeal())
			self.handCalc()

	def deal(self):
		cardDeal(self.hand)
		print(hand)


		#self.bet = raw_input('How much will you bet? > ')

	def handCalc(self):
		self.score = 0
		if self.hand[0][0] == 'A':
			#print("Would you like to buy insurance?")
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
			if self.score == 21 and len(self.hand) == 2 and self.action == 'deal':
				print("Dealer blackjack.")
				self.action = None
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

x = True
player1 = player()
house = dealer()
while x is True:
	player1.newGame()
	house.newGame()
	player1.playerAction()
	house.dealerAction()

	if player1.score > 21:
		print("Final hand %s, break at %s" % (player1.hand, player1.score))
	else:
		print("Player stayed at %s, hand was %s" % (player1.score, player1.hand))

	chickenDinner(player1, house)
	print("You received: %s, Total chip count: %s" % (player1.bet, player1.chips))
	handClear(player1, house)

#dealer.newGame()
#dealer.checkScore()