# Marta's class
# Class Voo
from classes.airport import Airport
from classes.airline import Airline
# Import the generic class
from classes.gclass import Gclass


class Voo(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier id, attribute must be the first on the list
    att = ['_id', '_airline_id', '_airport_id', '_flight_date', '_ticket_cost']
    header = 'Voo'
    # field description for use in, for example, input form
    des = ['Id', 'Airline_id','Airport_id','Flight_date','Ticket_cost']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, airline_id, airport_id, flight_date, ticket_cost):
        super().__init__()
        # Object attributes
        # Check the order and product referential integrity
        airport_id = int(airport_id)
        airline_id = int(airline_id)
        
        if airport_id in Airport.lst:
            if airline_id in Airline.lst:
                id = Voo.get_id(id)
                self._id = int(id)
                self._flight_date = str(flight_date)
                self._ticket_cost = int(ticket_cost)
                self._airport_id = int(airport_id)
                self._airline_id = int(airline_id)
                
                # Add the new object to the Voo list
                Voo.obj[id] = self
                Voo.lst.append(id)
            else:
                print('Airline ', airline_id, ' not found')
        else:
            print('Airport ', airport_id, ' not found')
                
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # airport property getter method
    @property
    def airport_id(self):
        return self._airport_id
    
    # airport property setter method           
    @airport_id.setter
    def airport_id(self, airport_id):
        airport_id = int(airport_id)
        if airport_id in Airport.lst:
            self._airport_id = airport_id
        else:
            print('Airport ', airport_id, ' not found')        
        
    # airline property getter method
    @property
    def airline_id(self):
        return self._airline_id

    # airline property setter method
    @airline_id.setter
    def airline_id(self, airline_id):
        airline_id = int(airline_id)
        if airline_id in Airline.lst:
            self._airline_id = airline_id
        else:
            print('Airline ', airline_id, ' not found') 
    
    # flight_date property getter method
    @property
    def flight_date(self):
        return self._flight_date

    # flight_date property setter method
    @flight_date.setter
    def flight_date(self, flight_date):
        self._flight_date = str(flight_date)
    
    # ticket_cost property getter method
    @property
    def ticket_cost(self):
        return self._ticket_cost

    # ticket_cost property setter method
    @ticket_cost.setter
    def ticket_cost(self, ticket_cost):
        self._ticket_cost = int(ticket_cost)
    


