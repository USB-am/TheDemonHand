import unittest

import cards as Card
import combos as Combo


class TestIsCombo(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.all_cards = Card.gen_cards()

	def test_duo(self):
		duo_cards = list(filter(
			lambda c: c.power==Card.Power.general,
			self.all_cards))[:2]
		combo = self.all_cards[:3] + duo_cards

		self.assertTrue(Combo.is_duo(combo))
		self.assertFalse(Combo.is_duo(self.all_cards[:5]))

	def test_double_duo(self):
		duo_cards_1 = [
			Card.Card(power=Card.Power.two, suit=Card.Suit.moon),
			Card.Card(power=Card.Power.two, suit=Card.Suit.stone)
		]
		duo_cards_2 = [
			Card.Card(power=Card.Power.six, suit=Card.Suit.fire),
			Card.Card(power=Card.Power.six, suit=Card.Suit.sun),
		]

		self.assertTrue(Combo.is_double_duo(duo_cards_1 + duo_cards_2))
		self.assertTrue(Combo.is_double_duo(duo_cards_1 + [self.all_cards[1]] + duo_cards_2))
		self.assertFalse(Combo.is_double_duo(duo_cards_1 + self.all_cards[:3]))
		self.assertFalse(Combo.is_double_duo(duo_cards_2 + self.all_cards[:3]))

	def test_trio(self):
		trio_cards = list(filter(
			lambda c: c.power==Card.Power.general,
			self.all_cards))[:3]
		combo = self.all_cards[:2] + trio_cards

		self.assertTrue(Combo.is_trio(combo))
		self.assertFalse(Combo.is_trio(self.all_cards[:5]))

	def test_quartet(self):
		quartet_cards = list(filter(
			lambda c: c.power==Card.Power.general,
			self.all_cards))[:4]
		combo = [self.all_cards[0]] + quartet_cards

		self.assertTrue(Combo.is_quartet(combo))
		self.assertFalse(Combo.is_quartet(self.all_cards[:5]))

	def test_great_squad(self):
		trio_cards = list(filter(
			lambda c: c.power==Card.Power.general,
			self.all_cards))[:3]
		duo_cards = list(filter(
			lambda c: c.power==Card.Power.admiral_1,
			self.all_cards))[:2]
		combo_1 = trio_cards + duo_cards
		combo_2 = duo_cards + trio_cards
		combo_3 = [duo_cards[0]] + trio_cards + [duo_cards[1]]

		self.assertTrue(Combo.is_great_squad(combo_1))
		self.assertTrue(Combo.is_great_squad(combo_2))
		self.assertFalse(Combo.is_great_squad(self.all_cards[:5]))

	def test_march(self):
		march_cards = self.all_cards[:5]
		no_march_cards = self.all_cards[:5:2]

		self.assertTrue(Combo.is_march(march_cards))
		self.assertFalse(Combo.is_march(no_march_cards))

	def test_is_combo(self):
		get_cards_by_power = lambda cards_count: list(filter(
			lambda c: c.power==Card.Power.two,
			self.all_cards))[:cards_count]
		combo_1 = self.all_cards[:5]	# True
		combo_2 = get_cards_by_power(3)	# True
		combo_3 = get_cards_by_power(2)	# True
		combo_4 = self.all_cards[:5:3]	# False
		combo_5 = self.all_cards[:2]	# False
		combo_6 = [self.all_cards[0]]	# False

		self.assertTrue(Combo.is_combo(combo_1))
		self.assertTrue(Combo.is_combo(combo_2))
		self.assertTrue(Combo.is_combo(combo_3))
		self.assertFalse(Combo.is_combo(combo_4))
		self.assertFalse(Combo.is_combo(combo_5))
		self.assertFalse(Combo.is_combo(combo_6))


class TestGetCombo(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.all_cards = Card.gen_cards()

	def _sorted_by_power(self, cards):
		return sorted(cards, key=lambda c: c.power.value)

	def test_get_duo(self):
		duo_cards = [
			Card.Card(power=Card.Power.two, suit=Card.Suit.stone),
			Card.Card(power=Card.Power.two, suit=Card.Suit.moon)]
		combo_1 = [duo_cards[0]] + self.all_cards[10:13] + [duo_cards[1]]
		combo_2 = duo_cards + self.all_cards[10:13]
		combo_3 = [self.all_cards[10]] + duo_cards

		self.assertEqual(duo_cards, Combo.get_duo_cards(combo_1))
		self.assertEqual(duo_cards, Combo.get_duo_cards(combo_2))
		self.assertEqual(duo_cards, Combo.get_duo_cards(combo_3))
		self.assertEqual(duo_cards, Combo.get_duo_cards(duo_cards))
		self.assertIsNone(Combo.get_duo_cards(self.all_cards[:5]))
		self.assertIsNone(Combo.get_duo_cards(self.all_cards[:2]))

	def test_get_horde(self):
		combo_1 = list(filter(
			lambda c: c.suit==Card.Suit.stone,
			self.all_cards))[:5]
		combo_2 = list(filter(
			lambda c: c.suit==Card.Suit.stone,
			self.all_cards))[:10:2]
		combo_3 = self.all_cards[:5:10]

		self.assertEqual(combo_1, Combo.get_horde_cards(combo_1))
		self.assertEqual(combo_2, Combo.get_horde_cards(combo_2))
		self.assertIsNone(Combo.get_horde_cards(combo_3))

	def test_get_double_duo(self):
		combo_1 = [
			Card.Card(power=Card.Power.two, suit=Card.Suit.stone),
			Card.Card(power=Card.Power.six, suit=Card.Suit.stone),
			Card.Card(power=Card.Power.two, suit=Card.Suit.moon),
			Card.Card(power=Card.Power.six, suit=Card.Suit.moon),
		]
		sorted_combo = self._sorted_by_power(combo_1)
		output_1 = self._sorted_by_power(Combo.get_double_duo_cards(combo_1))
		output_2 = self._sorted_by_power(Combo.get_double_duo_cards(combo_1 + [self.all_cards[-1]]))

		self.assertEqual(sorted_combo, output_1)
		self.assertEqual(sorted_combo, output_2)
		self.assertIsNone(Combo.get_double_duo_cards(self.all_cards[:5]))

	def test_get_trio(self):
		combo_1 = [
			Card.Card(power=Card.Power.two, suit=Card.Suit.stone),
			Card.Card(power=Card.Power.two, suit=Card.Suit.fire),
			Card.Card(power=Card.Power.two, suit=Card.Suit.sun),
		]
		sorted_combo = self._sorted_by_power(combo_1)
		output_1 = self._sorted_by_power(Combo.get_trio_cards(combo_1))
		output_2 = self._sorted_by_power(Combo.get_trio_cards(combo_1 + self.all_cards[:-2:-1]))

		self.assertEqual(sorted_combo, output_1)
		self.assertEqual(sorted_combo, output_2)
		self.assertIsNone(Combo.get_trio_cards(self.all_cards[:5]))

	def test_get_quertet(self):
		combo_1 = [
			Card.Card(power=Card.Power.two, suit=Card.Suit.stone),
			Card.Card(power=Card.Power.two, suit=Card.Suit.moon),
			Card.Card(power=Card.Power.two, suit=Card.Suit.fire),
			Card.Card(power=Card.Power.two, suit=Card.Suit.sun),
		]
		sorted_combo = self._sorted_by_power(combo_1)
		output_1 = self._sorted_by_power(Combo.get_quertet_cards(combo_1))
		output_2 = self._sorted_by_power(Combo.get_quertet_cards(combo_1 + [self.all_cards[-1]]))

		self.assertEqual(sorted_combo, output_1)
		self.assertEqual(sorted_combo, output_2)
		self.assertIsNone(Combo.get_quertet_cards(self.all_cards[:5]))

	def test_get_great_squad(self):
		combo_1 = [
			Card.Card(power=Card.Power.two, suit=Card.Suit.stone),
			Card.Card(power=Card.Power.two, suit=Card.Suit.moon),
			Card.Card(power=Card.Power.two, suit=Card.Suit.fire),
			Card.Card(power=Card.Power.six, suit=Card.Suit.moon),
			Card.Card(power=Card.Power.six, suit=Card.Suit.fire),
		]
		sorted_combo = self._sorted_by_power(combo_1)
		output_1 = self._sorted_by_power(Combo.get_great_squad_cards(combo_1))

		self.assertEqual(sorted_combo, output_1)
		self.assertIsNone(Combo.get_great_squad_cards(self.all_cards[:5]))

	def test_get_march(self):
		combo_1 = [
			Card.Card(power=Card.Power.two, suit=Card.Suit.stone),
			Card.Card(power=Card.Power.tree, suit=Card.Suit.stone),
			Card.Card(power=Card.Power.four, suit=Card.Suit.moon),
			Card.Card(power=Card.Power.five, suit=Card.Suit.fire),
			Card.Card(power=Card.Power.six, suit=Card.Suit.sun),
		]
		combo_2 = [
			Card.Card(power=Card.Power.ten, suit=Card.Suit.sun),
			Card.Card(power=Card.Power.nine, suit=Card.Suit.sun),
			Card.Card(power=Card.Power.eight, suit=Card.Suit.sun),
			Card.Card(power=Card.Power.seven, suit=Card.Suit.sun),
			Card.Card(power=Card.Power.six, suit=Card.Suit.sun),
		]
		sorted_combo_1 = self._sorted_by_power(combo_1)
		sorted_combo_2 = self._sorted_by_power(combo_2)
		output_1 = self._sorted_by_power(Combo.get_march_cards(combo_1))
		output_2 = self._sorted_by_power(Combo.get_march_cards(combo_2))

		self.assertEqual(sorted_combo_1, output_1)
		self.assertEqual(sorted_combo_2, output_2)
		self.assertIsNone(Combo.get_march_cards(self.all_cards[:10:2]))

	def test_get_combo(self):
		combo_duo = [
			Card.Card(power=Card.Power.two, suit=Card.Suit.moon),
			Card.Card(power=Card.Power.two, suit=Card.Suit.stone),
		]
		self.assertIsInstance(Combo.get_combo(combo_duo), Combo.Duo)

		combo_double_duo = combo_duo + [
			Card.Card(power=Card.Power.tree, suit=Card.Suit.fire),
			Card.Card(power=Card.Power.tree, suit=Card.Suit.sun),
		]
		self.assertIsInstance(Combo.get_combo(combo_double_duo), Combo.DoubleDuo)

		combo_trio = combo_duo + [
			Card.Card(power=Card.Power.two, suit=Card.Suit.fire),
		]
		self.assertIsInstance(Combo.get_combo(combo_trio), Combo.Trio)

		combo_great_squad = combo_double_duo + [
			Card.Card(power=Card.Power.tree, suit=Card.Suit.stone)
		]
		self.assertIsInstance(Combo.get_combo(combo_great_squad), Combo.GreatSquad)

		combo_quartet = [
			Card.Card(power=Card.Power.two, suit=suit)
			for suit in Card.Suit
		]
		self.assertIsInstance(Combo.get_combo(combo_quartet), Combo.Quartet)

		combo_horde = self.all_cards[:5]
		self.assertIsInstance(Combo.get_combo(combo_horde), Combo.Horde)

		combo_march = [
			Card.Card(power=Card.Power.two, suit=Card.Suit.stone),
			Card.Card(power=Card.Power.tree, suit=Card.Suit.fire),
			Card.Card(power=Card.Power.four, suit=Card.Suit.fire),
			Card.Card(power=Card.Power.five, suit=Card.Suit.moon),
			Card.Card(power=Card.Power.six, suit=Card.Suit.sun),
		]
		self.assertIsInstance(Combo.get_combo(combo_march), Combo.March)
