import os


class Enemy:
    def __init__(self):
        self.hp = self.max_hp


class Bison(Enemy):
    name = 'Бизон'
    max_hp = 250
    base_damage = 6
    crit_chance = 0.0
    image = os.path.join('assets', 'enemy', 'bison.png')

    def attack(self) -> int:
        return self.base_damage

    def take_damage(self, damage: int) -> None:
        self.hp -= damage

    def __str__(self):
        return f'<{self.name} [{self.hp}/{self.max_hp}]>'
