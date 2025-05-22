from typing import List

from cards import Card


class Rune:
	def __call__(self, combo: List[Card]) -> int:
		return 0


class StoneDamageRune(Rune):
	def __call__(self, combo: List[Card]) -> int:
		damage = 0
		for card in combo:
			if card.suit == Card.Suit.stone:
				damage += 10

		return damage
