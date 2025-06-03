from typing import List, Dict
from json import dumps

import eel

from combos import get_combo, Empty, Solo
from cards import Power, Suit, Card
from deck import Deck


eel.init('ui/web')
DECK = Deck()


def card_dict_to_obj(card: Dict) -> Card:
	''' Конвертивароть список с данными о карте в объект карты '''

	power = Power[card['power']]
	suit = Suit[card['suit']]

	return Card(suit=suit, power=power)


def get_card() -> Card:
	''' Вытащить карту из колоды '''

	while True:
		card_drawer = DECK.get_card()
		for card in card_drawer:
			yield card


@eel.expose
def get_combo_title(cards: List[Dict]) -> str:
	''' Получить название комбо по картам '''

	card_objs = [card_dict_to_obj(card) for card in cards]
	combo = get_combo(card_objs)

	if isinstance(combo, Empty):
		return {'title': '', 'power': ''}

	return {'title': combo.title, 'power': combo.power}


@eel.expose
def draw_card_from_deck() -> Dict:
	''' Вытащить карту из колоды '''

	next_card = next(get_card())

	return {
		'img': f'../img/cards/{next_card.power.value}.png',
		'power': next_card.power.name,
		'power-value': next_card.power.value,
		'suit': next_card.suit.name,
		'suit-img': f'../img/suit/{next_card.suit.name}.png',
	}


@eel.expose
def calc_attack_damage(cards: List[Dict]) -> int:
	''' Рассчитать силу атаки с комбо '''

	card_objs = [card_dict_to_obj(card) for card in cards]
	combo = get_combo(card_objs)
	damage = combo.power
	if isinstance(combo, Solo):
		damage += max(card_objs, key=lambda c: c.power.value).power.value
	else:
		damage += sum([card_dict_to_obj(card).power.value for card in cards])

	return damage


def run_ui():
	eel.start('templates/index.html',
		      jinja_templates='templates')
