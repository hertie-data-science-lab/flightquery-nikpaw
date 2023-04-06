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
            if self == other:
                return True
            else:
                return self.__lt__(other)

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
        k1_key = self.Key(k1[0], k1[1], k1[2], k1[3])
        k2_key = self.Key(k2[0], k2[1], k2[2], k2[3])
        
        flight_from_origin = 0
        flight_to_destination = 0
        possible_origins = []
        possible_destinations = []

        for key, value in a:
            if key._origin == k1_key._origin:
                flight_from_origin += 1
            if key._dest == k1_key._dest:
                flight_to_destination += 1
            if key._origin not in possible_origins:
                possible_origins.append(key._origin)
            if key._dest not in possible_destinations:
                possible_destinations.append(key._dest)

        if flight_from_origin == 0:
            print("\n", "No flight from this origin. Please enter a new destination from the following options: ", possible_origins)
        if flight_to_destination == 0:
            print("\n", "No flight to this destination. Please enter a new destination from the following options: ", possible_destinations)
        else:
            print("\n", "Possible Flights:", "\n")
            for key, value in a:
                if (key._date == k1_key._date and key._time == k1_key._time) or \
                    (key._date == k2_key._date and key._time == k2_key._time) or \
                    (key._date == k1_key._date and key._time > k1_key._time) or \
                    (key._date > k1_key._date and key._date < k2_key._date) or \
                    (key._date == k2_key._date and key._time < k2_key._time):
                        print("Flight", value, "from", key._origin, "to", key._dest, "on", key._date, "at", key._time)

a = FlightQuery()
s = [("C", "B", 622, 1200, "No1"), ("A", "B", 622, 1330, "No2"), ("A", "B", 622, 1300, "No3"), ("A", "B", 623, 1300, "No4"), ("A", "B", 621, 1500, "No5"), ("A", "B", 625, 1200, "No6")]
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


# Query Input
print("Welcome to FlightQuery!:) \n Please start you query. \n")
origin = input("Flight Origin: ")
destination = input("Flight Destination: ")
earliest_date = int(input("Earliest Date: "))
earliest_time = int(input("Earliest Time: "))
latest_date = int(input("Latest Date: "))
latest_time = int(input("Latest time: "))

k1 = (origin, destination, earliest_date, earliest_time)
k2 = (origin, destination, latest_date, latest_time)

# Query Output
a.query(k1, k2)


