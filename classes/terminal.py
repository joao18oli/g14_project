# Class Terminal

from classes.airport import Airport
# Import the generic class
from classes.gclass import Gclass

class Terminal(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_notes','_airport_id']
    # Class header title
    header = 'Terminal'
    # field description for use in, for example, input form
    des = ['Id','Notes','Airport_id']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, notes, airport_id):
        super().__init__()
        # Object attributes
        # Check the airport referential integrity
        airport_id = int(airport_id)
        if airport_id in Airport.lst:
            id = Terminal.get_id(id)
            self._id = int(id)
            self._notes = notes
            self._airport_id = airport_id
            # Add the new object to the Terminal list
            Terminal.obj[id] = self
            Terminal.lst.append(id)
        else:
            print('Airport ', airport_id, ' not found')
    # Object properties
    # code property getter method
    @property
    def id(self):
        return self._id
    # notes property getter method
    @property
    def notes(self):
        return self._notes
    # notes property setter method
    @notes.setter
    def notes(self, notes):
        self._notes = notes
    # airport_id property getter method
    @property
    def airport_id(self):
        return self._airport_id
    # airport_id property setter method
    @airport_id.setter
    def airport_id(self, airport_id):
        airport_id = int(airport_id)
        if airport_id in Airport.lst:
            self._airport_id = airport_id
        else:
            print('Airport ', airport_id, ' not found')    
            