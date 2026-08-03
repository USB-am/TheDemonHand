import pytest

from src.card import Card, Suit
from src.combos import (get_combo, DemonHandCombo, MarchingHordeCombo,
                        TetradCombo, GrandWarhostCombo, HordeCombo, MarchCombo,
                        TriadCombo, DyadSetCombo, DyadCombo, SoloCombo)


def make_cards(values, suits):
    return [Card(v, s) for v, s in zip(values, suits)]


def card(value, suit):
    return Card(value, Suit[suit.upper()])


COMBO_TEST_CASES = [
    ([10,10,10,10,10], ['sun']*5, DemonHandCombo),
    ([1,2,3,4,5], ['fire']*5, MarchingHordeCombo),
    ([5,5,5,5,7], ['sun']*5, TetradCombo),
    ([3,3,3,7,7], ['sun']*5, GrandWarhostCombo),
    ([1,2,3,4,7], ['sun']*5, HordeCombo),
    ([1,2,3,4,5], ['sun','fire','moon','stone','sun'], MarchCombo),
    ([5,5,5,7,8], ['sun','fire','moon','stone','sun'], TriadCombo),
    ([5,5,7,7,8], ['sun','fire','moon','stone','sun'], DyadSetCombo),
    ([5,5,7,8,9], ['sun','fire','moon','stone','sun'], DyadCombo),
    ([1,2,3,4,6], ['sun','fire','moon','stone','sun'], SoloCombo),
]


@pytest.mark.parametrize("values, suits, expected", COMBO_TEST_CASES)
def test_combos(values, suits, expected):
    cards = make_cards(values, [Suit[s.upper()] for s in suits])
    result = get_combo(cards)
    assert result == expected
