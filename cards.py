import enum
from typing import List
from dataclasses import dataclass


class Suit(enum.Enum):
	''' Масть карты '''

	stone = 1
	moon = 2
	fire = 3
	sun = 4


class Power(enum.Enum):
	''' Мощь карты '''

	two = 2
	tree = 3
	four = 4
	five = 5
	six = 6
	seven = 7
	eight = 8
	nine = 9
	ten = 10
	admiral_1 = 10.001
	admiral_2 = 10.002
	admiral_3 = 10.003
	general = 11


@dataclass
class Card:
	suit: Suit
	power: Power
	crit: bool=False

	def __str__(self):
		return f'[{self.suit}] {self.power}'


def gen_cards() -> List[Card]:
	''' Сгенерировать карты '''

	cards: List[Card] = []

	for suit in Suit:
		for power in Power:
			card = Card(suit=suit, power=power)
			cards.append(card)

	return cards