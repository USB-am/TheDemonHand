from typing import List
from dataclasses import dataclass

from cards import Card


def is_duo(cards: List[Card]) -> bool:
	''' Является ли комбо дуо '''

	if len(cards) < 2:
		return False

	sorted_cards = sorted(cards, key=lambda c: c.power.value)
	if sorted_cards[0].power == sorted_cards[1].power:
		return True

	return is_duo(sorted_cards[1:])

def get_duo_cards(cards: List[Card]) -> List[Card]:
	''' Получить из выбранных карт кобмо "Дуо" '''

	if not is_duo(cards):
		return

	sorted_cards = sorted(cards, key=lambda c: c.power.value)
	for card_ind in range(len(sorted_cards)-1):
		combo = sorted_cards[card_ind:card_ind+2]
		if is_duo(combo):
			return combo


def is_double_duo(cards: List[Card]) -> bool:
	''' Является ли кобмо двойным дуо '''

	if len(cards) < 4:
		return False

	sorted_cards = sorted(cards, key=lambda c: c.power.value)
	return is_duo(sorted_cards[:2]) and is_duo(sorted_cards[2:5]) or \
		is_duo(sorted_cards[:2]) and is_duo(sorted_cards[3:]) or \
		is_duo(sorted_cards[1:3]) and is_duo(sorted_cards[3:])

def get_double_duo_cards(cards: List[Card]) -> List[Card]:
	''' Получить из выбранных карт кобмо "Двойное дуо" '''

	if not is_double_duo(cards):
		return

	cards = cards.copy()
	duo_1 = get_duo_cards(cards)
	[cards.remove(card) for card in duo_1]
	duo_2 = get_duo_cards(cards)

	if None in (duo_1, duo_2):
		return
	return duo_1 + duo_2


def is_trio(cards: List[Card]) -> bool:
	''' Является ли комбо трио '''

	if len(cards) < 3:
		return False

	sorted_cards = sorted(cards, key=lambda c: c.power.value)
	if sorted_cards[0].power == sorted_cards[2].power:
		return True

	return is_trio(sorted_cards[1:])

def get_trio_cards(cards: List[Card]) -> List[Card]:
	''' Получить из выбранных карт кобмо "Трио" '''

	if not is_trio(cards):
		return

	sorted_cards = sorted(cards, key=lambda c: c.power.value)
	for i in range(3):
		combo = sorted_cards[i:i+3]
		if is_trio(combo):
			return combo


def is_quartet(cards: List[Card]) -> bool:
	''' Является ли комбо из 4 одинаковых карт '''

	if len(cards) < 4:
		return False

	sorted_cards = sorted(cards, key=lambda c: c.power.value)
	if sorted_cards[0].power == sorted_cards[3].power:
		return True

	return is_quartet(sorted_cards[1:])

def get_quertet_cards(cards: List[Card]) -> List[Card]:
	''' Получить из выбранных карт кобмо из 4 одинаковых карт '''

	if not is_quartet(cards):
		return

	sorted_cards = sorted(cards, key=lambda c: c.power.value)
	for i in range(2):
		combo = sorted_cards[i:i+4]
		if is_quartet(combo):
			return combo


def is_great_squad(cards: List[Card]) -> bool:
	''' Является ли комбо великим отрядом '''

	if len(cards) < 5:
		return False

	sorted_cards = sorted(cards, key=lambda c: c.power.value)
	if (is_trio(sorted_cards[:3]) and is_duo(sorted_cards[3:])) \
	or (is_duo(sorted_cards[:2]) and is_trio(sorted_cards[2:])):
		return True
	return False

def get_great_squad_cards(cards: List[Card]) -> List[Card]:
	''' Получить из выбранных карт комбо "Великий отряд" '''

	if not is_great_squad(cards):
		return

	cards = cards.copy()
	trio = get_trio_cards(cards)
	[cards.remove(card) for card in trio]
	duo = get_duo_cards(cards)

	if None in (trio, duo):
		return
	return trio + duo


def is_march(cards: List[Card]) -> bool:
	''' Является ли комбо маршем '''

	if len(cards) < 5:
		return False

	sorted_cards = sorted(cards, key=lambda c: c.power.value, reverse=True)
	for card_ind in range(4):
		if sorted_cards[card_ind].power.value - sorted_cards[card_ind+1].power.value == 1:
			continue
		return False
	return True

def get_march_cards(cards: List[Card]) -> List[Card]:
	''' Получить из выбранных карт кобмо "Марш" '''
	if is_march(cards): return cards


def is_horde(cards: List[Card]) -> bool:
	''' Является ли комбо ордой '''
	if len(cards) < 5: return False

	filtered_cards = tuple(filter(lambda c: c.suit==cards[0].suit, cards))
	return len(filtered_cards) == 5

def get_horde_cards(cards: List[Card]) -> List[Card]:
	''' Получить из выбранных карт кобмо "Орда" '''
	if is_horde(cards): return cards


def is_combo(cards: List[Card]) -> bool:
	''' Являются ли выбранные карты комбо '''

	return any((
		is_duo(cards),
		is_trio(cards),
		is_quartet(cards),
		is_great_squad(cards),
		is_march(cards),
		is_horde(cards)))


class Combo:
	def __init__(self, cards: List[Card]):
		self.cards = cards


class Solo(Combo):
	power = 0
	title = 'Одиночка'


class Duo(Combo):
	power = 20
	title = 'Пара'


class DoubleDuo(Combo):
	power = 40
	title = 'Две пары'


class Trio(Combo):
	power = 80
	title = 'Трио'


class March(Combo):
	power = 100
	title = 'Марш'


class Horde(Combo):
	power = 125
	title = 'Орда'


class GreatSquad(Combo):
	power = 175
	title = 'Великий отряд'


class Quartet(Combo):
	power = 400
	title = 'Квартет'


COMBO_PRIORITY = (
	(is_quartet, get_quertet_cards, Quartet),
	(is_great_squad, get_great_squad_cards, GreatSquad),
	(is_horde, get_horde_cards, Horde),
	(is_march, get_march_cards, March),
	(is_trio, get_trio_cards, Trio),
	(is_double_duo, get_double_duo_cards, DoubleDuo),
	(is_duo, get_duo_cards, Duo),
	(None, None, Solo),
)


def get_combo_cards(cards: List[Card]) -> List[Card]:
	''' Получить из выбранных карт лучшее комбо карт '''

	if not is_combo(cards):
		return max(cards, key=lambda c: c.power.value)

	for is_func, get_cards_func, _ in COMBO_PRIORITY:
		if is_func(cards):
			return get_cards_func(cards)


def get_combo(cards: List[Card]) -> Combo:
	''' Получить из выбранных карт лучшее кобмо '''

	if not is_combo(cards):
		max_card = max(cards, key=lambda c: c.power.value)
		return Solo([max_card,])

	for is_func, get_cards_func, combo_cls in COMBO_PRIORITY:
		if is_func(cards):
			return combo_cls(get_cards_func(cards))
