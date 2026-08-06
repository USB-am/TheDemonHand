# -*- coding: utf-8 -*-

import eel

from src.session import Session
from src.combos import get_combo


eel.init('src/web')

session = Session()


@eel.expose
def take_card() -> dict:
    card = session.deck.get_card()
    return card.asdict()


@eel.expose
def update_selected_cards(card_ids) -> None:
    cards = [session.deck.get_card_by_id(card_id) for card_id in card_ids]
    session.hand.select_card(cards)


@eel.expose
def get_combo_damage() -> dict:
    combo = get_combo(session.hand._selected_cards)
    if combo is None:
        return {'title': '',
                'damage': ''}
    return {'title': combo.title,
            'damage': combo.damage}


if __name__ == '__main__':
    eel.start("index.html", mode='firefox', size=(400, 300))
