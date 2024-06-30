from typing import List, Set, Tuple
from functools import lru_cache
import operator as op
from itertools import permutations, combinations

import numpy as np


class NoSolutionError(Exception):
    pass


def get_possible_partitions(cards: List[int]) -> Set[Tuple[Tuple[int]]]:
    n = len(cards)
    assert n > 1, f"at least 2 cards needed, but {n!r} is given."
    cards = np.array(cards)
    possible_partitions = set()
    for num_left in range(1, n // 2 + 1):
        for left_idx in combinations(range(n), num_left):
            left_idx = np.in1d(np.arange(n), left_idx)
            left, right = (
                tuple(np.sort(cards[left_idx])),
                tuple(np.sort(cards[~left_idx])),
            )  # sort helps the reuse of lru_cache
            possible_partitions.add((left, right))
    return possible_partitions


@lru_cache(maxsize=None)
def get_possible_outputs(cards: List[int], hint=False, target=None, display_hint=False) -> List[int]:
    num_cards = len(cards)
    possible_outputs = set()
    if num_cards == 1:
        possible_outputs.add(cards[0])
    elif num_cards == 2:
        possible_outputs.add(cards[0] + cards[1])
        possible_outputs.add(cards[0] * cards[1])
        possible_outputs.add(cards[0] - cards[1])
        possible_outputs.add(cards[1] - cards[0])
        if cards[1] != 0 and cards[0] % cards[1] == 0:
            possible_outputs.add(cards[0] // cards[1])
        if cards[0] != 0 and cards[1] % cards[0] == 0:
            possible_outputs.add(cards[1] // cards[0])
    else:
        for left, right in get_possible_partitions(cards):
            for l in get_possible_outputs(left):
                for r in get_possible_outputs(right):
                    o = get_possible_outputs((l, r))
                    possible_outputs |= o
                    if target and hint:
                        if target in o and len(left) + len(right) == len(cards):
                            if display_hint:
                                print(f"Hint: {left=}, {right=}, {l=}, {r=}")
    return possible_outputs
