import argparse

from src.solution import get_possible_outputs

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cards", nargs="+", type=int, required=True)
parser.add_argument("-t", "--target", type=int, required=True)


def main(args):
    possible_outputs = get_possible_outputs(tuple(args.cards))
    print(args.target in possible_outputs)


if __name__ == '__main__':
    main(parser.parse_args())
