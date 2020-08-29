"""
"""


class RollItException(Exception):
    """
    """


class RollItRuntimeError(RollItException):
    """
    """


class ParsingError(RollItException, ValueError):
    """
    """


class InvalidReferenceError(ParsingError):
    """
    """


class TooManyItemsError(ParsingError):
    """
    """


class RollItSyntaxError(ParsingError):
    """
    """


class RollitReferenceError(RollItException, LookupError):
    """
    """


class InvalidNameError(RollItException, LookupError):
    """
    """


class NoSuchLoopError(RollItException, LookupError):
    """
    """

    def __init__(self, loop_name, *args, **kwargs):
        self.loop_name = loop_name
        super().__init__(f'Loop {self.loop_name} either doesn\'t exist or is out of scope.', *args,
                         **kwargs)


class CannotReduceError(RollItRuntimeError):
    """
    """


class RollItTypeError(RollItRuntimeError):
    """
    """


class RollitIndexError(RollItRuntimeError):
    """
    """


class NoneError(RollItRuntimeError):
    """
    """
