#!/bin/python3
# pylint: disable=missing-docstring
"""Takes the grammar file and saves it to a python module.
"""

import argparse
import os
import pathlib
import subprocess  # nosec

default_out_file = pathlib.Path(__file__).parent / 'src' / 'rollit' / 'grammar.py'
default_grammar_file = pathlib.Path(__file__).parent / 'grammar.peg'


def create_arg_parser():
    argparser = argparse.ArgumentParser(
        __file__, description='Takes the grammar file and saves it to a python module.')
    argparser.add_argument('--skip-yapf', action='store_true', default=False)
    argparser.add_argument('-o',
                           '--output',
                           help='Where to save the generated file to.',
                           default=default_out_file)
    argparser.add_argument('grammar',
                           help='The grammar file to use.',
                           default=default_grammar_file,
                           type=pathlib.Path)
    return argparser


def main():
    args = create_arg_parser().parse_args()
    print(f'Generating parser from grammar file {args.grammar}...')
    subprocess.run(  # nosec
        ['canopy', '--lang', 'python', str(args.grammar)], stderr=subprocess.DEVNULL,
        text=True, check=True,
    )
    os.rename(f'{args.grammar.stem}.py', args.output)
    print(f'Saved parser to {args.output}.')


if __name__ == '__main__':
    main()
