from typing import Generator
import random

from cards import gen_cards


class Deck:
	''' Колода карт '''

	def __init__(self):
		self.all_cards = gen_cards()
		self.now_cards = self.all_cards[:]

	def get_card(self) -> Generator:
		''' Достать карту из колоды '''

		shuffle_deck = self.now_cards[:]
		random.shuffle(shuffle_deck)

		for card in shuffle_deck:
			self.now_cards.remove(card)
			yield card

		self.now_cards = self.all_cards
