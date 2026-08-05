import random

from src.card import Card
from src.combos import get_combo, Combo


class HandOverflowError(Exception):
    ''' Ошибка переполнения руки '''


class DeckCards:
    def __init__(self):
        self.all_cards: list[Card] = []
        self.remaining_cards: list[Card] = []

    def get_card(self) -> Card:
        if not len(self.remaining_cards):
            self.remaining_cards = random.sample(self.all_cards, len(self.all_cards))

        return self.remaining_cards.pop()


class HandManager:
    def __init__(self):
        self.cards: list[Card] = []
        self._selected_cards: list[Card] = []

    def select_card(self, card: Card) -> None:
        if card in self._selected_cards:
            self._selected_cards.remove(card)
        else:
            self._selected_cards.append(card)

    @property
    def selected_combo(self) -> Combo:
        return get_combo(self._selected_cards)

    def take_card(self, card: Card) -> None:
        if len(self.cards) > 8:
            raise HandOverflowError(f'Hand has 8 cards and con\'t take new!')
        self.cards.append(card)

    def discard_card(self) -> None:
        for card in self._selected_cards:
            self._selected_cards.remove(card)
            self.cards.remove(card)
