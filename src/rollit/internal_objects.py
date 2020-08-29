"""
"""

__all__ = []


class LeaveException(BaseException):
    """
    """
    __THE_EXCEPTION = None

    def __new__(cls):
        if not cls.__THE_EXCEPTION:
            cls.__THE_EXCEPTION = object.__new__(cls)
        return cls.__THE_EXCEPTION


class RestartException(BaseException):
    """
    """
    location_specifier = name = None

    #pylint: disable=super-init-not-called
    def __init__(self, restart_obj):
        self.location_specifier, self.name = restart_obj


class OopsException(BaseException):
    """
    """

    #pylint: disable=super-init-not-called
    def __init__(self, value):
        self.value = value


class Roll(list):
    """
    """

    def __init__(self, results):
        super().__init__(results)
        self._value = None

    @property
    def total(self):
        """
        """
        return sum(int(i) for i in self)

    @property
    def value(self):
        """
        """
        if self._value is None:
            return self.total
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __int__(self):
        return self.value

    def __str__(self):
        return f'{type(self).__name__}{super().__str__()}'

    def __repr__(self):
        return f'{type(self).__name__}{super().__repr__()}'
