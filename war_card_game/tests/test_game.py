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

        finished_game = False

        while not finished_game and len(deck_one) != 0 and len(deck_two) != 0:
            deck_one_card = deck_one.get_card()
            deck_two_card = deck_two.get_card()

            if deck_one_card < deck_two_card:
                deck_one.append_card(deck_one_card)
                deck_one.append_card(deck_two_card)
            elif deck_one_card > deck_two_card:
                deck_two.append_card(deck_one_card)
                deck_two.append_card(deck_two_card)
            else:
                pass

            finished_game = True

        # Finish
        self.assertTrue(finished_game)
