import argparse

import numpy as np

from src.solution import get_possible_outputs

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--num-cards", type=int, required=True)
parser.add_argument("--legal-numbers", nargs="+", type=int, default=list(range(1, 14)))
parser.add_argument("-t", "--target", type=int, required=True)


def main(args):
    while True:
        cards = np.random.choice(args.legal_numbers, size=args.num_cards, replace=True)
        possible_outputs = get_possible_outputs(tuple(cards), hint=False, target=args.target)
        if args.target in possible_outputs:
            print(f"#" * 40)
            print(f"# Generated quiz: {sorted(cards)}")
            print(f"#" * 40)
            get_possible_outputs(tuple(cards), hint=True, target=args.target)
            break

if __name__ == '__main__':
    main(parser.parse_args())
