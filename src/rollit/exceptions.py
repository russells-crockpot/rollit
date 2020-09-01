"""
"""


class RollitException(Exception):
    """
    """


class RollitRuntimeError(RollitException):
    """
    """


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


class RollitReferenceError(RollitException, LookupError):
    """
    """


class InvalidNameError(RollitException, LookupError):
    """
    """


class NoSuchLoopError(RollitException, LookupError):
    """
    """

    def __init__(self, loop_name, *args, **kwargs):
        self.loop_name = loop_name
        super().__init__(f'Loop {self.loop_name} either doesn\'t exist or is out of scope.', *args,
                         **kwargs)


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
