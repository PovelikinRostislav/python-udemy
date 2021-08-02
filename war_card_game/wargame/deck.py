from .card import Card, ranks
from random import shuffle

class Deck:
    def __init__(self, cards_list = None):
        self.shuffled = False

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
        self.shuffled = True

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def __len__(self):
        return len(self.cards)
