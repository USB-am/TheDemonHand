# -*- coding: utf-8 -*-

# from src.card import Card, Suit
# from src.combos import get_combo

import eel


eel.init('src/web')

@eel.expose
def get_hello_message(name):
    return f"Hello {name} from Python!"

eel.start("index.html", mode='firefox', size=(400, 300))


# def main():
#     c1 = Card(1, Suit.STONE)
#     c2 = Card(2, Suit.MOON)
#     c3 = Card(3, Suit.FIRE)
#     c4 = Card(4, Suit.SUN)
#     combo = get_combo([c1, c2, c3, c4])
#     print(combo.title)


# if __name__ == '__main__':
#     main()
