#!/bin/python3
# pylint: disable=missing-docstring
"""Takes the grammar file and saves it to a python module.
"""
import argparse
import contextlib
import pathlib

from lark.tools.standalone import main as build_parser

default_out_file = pathlib.Path(__file__).parent / 'src' / 'rollit' / 'parser.py'
default_grammar_file = pathlib.Path(__file__).parent / 'grammar.lark'


def create_arg_parser():
    argparser = argparse.ArgumentParser(
        __file__, description='Takes the grammar file and saves it to a python module.')
    argparser.add_argument('-g',
                           '--grammar',
                           help='The grammar file to use.',
                           default=default_grammar_file)
    argparser.add_argument('-o',
                           '--output',
                           help='Where to save the generated file to.',
                           default=default_out_file)
    return argparser


def main():
    args = create_arg_parser().parse_args()
    print(f'Generating parser from grammar {args.grammar}')
    with open(args.output, 'w') as f:
        with contextlib.redirect_stdout(f):
            # Begin by telling pylint that it should skip this file.
            print('# pylint: skip-file')
            # Next, tell yapf not to try and format it
            print('# yapf: disable')
            build_parser(args.grammar, 'start')
    print(f'Saved grammar to {args.output}')


if __name__ == '__main__':
    main()
