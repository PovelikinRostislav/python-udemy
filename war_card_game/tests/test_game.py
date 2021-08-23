import unittest
from wargame.deck import Deck
from wargame.card import Card, ranks

def prepare_random_game_decks():
    deck_one = Deck()
    deck_two = deck_one.split()
    deck_one.shuffle(), deck_two.shuffle()
    return deck_one, deck_two

def game_logic(deck_one, deck_two):
    winner_cards = []
    while len(deck_one) != 0 and len(deck_two) != 0:
        deck_one_card = deck_one.get_card()
        deck_two_card = deck_two.get_card()

        winner_cards.append(deck_one_card)
        winner_cards.append(deck_two_card)

        if deck_one_card < deck_two_card:
            deck_two.append_cards(winner_cards)
        elif deck_one_card > deck_two_card:
            deck_one.append_cards(winner_cards)
        else:
            try:
                for i in range(3):
                    winner_cards.append(deck_one.get_card())
                    winner_cards.append(deck_two.get_card())
            except IndexError:
                break

    if len(deck_one) != 0 and len(deck_two) == 0:
        winner = (True, False)
    else:
        winner = (False, True)

    return winner


class OneCardGame(unittest.TestCase):
    def setUp(self):
        self.winner_card = Card(ranks[1])
        self.loser_card = Card(ranks[0])

        self.winner_deck = Deck([self.winner_card])
        self.loser_deck = Deck([self.loser_card])

    def test_winner_loser(self):
        result = game_logic(self.winner_deck, self.loser_deck)
        self.assertEqual(result, (True, False))

    def test_loser_winner(self):
        result = game_logic(self.loser_deck, self.winner_deck)
        self.assertEqual(result, (False, True))

    def test_decks_len(self):
        game_logic(self.winner_deck, self.loser_deck)

        self.assertEqual(len(self.winner_deck), 2)
        self.assertEqual(len(self.loser_deck), 0)

    def test_winner_deck_content(self):
        game_logic(self.winner_deck, self.loser_deck)

        self.assertIn(self.winner_card, self.winner_deck)
        self.assertIn(self.loser_card, self.winner_deck)

    def test_equal_decks(self):
        result = game_logic(self.winner_deck, Deck([self.winner_card]))

        self.assertEqual(result, (False, True))

