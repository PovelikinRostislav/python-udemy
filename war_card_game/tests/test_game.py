import unittest
from wargame.deck import Deck
from wargame.card import Card, ranks
from copy import copy

def prepare_random_game_decks():
    deck_one = Deck()
    deck_two = deck_one.split()
    deck_one.shuffle(), deck_two.shuffle()
    return deck_one, deck_two

def check_result(deck_one, deck_two, winner_cards):
    if len(deck_one) != 0 and len(deck_two) != 0:
        raise Exception("Wrong game logic")
    elif len(winner_cards) != 0:
        raise Exception("Wrong game logic")
    elif len(deck_one) != 0 and len(deck_two) == 0:
        return (True, False)
    else:
        return (False, True)

def game_logic(deck_one, deck_two):
    winner_cards = []

    while len(deck_one) != 0 and len(deck_two) != 0:
        deck_one_card = deck_one.get_card()
        deck_two_card = deck_two.get_card()

        winner_cards.append(deck_one_card)
        winner_cards.append(deck_two_card)

        if deck_one_card < deck_two_card:
            # This take goes to Player 2. Keep playing
            deck_two.append_cards(winner_cards)
            winner_cards.clear()
        elif deck_one_card > deck_two_card:
            # This take goes to Player 1. Keep playing
            deck_one.append_cards(winner_cards)
            winner_cards.clear()
        elif len(deck_one) <= 3:
            # Player 1 has no cards for war continuation, he loses the game
            for _ in range(len(deck_one)):
                deck_two.append_card(deck_one.get_card())
            deck_two.append_cards(winner_cards)
            winner_cards.clear()
        elif len(deck_two) <= 3:
            # Player 2 has no cards for war continuation, he loses the game
            for _ in range(len(deck_two)):
                deck_one.append_card(deck_two.get_card())
            deck_one.append_cards(winner_cards)
            winner_cards.clear()
        else:
            # Players have cards for War state. Keep playing
            for i in range(3):
                winner_cards.append(deck_one.get_card())
                winner_cards.append(deck_two.get_card())

    winner = check_result(deck_one, deck_two, winner_cards)

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

class TwoCardGame(unittest.TestCase):
    def setUp(self):
        self.winner_cards = [Card(ranks[4]), Card(ranks[5])]
        self.loser_cards = [Card(ranks[0]), Card(ranks[1])]

        self.winner_deck = Deck(self.winner_cards)
        self.loser_deck = Deck(self.loser_cards)

    def test_winner_loser(self):
        result = game_logic(self.winner_deck, self.loser_deck)
        self.assertEqual(result, (True, False))

    def test_loser_winner(self):
        result = game_logic(self.loser_deck, self.winner_deck)
        self.assertEqual(result, (False, True))

    def test_decks_len(self):
        game_logic(self.winner_deck, self.loser_deck)

        self.assertEqual(len(self.winner_deck), 4)
        self.assertEqual(len(self.loser_deck), 0)

    def test_winner_deck_content(self):
        game_logic(self.winner_deck, self.loser_deck)

        for card in self.winner_cards:
            self.assertIn(card, self.winner_deck)
        for card in self.loser_cards:
            self.assertIn(card, self.winner_deck)

    def test_equal_decks(self):
        result = game_logic(self.winner_deck, copy(self.winner_deck))

        self.assertEqual(result, (False, True))

class RandomDecksGame(unittest.TestCase):
    def test_decks_len(self):
        for _ in range(42):
            deck_one, deck_two = prepare_random_game_decks()
            result = game_logic(deck_one, deck_two)

            if result[0]:
                self.assertEqual(len(deck_one), 52)
                self.assertEqual(len(deck_two), 0)
            else:
                self.assertEqual(len(deck_one), 0)
                self.assertEqual(len(deck_two), 52)

    def test_winner_deck_content(self):
        for _ in range(42):
            ranks_dict = {rank:4 for rank in ranks}

            deck_one, deck_two = prepare_random_game_decks()
            result = game_logic(deck_one, deck_two)

            if result[0]:
                for card in deck_one:
                    ranks_dict[card.rank] -= 1

                self.assertFalse(any(ranks_dict.values()))
            else:
                for card in deck_two:
                    ranks_dict[card.rank] -= 1

                self.assertFalse(any(ranks_dict.values()))

