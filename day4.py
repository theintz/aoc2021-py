from typing import List

MAGIC_WINNER_BITMASK_5X5_TABLE = [
    # rows
    0x0000001f,
    0x000003e0,
    0x00007c00,
    0x000f8000,
    0x01f00000,
    # columns
    0x01084210,
    0x00842108,
    0x00421084,
    0x00210842,
    0x00108421,
]

class BingoCard:
    # these are the numbers on the card
    numbers: List[int]
    # the bits of this int represent the numbers on the card that have been called
    # they correspond to the indices of the numbers var above
    hits: int = 0
    id = 0

    def __init__(self, numbers: str):
        numbers = numbers.replace("\n", " ").replace("  ", " ").strip()
        self.numbers = [int(n) for n in numbers.split(" ")]
        self.id = ".".join([str(n) for n in self.numbers])

    def hit(self, number: int) -> bool:
        if not number in self.numbers:
            return False

        index = self.numbers.index(number)
        self.hits |= 1 << index

        return True

    def won(self) -> bool:
        for bm in MAGIC_WINNER_BITMASK_5X5_TABLE:
            if self.hits & bm == bm:
                return True
        
        return False

    def sum_empty(self) -> int:
        sum = 0

        for i in range(len(self.numbers)):
            if not self.hits & 1 << i:
                sum += self.numbers[i]
        
        return sum

    def reset(self) -> None:
        self.hits = 0

def test_bingo_card():
    td = "22 13 17 11  0\n" \
         " 8  2 23  4 24\n" \
         "21  9 14 16  7\n" \
         " 6 10  3 18  5\n" \
         " 1 12 20 15 19"

    bc = BingoCard(td)
    
    assert(bc.id == "22.13.17.11.0.8.2.23.4.24.21.9.14.16.7.6.10.3.18.5.1.12.20.15.19")
    assert(bc.hit(21))
    assert(bc.hit(9))
    assert(not bc.won())
    assert(not bc.hit(34))
    assert(bc.hit(14))
    assert(bc.hit(16))
    assert(bc.hit(24))
    assert(not bc.won())
    assert(bc.hit(7))
    assert(bc.won())
    assert(bc.sum_empty() == 209)

    bc.reset()

    assert(bc.hit(17))
    assert(bc.hit(23))
    assert(not bc.won())
    assert(not bc.hit(34))
    assert(bc.hit(14))
    assert(bc.hit(3))
    assert(bc.hit(18))
    assert(not bc.won())
    assert(bc.hit(20))
    assert(bc.won())
    assert(bc.sum_empty() == 205)

# prove that the implementation is correct
test_bingo_card()

with open("day4-input.txt") as f:
    values = f.read().splitlines()

def hit_all_cards(cards: List[BingoCard], number:int ) -> BingoCard:
    for c in cards:
        c.hit(number)

        if c.won():
            return c
    
    return None

# part 1
seq = [int(v) for v in values[0].split(",")]
values = values[2:]
cards = []

while len(values) > 0:
    board = " ".join(values[:5])
    card = BingoCard(board)
    #print("created card " + card.id)
    cards.append(card)
    values = values[6:]

for s in seq:
    winner = None

    for c in cards:
        c.hit(s)
    
    for c in cards:
        if c.won():
            winner = c

    if winner:
        print(f"card {winner.id} won with number {s}")
        sum_empty = winner.sum_empty()
        print(sum_empty, sum_empty * s)
        break

# part 2
for c in cards:
    c.reset()

for s in seq:
    loser = None

    for c in cards:
        c.hit(s)
    
    for c in cards:
        if c.won():
            if len(cards) == 1:
                loser = c

            cards.remove(c)
    
    if len(cards) == 0:
        print(f"card {loser.id} is the last one at number {s}")
        sum_empty = loser.sum_empty()
        print(sum_empty, sum_empty * s)
        break