from .card import Card, ranks

class Deck:
    def __init__(self):
        self.cards = []
        for rank in ranks:
            rank_suites = [Card(rank)] * 4
            self.cards.extend(rank_suites)
