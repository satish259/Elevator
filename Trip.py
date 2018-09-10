class Trip(object):
    """represents one elevator trip
    code from https://raw.githubusercontent.com/mxvanzant/pyelevator/master/elevator.py
    """
    def __init__(self, trip): 
        items = trip.split('-') 
        self.startFloor = int(items[0]) 
        self.endFloor = int(items[1]) 
        if self.startFloor < self.endFloor: 
            self.direction = 'up' 
        else: 
            self.direction = 'down' 


