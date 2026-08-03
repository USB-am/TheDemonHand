import pytest

from src.card import Card, Suit
from src.combos import get_combo, SoloCombo


class TestSoloCombo:
    def test_solo_positive(self):
        c1 = Card(1, Suit.SUN)
        c2 = Card(2, Suit.FIRE)
        c3 = Card(3, Suit.MOON)
        c4 = Card(4, Suit.STONE)
        c5 = Card(6, Suit.STONE)

        assert get_combo([c1,]) == SoloCombo
        assert get_combo([c1, c2]) == SoloCombo
        assert get_combo([c1, c2, c3]) == SoloCombo
        assert get_combo([c1, c2, c3, c4]) == SoloCombo
        assert get_combo([c1, c2, c3, c4, c5]) == SoloCombo

    def test_solo_negative(self):
        finded_combo = SoloCombo

        assert get_combo([])
