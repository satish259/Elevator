class Transit(object):
    """ represents a series of trips that are all in the same direction
    combined into a series of unique ordered floor stops.
    code from https://raw.githubusercontent.com/mxvanzant/pyelevator/master/elevator.py
    The modelling of transits where the floors are sorted list made the biggest leap towards resolving this. 
    I may not have stumbles across this solution otherwise
    """
    def __init__(self):
        self.direction = None
        self._values = set()

    def added(self, trip):
        if self.direction == None or self.direction == trip.direction:
            self.direction = trip.direction
            self._values.add(trip.startFloor)
            self._values.add(trip.endFloor)
            return True
        return False

    def floors(self):
        temp = []
        temp.extend(self._values)
        if self.direction == 'up':
            temp.sort()
        else:
            temp.sort(reverse=True)
        return temp
