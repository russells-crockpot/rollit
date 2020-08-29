# pylint: disable=missing-docstring
"""
"""
import argparse
import sys

from .execution import ExecutionEnvironment


# pylint: disable=import-outside-toplevel
def _get_repl(env):
    try:
        from .repl.pretty import PrettyRepl as Repl
    except ImportError:
        from .repl.base import Repl
    return Repl(env)


def create_argparser():
    argparser = argparse.ArgumentParser(__file__, description='rollit interpreter')
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
    argparser.add_argument('script_file', help='rollit script to run.', nargs=argparse.REMAINDER)
    return argparser


def main():
    args = create_argparser().parse_args()
    env = ExecutionEnvironment()
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
        repl = _get_repl(env)
        repl.run()
