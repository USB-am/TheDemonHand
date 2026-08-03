from enum import Enum
from dataclasses import dataclass


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