"""
"""
import pathlib

import appdirs
import prompt_toolkit as pt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import style_from_pygments_cls
from pygments.styles import get_style_by_name

from .base import BaseRepl
from ..language_ref import KEYWORDS
from ..extra.pygments import RollitLexer

__all__ = []

cachedir = pathlib.Path(appdirs.user_cache_dir('rollit')) / 'repl'
cachedir.mkdir(parents=True, exist_ok=True)


class PrettyRepl(BaseRepl):
    """
    """

    _completer = WordCompleter(
        list(KEYWORDS) + ['?', '#', '!', '~'] +
        ['except when', 'but if', 'but always', 'occurrs then'])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._output_style = None
        self._session = pt.PromptSession(
            message=self.prompt_text,
            history=FileHistory(cachedir / 'history.txt'),
            editing_mode=getattr(pt.enums.EditingMode, self.options.edit_mode.upper()),
            auto_suggest=AutoSuggestFromHistory(),
            enable_open_in_editor=True,
            completer=self._completer,
            multiline=self.options.multiline,
            style=style_from_pygments_cls(get_style_by_name(self.options.style)),
            prompt_continuation=self._prompt_continuation,
            lexer=pt.lexers.PygmentsLexer(RollitLexer, sync_from_start=True),
            search_ignore_case=True,
        )

    def print_result(self, result):
        pt.print_formatted_text(result, style=self._output_style)
        # pt.print_formatted_text(f'{len(self.prompt_text)*" "} {result}\n')

    @staticmethod
    def _prompt_continuation(width, line_number, is_soft_wrap):
        return '.' * width

    def prompt(self):
        return self._session.prompt()
