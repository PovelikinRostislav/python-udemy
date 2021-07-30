from .card import Card, ranks

class Deck:
    def __init__(self):
        self.cards = []
        for rank in ranks:
            rank_suites = [Card(rank)] * 4
            self.cards.extend(rank_suites)

    def shuffle(self):
        shuffle(self.cards)

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
