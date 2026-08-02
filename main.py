# -*- coding: utf-8 -*-

from enum import Enum
from collections import Counter
from dataclasses import dataclass

# import eel


# eel.init('web')

# @eel.expose
# def get_hello_message(name):
#     return f"Hello {name} from Python!"

# eel.start("index.html", size=(400, 300))


class Suit(Enum):
    SUN = 'sun'
    FIRE = 'fire'
    MOON = 'moon'
    STONE = 'stone'


@dataclass
class Card:
    value: int
    suit: Suit

    def __str__(self):
        return f'<Card {self.value} {self.suit.value}>'


class Combo:
    pass


class DemonHandCombo(Combo):
    ''' 5 карт одинакового ранга одной масти '''
    damage = 2000
    title = 'Рука демона'

    def is_combo(self, cards: list[Card]) -> bool:
        is_suit_equals = len(set(map(lambda card: card.suit, cards))) == 1
        is_value_equals = sum(map(lambda card: card.value, cards)) == 50
        return is_suit_equals and is_value_equals


class MarchingHordeCombo(Combo):
    ''' 5 карт с последовательным рангом одной масти '''
    damage = 600
    title = 'Марширующая Орда'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        is_suit_equals = len(set(map(lambda card: card.suit, cards))) == 1

        card_values = map(lambda card: card.value, cards)
        is_filtered = sorted(card_values) == range(min(card_values), max(card_values))
        return is_suit_equals and is_filtered


class TetradCombo(Combo):
    ''' 4 карты одного ранга '''
    damage = 400
    title = 'Тетрада'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        card_rank = cards[0].value
        for card in cards:
            if card.value != card_rank:
                return False
        return True


class Triad(Combo):
    ''' 3 карты одного ранга '''
    damage = 80
    title = 'Триада'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        values_counts = Counter(card.value for card in cards)
        pairs_count = sum(1 for count in values_counts.values() if count == 3)
        return pairs_count == 1


class DyadSetCombo(Combo):
    ''' 2 пары по 2 карты одного ранга '''
    damage = 40
    title = 'Набор диад'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        values_counts = Counter(card.value for card in cards)
        pairs_count = sum(1 for count in values_counts.values() if count == 2)
        return pairs_count == 2


class DyadCombo(Combo):
    ''' 2 карты одного ранга '''
    damage = 20
    title = 'Диада'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        values_counts = Counter(card.value for card in cards)
        pairs_count = sum(1 for count in values_counts.values() if count == 2)
        return pairs_count == 1


class SoloCombo(Combo):
    ''' карта с наивысшим рангом '''
    damage = 10
    title = 'Соло'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        return len(cards) >= 1


def get_combo(cards: list[Card]) -> Combo:
    return Combo()


def main():
    c1 = Card(1, Suit.STONE)
    c2 = Card(2, Suit.MOON)
    c3 = Card(3, Suit.FIRE)
    c4 = Card(4, Suit.SUN)
    print(c1, c2, c3, c4, sep='\n')


if __name__ == '__main__':
    main()
