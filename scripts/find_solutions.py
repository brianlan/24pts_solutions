import argparse

from src.solution import get_possible_outputs

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cards", nargs="+", type=int, required=True)
parser.add_argument("-t", "--target", type=int, required=True)
parser.add_argument("-d", "--display-hint", action="store_true", default=False)


def main(args):
    possible_outputs = get_possible_outputs(tuple(args.cards), hint=True, target=args.target, display_hint=args.display_hint)
    print(args.target in possible_outputs)


if __name__ == '__main__':
    main(parser.parse_args())
