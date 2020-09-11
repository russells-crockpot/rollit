# pylint: disable=missing-docstring
"""
"""
import argparse
import sys
import traceback

from .exceptions import RollitRuntimeError
from .runtime import Runner, towers
from .repl.base import Repl
from .util import format_runtime_error

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
    argparser.add_argument('-d', '--debug', default=False, action='store_true')
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
    argparser.add_argument('script_file', help='rollit script to run.', nargs='?')
    argparser.add_argument('args',
                           help='Arguments to pass the rollit script.',
                           nargs=argparse.REMAINDER)
    return argparser


# pylint: disable=too-complex
def main():
    args = create_argparser().parse_args()
    runner = Runner(dice_tower=_TOWER_MAP[args.tower])
    try:
        if args.script_file:
            with open(args.script_file) as f:
                runner.sysargs = tuple(args.args)
                with runner.use_source(args.script_file):
                    runner.run(f.read())
        if args.command:
            with runner.use_source('cli'):
                result = runner.run(args.command)
            if not args.interactive:
                if result:
                    print(result)
                return
    except RollitRuntimeError as e:
        if args.debug:
            traceback.print_exc()
        print(format_runtime_error(e), file=sys.stderr)
        sys.exit(1)
    if args.interactive or not (args.command or args.script_file):
        with runner.use_source('interpreter'):
            if has_pretty and not args.ugly:
                repl = PrettyRepl(runner, options=args)
            else:
                repl = Repl(runner, options=args)
            repl.run()
