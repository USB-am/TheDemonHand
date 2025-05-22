# -*- coding: utf-8 -*-

import random
from typing import List, Generator

import cards as Card
import combos as Combo
from ui import run_ui


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


class Table:
	def __init__(self):
		self.hand: List[Card.Card] = []
		self.runes: List[Rune] = []


if __name__ == '__main__':
	# all_cards = Card.gen_cards()
	# runes = [StoneDamageRune(),]

	# bison = Bison()

	# cards = [
	# 	Card.Card(suit=Card.Suit.stone, power=Card.Power.general),
	# 	Card.Card(suit=Card.Suit.fire, power=Card.Power.general),
	# 	Card.Card(suit=Card.Suit.moon, power=Card.Power.general),
	# 	Card.Card(suit=Card.Suit.sun, power=Card.Power.general),
	# ]
	# combo = Combo.get_combo(cards)
	# damage = calc(combo, runes)
	# print(f'Bison.hp = {bison.hp}')
	# print(f'Damage = {damage}')
	# bison.hp -= damage
	# print(f'Bison.hp = {bison.hp}')

	run_ui()
