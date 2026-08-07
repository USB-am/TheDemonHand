from src.hand_manager import DeckCards, HandManager
from src.card import gen_all_card_variants
from src.enemy import Bison


class Session:
    def __init__(self):
        self.deck = DeckCards(gen_all_card_variants())
        self.hand = HandManager()
        self.enemy = Bison()
