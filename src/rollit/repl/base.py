"""
"""
import sys
import traceback
from collections import deque

from abc import ABCMeta, abstractmethod

from ..exceptions import RollitException, RollitRuntimeError
from ..grammar import ParseError
from ..runtime.objects import Roll
from ..util import format_runtime_error, is_valid_iterable

# try:
# import readline  # pylint: disable=unused-import
# except ImportError:
# pass

__all__ = ['BaseRepl', 'Repl']


class BaseRepl(metaclass=ABCMeta):
    """
    """

    prompt_text = '>>> '

    def __init__(self, runner, options):
        self.runner = runner
        self.options = options
        self.indent_level = 0
        self.line_tokens = deque()
        self.input_buffer = deque()

    @abstractmethod
    def prompt(self):
        """
        """

    def evaluate(self, user_input):
        """
        """
        return self.runner.run(user_input)

    def print_result(self, result):
        """
        """
        print(result)

    def next_statement(self):
        """
        """
        multiline = True
        while multiline or self.line_tokens:
            multiline = False
            self.input_buffer.append(self.prompt().strip())
            if self.input_buffer[-1].endswith('%>'):
                multiline = True
                if len(self.input_buffer) == 1 \
                        or not self.input_buffer[-2].endswith('%>'):
                    self.indent_level += 1
            #FIXME handle this MUCH better
            if '[' in self.input_buffer[-1]:
                self.line_tokens.append(']')
                self.indent_level += 1
            if self.line_tokens:
                if self.line_tokens[-1] == ']' and ']' in self.input_buffer[-1]:
                    self.line_tokens.pop()
                    self.indent_level -= 1
        self.indent_level = 0
        return '\n'.join(self.input_buffer)

    def print_error(self, error):
        """
        """
        if isinstance(error, RollitRuntimeError):
            if getattr(self.options, 'debug', False):
                traceback.print_exc()
            print(format_runtime_error(error), file=sys.stderr)
        else:
            traceback.print_exc()
        # print(f'{type(error).__name__}: {error}', file=sys.stderr)

    def run(self):
        """
        """
        while True:
            try:
                self.input_buffer.clear()
                user_input = self.next_statement()
                if not user_input.strip().strip('|'):
                    continue
                results = self.runner.run(user_input)
                if not is_valid_iterable(results) or isinstance(results, Roll):
                    results = (results,)
                for result in results:
                    if isinstance(result, str):
                        result = f"'{result}'"
                    self.print_result(result)
            except (RollitException, ParseError) as e:
                self.print_error(e)
            except (KeyboardInterrupt, EOFError):
                return
            except Exception:
                traceback.print_exc()


class Repl(BaseRepl):
    """
    """

    def prompt(self):
        return input(self.prompt_text)  # nosec
