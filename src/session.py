from src.hand_manager import DeckCards, HandManager
from src.card import gen_all_card_variants


class Session:
    def __init__(self):
        self.deck = DeckCards(gen_all_card_variants())
        self.hand = HandManager()
