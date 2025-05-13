from typing import List, Dict
from json import dumps

import eel

from combos import get_combo, Empty
from cards import Power, Suit, Card


eel.init('ui/web')


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

	return {
		'img': '../img/cards/10.png',
		'power': '10',
		'suit': 'sun',
	}


def run_ui():
	eel.start('templates/index.html',
		      jinja_templates='templates')
