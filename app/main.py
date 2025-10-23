class Distance:
    def __init__(self, km):
        if not isinstance(km, (int, float)):
            raise TypeError("Distance must be a number")
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    @staticmethod
    def _get_km(value):
        if isinstance(value, Distance):
            return value.km
        if isinstance(value, (int, float)):
            return value
        return NotImplemented

    def __add__(self, other):
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return Distance(self.km + km)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        self.km += km
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        if isinstance(other, Distance):
            raise TypeError("Multiplication by Distance is not supported")
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Distance(self.km / other)
        if isinstance(other, Distance):
            raise TypeError("Division by Distance is not supported")
        return NotImplemented

    def __rtruediv__(self, other):
        return NotImplemented

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
