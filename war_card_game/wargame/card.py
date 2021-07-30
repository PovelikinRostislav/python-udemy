ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {}
for idx, rank in enumerate(ranks):
    values[rank] = idx
del rank, idx

class Card:
    def __init__(self, rank):
        if not isinstance(rank, str):
            raise TypeError()
        elif rank not in ranks:
            raise ValueError()
        else:
            self.rank = rank
            self.value = values[rank]

    def __repr__(self):
        return f"Card of {self.rank} value"
