from .card import Card, ranks
from random import shuffle

class Deck:
    def __init__(self, cards_list = None):
        if cards_list is None:
            self.cards = []
            for rank in ranks:
                rank_suites = [Card(rank)] * 4
                self.cards.extend(rank_suites)
        elif isinstance(cards_list, list):
            self.cards = cards_list
        else:
            raise TypeError()

    def split(self):
        popped_cards = []
        for idx in range(len(self.cards) // 2):
            popped_cards.append(self.cards.pop())
        return Deck(popped_cards)

    def shuffle(self):
        shuffle(self.cards)

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
