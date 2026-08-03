from collections import Counter

from src.card import Card


class Combo:
    pass


class SoloCombo(Combo):
    ''' карта с наивысшим рангом '''
    damage = 10
    title = 'Соло'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        return len(cards) >= 1


class DyadCombo(Combo):
    ''' 2 карты одного ранга '''
    damage = 20
    title = 'Диада'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        values_counts = Counter(card.value for card in cards)
        pairs_count = sum(1 for count in values_counts.values() if count == 2)
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
    

class TriadCombo(Combo):
    ''' 3 карты одного ранга '''
    damage = 80
    title = 'Триада'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        values_counts = Counter(card.value for card in cards)
        pairs_count = sum(1 for count in values_counts.values() if count == 3)
        return pairs_count == 1


class MarchCombo(Combo):
    ''' 5 карт с последовательным рангом и любой масти '''
    damage = 100
    title = 'Марш'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        if len(cards) < 5:
            return False

        card_values = list(map(lambda card: card.value, cards))
        is_sorted = sorted(card_values) == list(range(min(card_values), max(card_values) + 1))
        return is_sorted


class HordeCombo(Combo):
    ''' 5 карт с одинаковой мастью '''
    damage = 125
    title = 'Орда'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        if len(cards) < 5:
            return False

        return len({card.suit for card in cards}) == 1


class GrandWarhostCombo(Combo):
    ''' Комбинация из Dyad и Triad комбинаций '''
    damage = 175
    title = 'Великий отряд'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        if len(cards) < 5:
            return False

        counts = Counter(card.value for card in cards)
        return len(counts) == 2 and list(counts.values())[0] in (2, 3)


class TetradCombo(Combo):
    ''' 4 карты одного ранга '''
    damage = 400
    title = 'Тетрада'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        counts = Counter(card.value for card in cards)
        return 4 in counts.values()


class MarchingHordeCombo(Combo):
    ''' 5 карт с последовательным рангом одной масти '''
    damage = 600
    title = 'Марширующая Орда'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        if len(cards) < 5:
            return False

        is_suit_equals = len(set(map(lambda card: card.suit, cards))) == 1
        card_values = list(map(lambda card: card.value, cards))
        is_sorted = sorted(card_values) == list(range(min(card_values), max(card_values) + 1))
        return is_suit_equals and is_sorted


class DemonHandCombo(Combo):
    ''' 5 карт одинакового ранга одной масти '''
    damage = 2000
    title = 'Рука демона'

    def is_combo(self, cards: list[Card]) -> bool:
        if len(cards) < 5:
            return False

        is_suit_equals = len(set(map(lambda card: card.suit, cards))) == 1
        is_value_equals = sum(map(lambda card: card.value, cards)) == 50
        return is_suit_equals and is_value_equals


COMBO_PRIORITY = (
    MarchingHordeCombo,
    TetradCombo,
    HordeCombo,
    MarchCombo,
    TriadCombo,
    DyadSetCombo,
    DyadCombo,
    SoloCombo
)


def get_combo(cards: list[Card]) -> Combo:
    for combo in COMBO_PRIORITY:
        if combo.is_combo(cards):
            return combo
