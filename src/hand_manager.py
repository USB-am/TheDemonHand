from src.card import Card, Suit
from src.combos import get_combo, Combo


class DeckCards:
    def __init__(self):
        self.all_cards: list[Card] = []
        self.remaining_cards: list[Card] = []

    def get_card(self) -> Card:
        if not len(self.remaining_cards):
            self.remaining_cards = self.all_cards.copy()

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

    def discard_card(self) -> None:
        for card in self._selected_cards:
            self._selected_cards.remove(card)
