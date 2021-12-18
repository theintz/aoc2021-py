from __future__ import annotations
from typing import List, Tuple
from math import prod

with open("day16-input.txt") as f:
    value = f.read()

# part 1
class BitString():
    s: str # string of 0 and 1

    def __init__(self, s: str) -> None:
        if s.startswith("0b"):
            self.s = s[2:]
        elif s.startswith("0x"):
            # highly inefficient
            self.s = "".join([bin(int(n, 16))[2:].rjust(4, "0") for n in s[2:]])
        else:
            assert(False)
    
    def as_int(self) -> int:
        return int(self.s, 2)
    
    def sub(self, pos: int, count: int = -1) -> BitString:
        if count == -1:
            count = len(self.s)
        return BitString("0b" + self.s[pos:pos + count])
    
    def __len__(self) -> int:
        return len(self.s)
    
    def __str__(self) -> str:
        return self.s

def test_bitstring():
    bs = BitString("0xAAA")
    assert(bs.s == "101010101010")
    assert(bs.as_int() == 2730)
    assert(bs.sub(0, 1).as_int() == 1)
    assert(bs.sub(0, 3).as_int() == 5)
    assert(bs.sub(2, 3).as_int() == 5)
    assert(bs.sub(3, 1).as_int() == 0)
    assert(bs.sub(8, 4).as_int() == 10)
    assert(bs.sub(2, -1).as_int() == 682)
    assert(bs.sub(4).as_int() == 170)
    assert(len(bs) == 12)

    bs = BitString("0xD2FE28")
    assert(bs.s == "110100101111111000101000")

test_bitstring()

class Packet:
    type: str
    version: int
    value: int = 0
    len_type: str = ""
    length: int = 0
    sub_packets: List[Packet] = []

    def __init__(self, type: str, version: int):
        self.type = type
        self.version = version

    def __str__(self) -> str:
        return str(vars(self))

PACKET_TYPES = {
    0: "sum",
    1: "pro",
    2: "min",
    3: "max",
    4: "lit",
    5: "gth",
    6: "lth",
    7: "equ"
}

def parse_header(raw: BitString) -> Tuple[Packet, int]:
    version = raw.sub(0, 3).as_int()
    type = raw.sub(3, 3).as_int()
    p = Packet(PACKET_TYPES[type], version)
    header_len = 6

    if type != 4: # operator packet
        p.len_type = "numsub" if raw.sub(6, 1).as_int() else "bitlen"
        p.length = raw.sub(7, 15 if p.len_type == "bitlen" else 11).as_int()
        header_len += 16 if p.len_type == "bitlen" else 12
    
    return (p, header_len)

def parse_literal(raw: BitString) -> Tuple[int, int]:
    i = 0
    val = 0

    while i + 5 <= len(raw):
        cur = raw.sub(i, 5).as_int()
        val = (val << 4) + (cur & 0x0f)
        i += 5

        if not (cur & 0x10):
            break
    
    return (val, i)

def parse_single_packet(raw: BitString) -> Tuple[Packet, int]:
    p, consumed_header = parse_header(raw)
    raw = raw.sub(consumed_header, -1)

    if p.type == "lit":
        value, consumed_body = parse_literal(raw)
        p.value = value
    else:
        raw_opr = raw.sub(0, p.length) if p.len_type == "bitlen" else raw
        count = p.length if p.len_type == "numsub" else -1

        ps, consumed_body = parse_packets(raw_opr, count)
        p.sub_packets = ps
    
    return (p, consumed_header + consumed_body)

def parse_packets(raw: BitString, count: int = -1) -> Tuple[List[Packet], int]:
    ps = []
    total_consumed = 0
    while len(raw) >= 11:
        p, consumed = parse_single_packet(raw)
        raw = raw.sub(consumed, -1)
        ps.append(p)
        total_consumed += consumed

        if count > 0 and len(ps) == count:
            break
    
    return (ps, total_consumed)

p, _ = parse_packets(BitString("0x" + value))
print(p[0])

def cum_versions(packets: List[Packet]) -> int:
    v = 0
    for p in packets:
        v += p.version
        v += cum_versions(p.sub_packets)
    return v

print(cum_versions(p))

# part 2

def evaluate(p: Packet) -> int:
    if p.type == "lit":
        return p.value
    elif p.type == "sum":
        return sum([evaluate(sp) for sp in p.sub_packets])
    elif p.type == "pro":
        return prod([evaluate(sp) for sp in p.sub_packets])
    elif p.type == "min":
        return min([evaluate(sp) for sp in p.sub_packets])
    elif p.type == "max":
        return max([evaluate(sp) for sp in p.sub_packets])
    elif p.type == "gth":
        return 1 if evaluate(p.sub_packets[0]) > evaluate(p.sub_packets[1]) else 0
    elif p.type == "lth":
        return 1 if evaluate(p.sub_packets[0]) < evaluate(p.sub_packets[1]) else 0
    elif p.type == "equ":
        return 1 if evaluate(p.sub_packets[0]) == evaluate(p.sub_packets[1]) else 0

print(evaluate(p[0]))