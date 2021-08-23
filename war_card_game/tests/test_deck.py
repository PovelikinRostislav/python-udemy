import unittest
from wargame.deck import Deck
from wargame.card import ranks, Card

class Constructor(unittest.TestCase):
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

class Split(unittest.TestCase):
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

        # Odd deck receives more cards
        self.assertEqual(len(odd_deck), len(ranks) // 2 + 1)
        self.assertEqual(len(new_deck), len(ranks) // 2)

class Shuffle(unittest.TestCase):
    def test_if_default_deck_is_shuffled(self):
        self.assertFalse(Deck().shuffled)

    def test_shuffle_effect(self):
        deck = Deck()

        deck.shuffle()

        self.assertTrue(deck.shuffled)

class GetCard(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.card = self.deck.get_card()

    def test_deck_len_decreased(self):
        self.assertEqual(len(self.deck), 51)

    def test_card_value(self):
        self.assertEqual(self.card.rank, ranks[0])

    def test_exception_if_empty(self):
        while len(self.deck) > 0:
            self.deck.get_card()
        with self.assertRaises(IndexError):
            self.deck.get_card()

class AppendCard(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.zero = Card(ranks[0])
        custom_rank = 42 % len(ranks)
        self.non_zero = Card(ranks[custom_rank])

    def test_deck_len_increased(self):
        prev_len = len(self.deck)

        self.deck.append_card(self.zero)
        self.assertEqual(len(self.deck), prev_len + 1)

    def test_card_value(self):
        empty_deck = Deck()
        while len(empty_deck) > 0:
            empty_deck.get_card()

        empty_deck.append_card(self.non_zero)

        self.assertEqual(empty_deck.cards[0], self.non_zero)

    def test_card_value_and_position(self):
        self.deck.append_card(self.non_zero)

        self.assertEqual(self.deck.cards[-1], self.non_zero)

class AppendCards(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.cards_to_append = [Card(rank) for rank in ranks[:5]]

    def test_throws_when_not_iterable(self):
        with self.assertRaises(TypeError):
            Deck().append_cards(42)

    def test_throws_when_not_card(self):
        with self.assertRaises(TypeError):
            Deck.append_cards([42])

    def test_deck_len_increases(self):
        previous_len = len(self.deck)
        expected_increase = len(self.cards_to_append)

        self.deck.append_cards(self.cards_to_append)

        self.assertEqual(len(self.deck), previous_len + expected_increase)

    def test_appended_values(self):
        empty_deck = Deck()
        while len(empty_deck) > 0:
            empty_deck.get_card()

        empty_deck.append_cards(self.cards_to_append)

        for i, card in enumerate(self.cards_to_append):
            self.assertEqual(empty_deck.cards[i], card)

    def test_appended_values_and_positions(self):
        initial_len = len(self.deck)
        self.deck.append_cards(self.cards_to_append)

        for i, card in enumerate(self.cards_to_append):
            self.assertEqual(self.deck.cards[initial_len + i], card)

class IndexingSlicing(unittest.TestCase):
    def setUp(self):
        self.default_deck = Deck()

    def test_indexing_start(self):
        self.assertEqual(self.default_deck[0], Card(ranks[0]))

    def test_indexing_end(self):
        self.assertEqual(self.default_deck[-1], Card(ranks[-1]))

    def test_slicing(self):
        slice_obj = slice(3, 42, 3)

        self.assertEqual(self.default_deck[slice_obj], self.default_deck.cards[slice_obj])
