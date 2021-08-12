import unittest
from wargame.card import ranks, values, Card

class GlobalValues(unittest.TestCase):
    def test_ranks(self):
        self.assertEqual(len(ranks), 13)

    def test_values(self):
        counter = 0
        for rank in ranks:
            self.assertEqual(values[rank], counter)
            counter += 1

class Constructor(unittest.TestCase):
    def test_card_ctor_throws_value_error(self):
        with self.assertRaises(ValueError):
            Card('zero')

    def test_card_ctor_throws_type_error(self):
        with self.assertRaises(TypeError):
            Card(1)

    def test_card_ctor(self):
        for rank in ranks:
            self.assertEqual(Card(rank).value, values[rank])

class Operators(unittest.TestCase):
    def test_eq(self):
        first_card = Card(ranks[0])
        second_card = Card(ranks[0])

        self.assertEqual(first_card, second_card)

    def test_neq(self):
        first_card = Card(ranks[0])
        second_card = Card(ranks[1])

        self.assertNotEqual(first_card, second_card)
