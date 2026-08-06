import pytest

from src.card import Card, Suit
from src.combos import (get_combo, DemonHandCombo, MarchingHordeCombo,
                        TetradCombo, GrandWarhostCombo, HordeCombo, MarchCombo,
                        TriadCombo, DyadSetCombo, DyadCombo, SoloCombo)


def card(value, suit):
    return Card(
        id=f'{value}-{suit}',
        value=value,
        suit=Suit[suit.value.upper()],
        face_path=''
    )


def make_cards(values, suits):
    return [card(v, s) for v, s in zip(values, suits)]


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


COMBO_CARDS_TEST_CASES = [
    (make_cards([10]*5, [Suit.SUN]*5), DemonHandCombo, make_cards([10]*5, [Suit.SUN]*5)),
    (make_cards([2, 3, 4, 5, 6], [Suit.SUN]*5), MarchingHordeCombo, make_cards([2, 3, 4, 5, 6], [Suit.SUN]*5)),
    (make_cards([5, 5, 5, 5, 7], [Suit.SUN]*5), TetradCombo, make_cards([5, 5, 5, 5], [Suit.SUN]*4)),
    (make_cards([2, 5, 5, 5, 5], [Suit.SUN]*5), TetradCombo, make_cards([5, 5, 5, 5], [Suit.SUN]*4)),
    (make_cards([3, 3, 3, 7, 7], [Suit.SUN]*5), GrandWarhostCombo, make_cards([3, 3, 3, 7, 7], [Suit.SUN]*5)),
    (make_cards([2, 4, 6, 8, 7], [Suit.SUN]*5), HordeCombo, make_cards([2, 4, 6, 8, 7], [Suit.SUN]*5)),
    (make_cards([2, 3, 4, 5, 6], [Suit.SUN, Suit.FIRE, Suit.MOON, Suit.SUN, Suit.STONE]), MarchCombo, make_cards([2, 3, 4, 5, 6], [Suit.SUN, Suit.FIRE, Suit.MOON, Suit.SUN, Suit.STONE])),
    (make_cards([5, 7, 5, 5, 6], [Suit.SUN]*5), TriadCombo, make_cards([5, 5, 5], [Suit.SUN]*3)),
    (make_cards([2, 4, 5, 2, 5], [Suit.SUN]*5), DyadSetCombo, make_cards([2, 2, 5, 5], [Suit.SUN]*4)),
    (make_cards([2, 3, 7, 8, 2], [Suit.SUN]*5), DyadCombo, make_cards([2, 2], [Suit.SUN]*2)),
    (make_cards([2, 9, 5, 4, 7], [Suit.SUN]*5), SoloCombo, make_cards([9], [Suit.SUN])[0]),
]

@pytest.mark.parametrize("cards, combo, expected", COMBO_CARDS_TEST_CASES)
def test_get_combo_cards(cards, combo, expected):
    result = combo.get_combo_cards(cards)
    assert result == expected
