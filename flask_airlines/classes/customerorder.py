"""
@author: António Brito / Carlos Bragança (2025)
#objective: class Order
"""""
# Class CustomerOrder
import datetime
from classes.customer import Customer
# Import the generic class
from classes.gclass import Gclass

class CustomerOrder(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_date','_customer_id']
    # Class header title
    header = 'Customer Order'
    # field description for use in, for example, input form
    des = ['Id','Date','Customer_id']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, date, customer_id):
        super().__init__()
        # Object attributes
        # Check the customer referential integrity
        customer_id =int(customer_id)
        if customer_id in Customer.lst:
            id = CustomerOrder.get_id(id)
            self._id = int(id)
            self._date = datetime.date.fromisoformat(date)
            self._customer_id = customer_id
            # Add the new object to the Order list
            CustomerOrder.obj[id] = self
            CustomerOrder.lst.append(id)
        else:
            print('Customer ', customer_id, ' not found')
    # Object properties
    # code property getter method
    @property
    def id(self):
        return self._id
    # date property getter method
    @property
    def date(self):
        return self._date
    # date property setter method
    @date.setter
    def date(self, date):
        self._date = date
    # customer property getter method
    @property
    def customer_id(self):
        return self._customer_id
    # customer property setter method
    @customer_id.setter
    def customer_id(self, customer_id):
        if customer_id in Customer.lst:
            self._customer_id = customer_id
        else:
            print('Customer ', customer_id, ' not found')    
            