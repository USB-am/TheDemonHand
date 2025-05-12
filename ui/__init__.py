from typing import List, Dict

import eel

from combos import get_combo
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

	return {'title': combo.title, 'power': combo.power}


def run_ui():
	eel.start('templates/index.html',
		      jinja_templates='templates')
