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

    @staticmethod
    def get_combo_cards(cards: list[Card]) -> list[Card] | None:
        if not SoloCombo.is_combo(cards):
            return None

        return sorted(cards, key=lambda c: c.value)[-1]


class DyadCombo(Combo):
    ''' 2 карты одного ранга '''
    damage = 20
    title = 'Диада'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        values_counts = Counter(card.value for card in cards)
        pairs_count = sum(1 for count in values_counts.values() if count == 2)
        return pairs_count == 1

    @staticmethod
    def get_combo_cards(cards: list[Card]) -> list[Card] | None:
        if not DyadCombo.is_combo(cards):
            return None
        values_counts = Counter(card.value for card in cards)
        for value, count in values_counts.items():
            if count == 2:
                return list(filter(lambda c: c.value==value, cards))


class DyadSetCombo(Combo):
    ''' 2 пары по 2 карты одного ранга '''
    damage = 40
    title = 'Набор диад'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        values_counts = Counter(card.value for card in cards)
        pairs_count = sum(1 for count in values_counts.values() if count == 2)
        return pairs_count == 2

    @staticmethod
    def get_combo_cards(cards: list[Card]) -> list[Card] | None:
        if not DyadSetCombo.is_combo(cards):
            return None

        output: list[Card] = []
        values_counts = Counter(card.value for card in cards)
        for value, count in values_counts.items():
            if count == 2:
                dyad_cards = list(filter(lambda c: c.value==value, cards))
                output.extend(dyad_cards)
        return output


class TriadCombo(Combo):
    ''' 3 карты одного ранга '''
    damage = 80
    title = 'Триада'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        values_counts = Counter(card.value for card in cards)
        pairs_count = sum(1 for count in values_counts.values() if count == 3)
        return pairs_count == 1
    
    @staticmethod
    def get_combo_cards(cards: list[Card]) -> list[Card] | None:
        if not TriadCombo.is_combo(cards):
            return None
        values_counts = Counter(card.value for card in cards)
        for value, count in values_counts.items():
            if count == 3:
                return list(filter(lambda c: c.value==value, cards))


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

    @staticmethod
    def get_combo_cards(cards: list[Card]) -> list[Card] | None:
        if not MarchCombo.is_combo(cards):
            return None
        return cards


class HordeCombo(Combo):
    ''' 5 карт с одинаковой мастью '''
    damage = 125
    title = 'Орда'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        if len(cards) < 5:
            return False

        return len({card.suit for card in cards}) == 1

    @staticmethod
    def get_combo_cards(cards: list[Card]) -> list[Card] | None:
        if not HordeCombo.is_combo(cards):
            return None
        return cards


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

    @staticmethod
    def get_combo_cards(cards: list[Card]) -> list[Card] | None:
        if not GrandWarhostCombo.is_combo(cards):
            return None
        return cards


class TetradCombo(Combo):
    ''' 4 карты одного ранга '''
    damage = 400
    title = 'Тетрада'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        counts = Counter(card.value for card in cards)
        return 4 in counts.values()

    @staticmethod
    def get_combo_cards(cards: list[Card]) -> list[Card] | None:
        if not TetradCombo.is_combo(cards):
            return None

        sorted_cards = sorted(cards, key=lambda c: c.value)
        if TetradCombo.is_combo(sorted_cards[:-1]):
            return sorted_cards[:-1]
        return sorted_cards[1:]


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

    @staticmethod
    def get_combo_cards(cards: list[Card]) -> list[Card] | None:
        if not MarchingHordeCombo.is_combo(cards):
            return None
        return cards


class DemonHandCombo(Combo):
    ''' 5 карт одинакового ранга одной масти '''
    damage = 2000
    title = 'Рука демона'

    @staticmethod
    def is_combo(cards: list[Card]) -> bool:
        if len(cards) < 5:
            return False

        is_suit_equals = len(set(map(lambda card: card.suit, cards))) == 1
        is_value_equals = sum(map(lambda card: card.value, cards)) == 50
        return is_suit_equals and is_value_equals

    @staticmethod
    def get_combo_cards(cards: list[Card]) -> list[Card] | None:
        if not DemonHandCombo.is_combo(cards):
            return None
        return cards


COMBO_PRIORITY = (
    DemonHandCombo,
    MarchingHordeCombo,
    TetradCombo,
    GrandWarhostCombo,
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


def calculate_combo_damage(cards: list[Card]) -> int:
    combo = get_combo(cards)
    combo_cards = combo.get_combo_cards(cards)
    return combo.damage + sum(map(lambda c: c.value, combo_cards))
