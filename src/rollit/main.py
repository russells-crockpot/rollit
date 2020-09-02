# pylint: disable=missing-docstring
"""
"""
import argparse
import sys

from .execution import ExecutionEnvironment, towers
from .repl.base import Repl
has_pretty = False
try:
    from .repl.pretty import PrettyRepl
    has_pretty = True
except ImportError:
    pass

_TOWER_MAP = {
    'default': towers.DefaultTower,
    'incremental': towers.IncrementalTower,
    'max': towers.MaxTower,
    'min': towers.MinTower,
}


def create_argparser():
    argparser = argparse.ArgumentParser(__file__, description='rollit interpreter')
    argparser.add_argument(
        '-t',
        '--tower',
        help='The tower class to use.',
        default='default',
        choices=['default', 'incremental', 'max', 'min'],
    )
    argparser.add_argument('-i',
                           '--interactive',
                           help='Start in interactive mode.',
                           default=False,
                           action='store_true')
    argparser.add_argument(
        '-c',
        '--command',
        help='Executes the provided command.',
        default=None,
    )
    if has_pretty:
        argparser.add_argument(
            '--ugly',
            help="Don't use the pretty REPL.",
            default=False,
            action='store_true',
        )
        argparser.add_argument(
            '-e',
            '--edit-mode',
            help='Edit more to use.',
            choices=['vi', 'emacs'],
            default='vi',
        )
        argparser.add_argument(
            '-s',
            '--style',
            help='The pygments style to use.',
            default='vim',
        )
        argparser.add_argument(
            '-m',
            '--multiline',
            help='Use multiline mode.',
            default=False,
            action='store_true',
        )
    argparser.add_argument('script_file', help='rollit script to run.', nargs=argparse.REMAINDER)
    return argparser


def main():
    args = create_argparser().parse_args()
    env = ExecutionEnvironment(dice_tower=_TOWER_MAP[args.tower])
    if args.script_file:
        if len(args.script_file) > 1:
            print('Only one rollit script file can be provided at at time!', file=sys.stderr)
            sys.exit(1)
        with open(args.script_file[0]) as f:
            env.run(f.read())
    if args.command:
        result = env.run(args.command)
        if not args.interactive:
            if result:
                print(result)
            return
    if args.interactive or not (args.command or args.script_file):
        if has_pretty and not args.ugly:
            repl = PrettyRepl(env, options=args)
        else:
            repl = Repl(env, options=args)
        repl.run()
