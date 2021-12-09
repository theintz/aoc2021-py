from typing import Dict, List

with open("day8-input.txt") as f:
    values = f.read().splitlines()
    values = [v.split(" | ") for v in values]
    values = [(v[0].split(" "), v[1].split(" ")) for v in values]

# part 1
count = sum([len([r for r in result if len(r) in (2, 3, 4, 7)]) for _, result in values])
print(count)

# part 2
PATTERN_MAPPINGS_5S6S = {
    "acdeg": "2",
    "acdfg": "3",
    "abdfg": "5",
    "abcefg": "0",
    "abdefg": "6",
    "abcdfg": "9",
}

LEGAL_PATTERNS_5S6S = list(PATTERN_MAPPINGS_5S6S.keys())

def str_diff(s1: str, s2: str) -> str:
    diff = ""

    for c in s1:
        if c not in s2:
            diff += c

    for c in s2:
        if c not in s1:
            diff += c

    return diff

def test_str_diff():
    assert(str_diff("abc", "abc") == "")
    assert(str_diff("ab", "abc") == "c")
    assert(str_diff("abc", "b") == "ac")
    assert(str_diff("a", "") == "a")

test_str_diff()

def apply_mapping(pattern: str, mapping: Dict) -> List[str]:
    """ A function that applies an incomplete mapping to a
    given string, producing all possible combinations. """
    results = []

    for char in pattern:
        if len(mapping[char]) == 0:
            raise Exception("something weird happened")

        if not results:
            results = list(mapping[char])
        else:
            results = [r + replacement for r in results for replacement in mapping[char] if replacement not in r]

    return results

def test_apply_mapping():
    mapping_a = {"a": "fg", "b": "h"}
    str_a = "ab"
    assert(apply_mapping(str_a, mapping_a) == ["fh", "gh"])

    mapping_a = {"a": "fg", "b": "h", "c": "fg"}
    str_a = "abc"
    assert(apply_mapping(str_a, mapping_a) == ["fhg", "ghf"])

    mapping_a = {"a": "f", "b": "h"}
    str_a = "ba"
    assert(apply_mapping(str_a, mapping_a) == ["hf"])

    mapping_a = {"a": "fg", "b": "hi", "c": "fg"}
    str_a = "abc"
    assert(apply_mapping(str_a, mapping_a) == ["fhg", "fig", "ghf", "gif"])

test_apply_mapping()

def sort_p(pattern: str) -> str:
    return "".join(sorted(pattern))

total = 0
for pattern, result in values:
    mapping = { chr(n): "x" for n in range(97, 104) }
    mapping_sorted_ps = { sort_p(p): -1 for p in pattern}

    pattern_1 = [p for p in pattern if len(p) == 2][0]
    mapping[pattern_1[0]] = "cf"
    mapping[pattern_1[1]] = "cf"
    mapping_sorted_ps[sort_p(pattern_1)] = "1"

    pattern_7 = [p for p in pattern if len(p) == 3][0]
    mapping_a = str_diff(pattern_1, pattern_7)
    mapping[mapping_a] = "a"
    mapping_sorted_ps[sort_p(pattern_7)] = "7"

    pattern_4 = [p for p in pattern if len(p) == 4][0]
    mapping_bd = str_diff(pattern_1, pattern_4)
    mapping[mapping_bd[0]] = "bd"
    mapping[mapping_bd[1]] = "bd"
    mapping_sorted_ps[sort_p(pattern_4)] = "4"

    pattern_8 = [p for p in pattern if len(p) == 7][0]
    mapping_eg = str_diff(pattern_4 + mapping_a, pattern_8)
    mapping[mapping_eg[0]] = "eg"
    mapping[mapping_eg[1]] = "eg"
    mapping_sorted_ps[sort_p(pattern_8)] = "8"

    for pattern_5s6s in sorted([p for p in pattern if len(p) == 5 or len(p) == 6], key=len):
        # check whether mapping is already solved
        # if all([False for v in mapping.values() if len(v) != 1]):
        #     break

        applied = apply_mapping(pattern_5s6s, mapping)
        applied = [p for p in applied if sort_p(p) in LEGAL_PATTERNS_5S6S]

        # this may fail, let's see
        assert(len(applied) <= 2)

        for i in range(len(pattern_5s6s)):
            if len(applied) > 1 and applied[0][i] != applied[1][i]:
                continue

            mapping[pattern_5s6s[i]] = applied[0][i]

        mapping_sorted_ps[sort_p(pattern_5s6s)] = PATTERN_MAPPINGS_5S6S[sort_p(applied[0])]

    res_applied = int("".join([mapping_sorted_ps[sort_p(r)] for r in result]))
    #print(res_applied)
    total += res_applied

print(total)
