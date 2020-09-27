"""
"""
import itertools
import pathlib

import appdirs
import prompt_toolkit as pt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter, NestedCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import style_from_pygments_cls
from pygments.styles import get_style_by_name

from .. import langref
from .base import BaseRepl
from ..extra.pygments import RollitLexer
from ..runtime import context as curent_context

__all__ = []

cachedir = pathlib.Path(appdirs.user_cache_dir('rollit')) / 'repl'
cachedir.mkdir(parents=True, exist_ok=True)


class ScopeCompleter(WordCompleter):
    """
    """

    def __init__(self, runner, scope_attr):
        super().__init__(None)
        self.runner = runner
        self.scope_attr = scope_attr

    @property
    # pylint: disable=missing-function-docstring
    def words(self):
        if curent_context:
            context = curent_context
        else:
            context = self.runner.default_context
        return getattr(context.scope, self.scope_attr)

    @words.setter
    def words(self, value):
        return


class VariableCompleter(WordCompleter):
    """
    """

    def __init__(self, runner):
        super().__init__(None)
        self.runner = runner

    @property
    # pylint: disable=missing-function-docstring
    def words(self):
        if curent_context:
            context = curent_context
        else:
            context = self.runner.default_context
        return context.scope.variable_names()

    @words.setter
    def words(self, value):
        return


class LoopCompleter(WordCompleter):
    """
    """

    def __init__(self, runner):
        super().__init__(None)
        self.runner = runner

    @property
    # pylint: disable=missing-function-docstring
    def words(self):
        if curent_context:
            context = curent_context
        else:
            context = self.runner.default_context
        return context.scope.loops + ['~', '^', '!']

    @words.setter
    def words(self, value):
        return


class PrettyRepl(BaseRepl):
    """
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._output_style = None
        self._session = pt.PromptSession(
            message=self.prompt_text,
            history=FileHistory(cachedir / 'history.txt'),
            editing_mode=getattr(pt.enums.EditingMode, self.options.edit_mode.upper()),
            auto_suggest=AutoSuggestFromHistory(),
            enable_open_in_editor=True,
            completer=self._create_completer(),
            multiline=self.options.multiline,
            style=style_from_pygments_cls(get_style_by_name(self.options.style)),
            prompt_continuation=self._prompt_continuation,
            lexer=pt.lexers.PygmentsLexer(RollitLexer, sync_from_start=True),
            search_ignore_case=True,
        )

    def _create_completer(self):
        variable_completer = ScopeCompleter(self.runner, 'variable_names')
        loop_completer = LoopCompleter(self.runner)
        modifier_completer = ScopeCompleter(self.runner, 'modifier_names')
        d = {k: None for k in itertools.chain(
            langref.KEYWORDS,
            langref.SPECIAL_REFERENCES,
        )}
        d['->'] = modifier_completer
        d['=>'] = modifier_completer
        d['for'] = {'every': None}
        d['except'] = {'when': None}
        d['but'] = {'if': None, 'always': None}
        d['restart'] = {
            'before': loop_completer,
            'at': loop_completer,
            'after': loop_completer,
        }
        d['clear'] = variable_completer
        return NestedCompleter.from_nested_dict(d)

    def print_result(self, result):
        pt.print_formatted_text(result, style=self._output_style)
        # pt.print_formatted_text(f'{len(self.prompt_text)*" "} {result}\n')

    @staticmethod
    def _prompt_continuation(width, line_number, is_soft_wrap):
        return '.' * width

    def prompt(self):
        return self._session.prompt()
