from typing import List


def calc_health(player: 'Player', percent: float) -> int:
	''' Рассчитать количество восстанавливаемого здоровья '''

	missing_hp = player.max_hp - player.hp
	return int(missing_hp * percent)


class Player:
	def __init__(self, max_hp: int):
		self.max_hp: int = max_hp
		self.hp: int = hp

		self.runes: List['Rune'] = []
		self.money: int = 0

		self.crit_chance: int = 0

	def health(self, percent: float) -> None:
		''' Восстановить <percent> недостающего здоровья '''

		self.hp += calc_health(self, percent)
