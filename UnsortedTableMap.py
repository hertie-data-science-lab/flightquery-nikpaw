from MapBase import *


class UnsortedTableMap(MapBase):
    def __init__(self):
        # initializes empty _table list
        self._table = []

    def __len__(self):
        # returns the length of the _table list
        return len(self._table)

    def _findkey(self, key):
        # searches _table list for object with matching key
        # helper function, see getitem etc. defined below
        for i in range(len(self)):
            if key == self._table[i]._key:
                return i
        return None

    def __setitem__(self, key, value):
        # sets a new key-value pair
        i = self._findkey(key)
        if i is not None:
            # if key is in list, value is updated to the new value
            self._table[i]._value = value
        else:
            # if key is not in list,key-value pair added to end of list
            self._table.append(self._Item(key, value))

    def __getitem__(self, item):
        # find the index of the _Item object with the given key
        # uses findkey defined above
        i = self._findkey(item)
        if i is None:
            raise KeyError(item)
        else:
            return self._table[i]._value

    def __delitem__(self, key):
        # deletes key-value pair
        # uses findkey defined above
        i = self._findkey(key)
        if i is None:
            raise KeyError(key)
        else:
            del self._table[i]

    def __iter__(self):
        for item in self._table:
            yield item._key


if __name__ == "__main__":
    # instance of the UnsortedTableMap class?
    # why as an if?
    a = UnsortedTableMap()
    a[1] = 1
    a[2] = 2
    a['a'] = 'a'
    a[3] = 3
    a[4] = 4
    print(len(a))
    for i in a:
        print(i, a[i])

    del a[1]
    print(len(a))
    for i in a:
        print(i, a[i])
