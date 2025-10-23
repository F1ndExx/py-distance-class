class Distance:
    def __init__(self, km):
        if not isinstance(km, (int, float)):
            raise TypeError("Distance must be a number")
        self.km = km

    # String representations
    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    # Internal helper
    @staticmethod
    def _get_km(value):
        if isinstance(value, Distance):
            return value.km
        if isinstance(value, (int, float)):
            return value
        return NotImplemented

    # Addition
    def __add__(self, other):
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return Distance(self.km + km)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        self.km += km
        return self

    # Multiplication
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        if isinstance(other, Distance):
            raise TypeError("Multiplication by Distance is not supported")
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    # True division
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Distance(round(self.km / other, 2))
        if isinstance(other, Distance):
            raise TypeError("Division by Distance is not supported")
        return NotImplemented

    def __rtruediv__(self, other):
        raise TypeError("Cannot divide number by Distance")

    # Comparisons
    def __eq__(self, other):
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km == km

    def __lt__(self, other):
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km < km

    def __le__(self, other):
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km <= km

    def __gt__(self, other):
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km > km

    def __ge__(self, other):
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km >= km
