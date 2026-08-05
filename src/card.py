from enum import Enum
from dataclasses import dataclass


class CardRank(Enum):
    two = 2
    tree = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    command_1 = 10
    command_2 = 10
    command_3 = 10
    prime_0 = 10


class Suit(Enum):
    SUN = 'sun'
    FIRE = 'fire'
    MOON = 'moon'
    STONE = 'stone'


@dataclass
class Card:
    value: CardRank
    suit: Suit

    def __str__(self):
        return f'<Card {self.value.value} {self.suit.value}>'


def gen_all_card_variants() -> list[Card]:
    output: list[Card] = []

    for suit in Suit:
        for rank in CardRank:
            output.append(Card(
                value=rank,
                suit=suit
            ))

    return output
