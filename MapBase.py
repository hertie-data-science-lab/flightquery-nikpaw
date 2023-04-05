class MapBase:  # basic map class
    class _Item:  # innerclass, contains flights
        __slots__ = "_key", "_value"  # what does __slots__ do?
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):  # compare two _Item objects based on keys
            return str(self._key) < str(self._value)

        def __str__(self):  # returns string of _Item
            return "{0} : {1}".format(self._key, self._value)