# -*- coding: utf-8 -*-

import eel

from src.session import Session


eel.init('src/web')

session = Session()


@eel.expose
def get_hello_message(name):
    txt = f"Hello {name} from Python!"
    return txt


@eel.expose
def take_card() -> dict:
    card = session.deck.get_card()
    return card.asdict()
    # return {
    #     'value': card.value.value,
    #     'suit': card.suit.value
    # }


if __name__ == '__main__':
    eel.start("index.html", mode='firefox', size=(400, 300))
