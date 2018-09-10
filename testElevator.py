import Elevator
import traceback

def testElevator(opMode, fileName):
    """ module to load data from file and run elevator for testing
    """
    if opMode.lower() != 'a' and opMode.lower() != 'b':
        raise Exception('Incorrect operation node ' + opMode + '. a and b are the only valid modes.')
    else:
        try:
            with open(fileName,'r') as openFl:
                for trips in openFl.read().splitlines():
                    elevator=Elevator.Elevator(opMode,trips.split(':')[0],trips.split(':')[1])
        except IOError:
             raise Exception('Could not read file:', openFl)
        except Exception as e: # catch all errors
             raise Exception(traceback.format_exc())
