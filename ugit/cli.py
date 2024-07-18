# In charge of parsing and processing user input.


import argparse
import os  # modificarea/crearea fisierelor
from . import data


def main():
    args = parse_args()
    args.func(args)


# Argument parser pentru a putea implementa subcomenzi gen commit, init
def parse_args():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)

    return parser.parse_args()


def init(args):
    data.init()
    print(f"Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}")
