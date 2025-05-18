from typing import List, Dict
from json import dumps

import eel

from combos import get_combo, Empty
from cards import Power, Suit, Card
from deck import Deck


eel.init('ui/web')
DECK = Deck()


def get_card() -> Card:
	''' Вытащить карту из колоды '''

	while True:
		card_drawer = DECK.get_card()
		for card in card_drawer:
			yield card


@eel.expose
def get_combo_title(cards: List[Dict]) -> str:
	''' Получить название комбо по картам '''

	card_objs: List[Card] = []

	for card in cards:
		power = Power[card['power']]
		suit = Suit[card['suit']]
		card_objs.append(Card(
			power=power,
			suit=suit
		))

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
		'suit': next_card.suit.name,
	}


def run_ui():
	eel.start('templates/index.html',
		      jinja_templates='templates')
