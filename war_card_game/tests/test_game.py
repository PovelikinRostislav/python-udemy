import unittest
from wargame.deck import Deck

def prepare_game_decks():
    deck_one = Deck()
    deck_two = deck_one.split()
    deck_one.shuffle(), deck_two.shuffle()
    return deck_one, deck_two

class TestGame(unittest.TestCase):
    def test_game_logic(self):
        deck_one, deck_two = prepare_game_decks()

        self.assertEqual(len(deck_one), (52//2))
        self.assertEqual(len(deck_two), len(deck_one))
        self.assertTrue(deck_one.shuffled)
        self.assertTrue(deck_two.shuffled)

        finished_game = False

        while not finished_game:
            finished_game = True

        # Finish
        self.assertTrue(finished_game)
