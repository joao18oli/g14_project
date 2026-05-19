"""
@author: António Brito / Carlos Bragança (2025)
#objective: class Customer_login
"""
# Class Customer_login
# Import the generic class
from classes.gclass import Gclass

class Customer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_name','_address','_phone']
    # Class header title
    header = 'Persons'
    # field description for use in, for example, input form
    des = ['Id','Name','Address','Phone']
    # Constructor: Called when an object is instantiated
    def __init__(self,id,name,address,phone):
        super().__init__()
        # Object attributes
        id = Customer.get_id(id)
        self._id = id
        self._name = name
        self._address = address
        self._phone = phone
        # Add the new object to the Customer's list
        Customer.obj[id] = self
        Customer.lst.append(id)
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # name property getter method
    @property
    def name(self):
        return self._name
    # name property setter method
    @name.setter
    def name(self, name):
        self._name = name
    # address property getter method
    @property
    def address(self):
        return self._address
    # address property setter method
    @address.setter
    def address(self, address):
        self._address = address
    # phone property getter method
    @property
    def phone(self):
        return self._phone
    # phone property setter method
    @phone.setter
    def phone(self, phone):
        self._phone = phone
