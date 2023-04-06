from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expeted period'''
    class Key:
        _slots_ = "_origin", "_dest", "_date", "_time"
        
        def __init__(self, origin, dest, date, time):
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time

        def __lt__(self, other):
            if self._origin < other._origin:
                return True
            elif self._origin == other._origin and self._dest < other._dest:
                return True
            elif self._dest == other._dest and self._date < other._date:
                return True
            elif self._date == other._date and self._time < other._time:
                return True
            else:
                return False

        def __le__(self, other):
            try:
                self_index = self._find_index(self)
                other_index = self._find_index(other)
                return self_index <= other_index
            except ValueError:
                return NotImplemented

        def __gt__(self, other):
            if self._origin > other._origin:
                return True
            elif self._origin == other._origin and self._dest > other._dest:
                return True
            elif self._dest == other._dest and self._date > other._date:
                return True
            elif self._date == other._date and self._time > other._time:
                return True
            else:
                return False

        def __ge__(self, other):
            if self == other:
                return True
            else:
                return self.__gt__(other)

    def query(self, k1, k2):
        if k1[0] is not k2[0] or k1[1] is not k2[1]:
            raise KeyError("The origin or the destination are not the same")
        else:
            k1_key = self.Key(k1[0], k1[1], k1[2], k1[3])
            k2_key = self.Key(k2[0], k2[1], k2[2], k2[3])

            for key, value in a:
                if (key._date == k1_key._date and key._time == k1_key._time) or \
                    (key._date == k2_key._date and key._time == k2_key._time) or \
                    (key._date == k1_key._date and key._time > k1_key._time) or \
                    (key._date > k1_key._date and key._date < k2_key._date) or \
                    (key._date == k2_key._date and key._time < k2_key._time):
                        print(key._origin, key._dest, key._date, key._time, value)
                

a = FlightQuery()
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1330, "No2"), ("A", "B", 622, 1300, "No3"), ("A", "B", 722, 1300, "No4"), ("A", "B", 922, 1500, "No5"), ("A", "B", 322, 1200, "No6")]
for each in s:
    key = a.Key(each[0], each[1], each[2], each[3])
    value = each[4]
    a[key] = value
print(len(a))

example_origin = "A"

# Print Flight Query
print("Initialization", "\n")
for key, value in a:
    print(key._origin, key._dest, key._date, key._time, value)
print("\n")


# Query
k1 = ("A", "B", 822, 1200)
k2 = ("A", "B", 722, 1430)

print("Input", "\n")
print("Earliest date:", k1[2])
print("Earliest time:", k1[3])
print("Latest date:", k2[2])
print("Latest time:", k2[3], "\n")

print("Possible Flights:", "\n")
a.query(k1, k2)


