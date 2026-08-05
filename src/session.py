from src.hand_manager import DeckCards, HandManager


class Session:
    def __init__(self):
        self.deck = DeckCards()
        self.hand = HandManager()
