from typing import List

from combos import Combo
from runes import Rune


def calc(combo: Combo, runes: List[Rune]) -> int:
	result = combo.power

	for card in combo.cards:
		result += int(card.power.value)

	resuult += int(combo.power)

	for rune in runes:
		result += rune(combo.cards)

	return result
