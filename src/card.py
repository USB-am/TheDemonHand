import os
from pathlib import Path
from enum import Enum
from dataclasses import dataclass, asdict


class Rank(Enum):
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
    id: str
    value: Rank
    suit: Suit
    face_path: Path = None

    def asdict(self) -> dict:
        return asdict(self)

    def __str__(self):
        return f'<Card {self.value.value} {self.suit.value}>'


def gen_all_card_variants() -> list[Card]:
    card_assets_dir = os.path.join('assets', 'cards')
    assets_path = {
        card_rank.name: os.path.join(card_assets_dir, f'{card_rank.name}.png')
        for card_rank in Rank
    }
    output: list[Card] = []

    for suit in Suit:
        for rank in Rank:
            output.append(Card(
                id=f'{suit.name}-{rank.name}',
                value=rank.value,
                suit=suit.value,
                face_path=assets_path[rank.name]
            ))

    return output
