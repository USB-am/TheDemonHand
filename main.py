# -*- coding: utf-8 -*-

import random
from typing import List, Generator

import cards as Card
import combos as Combo


class Rune:
	def __call__(self, combo: List[Card.Card]) -> int:
		return 0


class StoneDamageRune(Rune):
	def __call__(self, combo: List[Card.Card]) -> int:
		damage = 0
		for card in combo:
			if card.suit == Card.Suit.stone:
				damage += 10

		return damage


class Enemy:
	def attack(self) -> int:
		return self.damage

	@property
	def hp(self) -> int:
		return self._hp

	@hp.setter
	def hp(self, value: int) -> None:
		self._hp += value

		if self._hp > self.max_hp:
			self._hp = self.max_hp
		if self._hp <= 0:
			del self

	def __call__(self, combo: List[Card.Card]) -> None:
		pass

	def __del__(self):
		print(f'{self.name} is die!')


class Bison(Enemy):
	max_hp = 5000
	_hp = 5000
	name = 'Bison'
	damage = 8


class Deck:
	''' Колода карт '''

	def __init__(self):
		self.all_cards = gen_cards()
		self.now_cards = self.all_cards[:]

	def get_card(self) -> Generator:
		''' Достать карту из колоды '''

		shuffle_deck = random.shuffle(self.all_cards)	# Update
		for card in shuffle_deck:
			self.now_cards.remove(card)
			yield card

		self.now_cards = self.all_cards


class Table:
	def __init__(self):
		self.hand: List[Card.Card] = []
		self.runes: List[Rune] = []


def calc(combo: Combo.Combo, runes: List[Rune]) -> int:
	result = combo.power

	for card in combo.cards:
		result += int(card.power.value)

	for rune in runes:
		result += rune(combo.cards)

	return result


if __name__ == '__main__':
	all_cards = Card.gen_cards()
	runes = [StoneDamageRune(),]

	bison = Bison()

	cards = [
		Card.Card(suit=Card.Suit.stone, power=Card.Power.general),
		Card.Card(suit=Card.Suit.fire, power=Card.Power.general),
		Card.Card(suit=Card.Suit.moon, power=Card.Power.general),
		Card.Card(suit=Card.Suit.sun, power=Card.Power.general),
	]
	combo = Combo.get_combo(cards)
	damage = calc(combo, runes)
	print(f'Bison.hp = {bison.hp}')
	print(f'Damage = {damage}')
	bison.hp -= damage
	print(f'Bison.hp = {bison.hp}')
