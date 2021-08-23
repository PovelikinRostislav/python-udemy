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

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def split(self):
        popped_cards = []
        for idx in range(len(self.cards) // 2):
            popped_cards.append(self.cards.pop())
        return Deck(popped_cards)

    def shuffle(self):
        shuffle(self.cards)
        self.shuffled = True

    def get_card(self):
        # Pull out the card from the top, which is 0 index
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            raise IndexError('getting card from empty deck')

    def append_card(self, card):
        # Put the card to the bottom, which is in the end of the list
        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise TypeError()

    def append_cards(self, cards):
        for card in cards:
            self.append_card(card)
