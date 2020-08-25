#!/bin/python3
# pylint: disable=missing-docstring
"""Takes the grammar file and saves it to a python module.
"""

import argparse
import pathlib
import re

import tatsu
import yapf

default_out_file = pathlib.Path(__file__).parent / 'src' / 'rollit' / 'parser.py'
default_grammar_file = pathlib.Path(__file__).parent / 'grammar.tatsu'

_SKIP_IF_STARTS_WITH = {
    'from tatsu.util import re, generic_main',
    'from tatsu.parsing import leftrec, nomemo',
    'import sys',
}


def create_arg_parser():
    argparser = argparse.ArgumentParser(
        __file__, description='Takes the grammar file and saves it to a python module.')
    argparser.add_argument('-o',
                           '--output',
                           help='Where to save the generated file to.',
                           default=default_out_file)
    argparser.add_argument('grammar', help='The grammar file to use.', default=default_grammar_file)
    return argparser


def alter_generated_code(src_code):
    parser_import_passed = False
    lines = []
    # The first line is a shebang, but we don't want this executable.
    # The second line is an encoding, but we're using python 3, so we don't need it.
    # The line after that is blank.
    # So we ignore the first three lines.
    for line in src_code.splitlines()[3:]:
        if re.match(r'^class\s+[A-Za-z0-9_]+Semantics\b.*:$', line):
            break
        should_skip = False
        for prefix in _SKIP_IF_STARTS_WITH:
            if line.startswith(prefix):
                should_skip = True
                break
        if should_skip:
            continue
        line = line.replace('rollitBuffer', '_Tokenizer')
        if line == 'from tatsu.parsing import Parser':
            line = f'{line} as _Parser'
            parser_import_passed = True
        elif parser_import_passed and 'Parser' in line:
            line = re.sub(r'\bParser\b', '_Parser', line)
            line = re.sub(r'rollitParser', 'Parser', line)
        lines.append(line)
    return lines


def main():
    args = create_arg_parser().parse_args()
    lines = [
        '""" The parser file, Automatically generated by TatSu (with some small modifications).',
        '"""',
        '# pylint: skip-file',
        '#',
        '#' * 100,
        '#',
    ]
    print(f'Generating parser from grammar file {args.grammar}...')
    with open(args.grammar) as f:
        src_code = tatsu.to_python_sourcecode(f.read(), parseinfo=True)[3:]
    lines += alter_generated_code(src_code)
    src_code = '\n'.join(lines).strip()
    with open(args.output, 'w') as f:
        f.write(src_code)
    print(f'Saved parser to {args.output}.')
    print(f'Running yapf on {args.output}...')
    yapf.main(['yapf', '-i', str(args.output)])
    print('Finished parser generation.')


if __name__ == '__main__':
    main()
