import Trip
import Transit

class Elevator(object):
    """ a model Elevator that oeprates on two modes:
        mode a is single person in elevator at any times and each journey deemed a trip
        mode b where mutliple persons could be in elevator based on trips deemed transit
    """

    def __init__(self, opMode, currFloor, calls): 
        "Initialise elevator class with reused variables"
        self.currFloor=int(currFloor)
        self.distance=0
        route=[]
        route.append(int(currFloor))
        self.route=route
        if opMode.lower() == 'a':
            self.journey=self.modeA(calls)
        elif opMode.lower() == 'b':
            self.journey=self.modeB(calls)
        else:
            raise Exception('Incorrect operation node ' + str(opMode) + '. a and b are the valid modes.')
        self.displayJourneys()

    def modeA(self,calls):
        "mode a is single person in elevator at any times and each journey deemed a trip"
        trips=initTrips(calls)
        for trip in trips:
            if self.currFloor != trip.startFloor:
                self.endFloor = self.move(self.currFloor, trip.startFloor)
            self.currFloor = self.move(trip.startFloor, trip.endFloor)
        self.route.append('(%s)' % self.distance)

    def modeB(self, calls):
        "mode b where mutliple persons could be in elevator based on trips deemed transit"
        transits=initTransits(calls)
        for transit in transits:
            floors = transit.floors()
            for floor in floors:
                if floor != self.currFloor:
                    self.currFloor=self.move(self.currFloor, floor)
        self.route.append('(%s)' % self.distance)

    def displayJourneys(self):
        "display journeys of elevator with each floor visited and distance covered as number of floors in brackets"
        print(' '.join([str(item) for item in self.route]))

    def move(self, startFloor, endFloor):
        "moves elevator from start to end floor and tracks the distance travelled"
        if self.route[-1]!=startFloor: self.route.append(startFloor) # if lift was moved to starting floor, it needs to appear just once
        self.route.append(endFloor)
        self.distance +=  abs(startFloor - endFloor)
        return endFloor

def initTrips(calls):
    "initialises trips deemed single journeys"
    trips = []
    items = calls.split(',')
    for item in items:
        trips.append(Trip.Trip(item))
    return trips

def initTransits(calls):
    "initialises transits which is a collection of trips"
    trips=initTrips(calls)
    transits = []
    transit = Transit.Transit()
    transits.append(transit)
    for trip in trips:
        if transit.added(trip):
            continue
        transit = Transit.Transit()
        transits.append(transit)
        transit.added(trip)
    return transits