"""
"""

__all__ = []


class RollitNonErrorException(BaseException):
    """
    """


class LeaveException(RollitNonErrorException):
    """
    """
    __THE_EXCEPTION = None

    def __new__(cls):
        if not cls.__THE_EXCEPTION:
            cls.__THE_EXCEPTION = object.__new__(cls)
        return cls.__THE_EXCEPTION


class RestartException(RollitNonErrorException):
    """
    """
    location_specifier = name = None

    #pylint: disable=super-init-not-called
    def __init__(self, restart_obj):
        self.location_specifier, self.name = restart_obj


class OopsException(RollitNonErrorException):
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

    def reduce(self, context):
        """
        """
        value_reduced = False
        new_values = []
        for result in self:
            if not isinstance(result, (int, float)):
                result = context.reduce(result)
                value_reduced = True
            new_values.append(result)
        if not value_reduced:
            return self.value
        roll = Roll(new_values)
        # pylint: disable=protected-access
        roll._value = self._value
        return roll

    def __float__(self):
        return float(self.value)

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return f'[{", ".join(str(r) for r in self)}]'

    def map_to(self, *args):
        """
        """
        raise NotImplementedError()

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        return self.value / other

    def __floordiv__(self, other):
        return self.value // other

    def __mod__(self, other):
        return self.value % other

    def __radd__(self, other):
        return other + self.value

    def __rsub__(self, other):
        return other - self.value

    def __rmul__(self, other):
        return other * self.value

    def __rtruediv__(self, other):
        return other / self.value

    def __rfloordiv__(self, other):
        return other // self.value

    def __rmod__(self, other):
        return other % self.value


class Bag(dict):
    """
    """
    #TODO


class Modifier:
    """
    """
    __slots__ = ()
