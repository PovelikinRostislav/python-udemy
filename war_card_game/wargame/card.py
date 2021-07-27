ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {}
for idx, rank in enumerate(ranks):
    values[rank] = idx

class Card:
    def __init__(self, rank):
        if rank not in ranks:
            raise ValueError()

        self.rank = rank
        self.value = values[rank]
