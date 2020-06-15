import const
from argparse import ArgumentParser


class ArgParse:

    parser = None
    args = None

    def __init__(self):
        self.parser = ArgumentParser(description='Visualize various sorting algorithms')
        self.parser.add_argument('-q', help='Quicksort', action='store_true')
        self.parser.add_argument('-b', help='Bubblesort', action='store_true')
        self.parser.add_argument('-s', help='Shellsort', action='store_true')
        self.args = self.parser.parse_args()
        print(self.args)


    def parse_args(self):
        if self.args.q:
            const.QUICKSORT = True
        elif self.args.b:
            const.BUBBLESORT = True
        elif self.args.s:
            const.SHELLSORT = True

    def print_usage(self):
        self.parser.print_help()

