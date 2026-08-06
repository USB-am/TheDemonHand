import random

from src.card import Card
from src.combos import get_combo, Combo


class HandOverflowError(Exception):
    ''' Ошибка переполнения руки '''


class DeckCards:
    def __init__(self, all_cards: list[Card]):
        self.all_cards = all_cards
        self.remaining_cards: list[Card] = []

    def get_card(self) -> Card:
        if not len(self.remaining_cards):
            self.remaining_cards = random.sample(self.all_cards, len(self.all_cards))

        return self.remaining_cards.pop()

    def get_card_by_id(self, card_id: str) -> Card:
        for card in self.all_cards:
            if card.id == card_id:
                return card


class HandManager:
    def __init__(self):
        self.cards: list[Card] = []
        self._selected_cards: list[Card] = []

    def select_card(self, cards: list[Card]) -> None:
        self._selected_cards = cards

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
