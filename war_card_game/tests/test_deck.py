import unittest
from wargame.deck import Deck
from wargame.card import ranks, Card

class TestDeck(unittest.TestCase):
    def test_cards_in_default_deck(self):
        # Check that default deck has 4 cards of each rank
        deck = Deck()
        ranks_dict = {rank:4 for rank in ranks}

        for card in deck.cards:
            ranks_dict[card.rank] -= 1

        self.assertFalse(any(ranks_dict.values()))

    def test_ctor_from_cards_list(self):
        cards_list = [Card(rank) for rank in ranks]

        deck = Deck(cards_list)

        self.assertEqual(len(deck), len(ranks))

        # Check that initial list is not changed
        self.assertEqual(len(cards_list), len(ranks))

    def test_ctor_throws_exception(self):
        with self.assertRaises(TypeError):
            Deck(42)

    def test_splitted_in_half_decks(self):
        initial_deck = Deck()
        expected_size = len(initial_deck) // 2

        new_deck = initial_deck.split()

        self.assertEqual(len(initial_deck), expected_size)
        self.assertEqual(len(new_deck), expected_size)

    def test_splitted_single_card(self):
        single_card_deck = Deck([Card(ranks[0])])

        single_card_deck.split()

        self.assertEqual(len(single_card_deck), 1)

    def test_splitted_odd_deck(self):
        odd_deck = Deck([Card(rank) for rank in ranks])

        new_deck = odd_deck.split()

        self.assertEqual(len(odd_deck), len(ranks) // 2 + 1)
        self.assertEqual(len(new_deck), len(ranks) // 2)
