"""
"""


class RollitException(Exception):
    """
    """


class RollitRuntimeError(RollitException):
    """
    """
    msg = None
    """ """
    codeinfo = None
    """ """

    def __init__(self, *args, codeinfo=None, **kwargs):
        self.codeinfo = codeinfo
        if args:
            self.msg = args[0]
        super().__init__(*args, **kwargs)


class ParsingError(RollitException, ValueError):
    """
    """


class InvalidReferenceError(ParsingError):
    """
    """


class TooManyItemsError(ParsingError):
    """
    """


class RollitSyntaxError(ParsingError):
    """
    """


class RollitNameError(RollitRuntimeError):
    """
    """
    name = None
    """ """

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)


class RollitReferenceError(RollitNameError, LookupError):
    """
    """

    def __init__(self, name, *args, **kwargs):
        if not args:
            args = (f'Could not find an item with the name {name}.',)
        super().__init__(name, *args, **kwargs)


class InvalidNameError(RollitNameError, LookupError):
    """
    """
    name = None
    """ """

    def __init__(self, name, *args, **kwargs):
        if not args:
            args = (f'Item name {name} is invalid.',)
        super().__init__(name, *args, **kwargs)


class NoSuchLoopError(RollitNameError, LookupError):
    """
    """

    def __init__(self, name, *args, **kwargs):
        if not args:
            args = (f'Could not find a loop with the name {name}.',)
        super().__init__(name, *args, **kwargs)


class CannotReduceError(RollitRuntimeError):
    """
    """


class RollitTypeError(RollitRuntimeError):
    """
    """


class RollitIndexError(RollitRuntimeError):
    """
    """


class NoneError(RollitRuntimeError):
    """
    """


class LibraryNotFoundError(RollitRuntimeError):
    """
    """
    name = None
    """ """

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(f'Could not locate a library named {self.name}', *args, **kwargs)
