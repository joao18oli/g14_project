"""
@author: António Brito / Carlos Bragança (2025)
#objective: class Product
"""""
# Class Product
# Import the generic class
from classes.gclass import Gclass

class Product(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_name','_price','_stock']
    # Class header title
    header = 'Product'
    # field description for use in, for example, input form
    des = ['Id','Name','Price','Stock']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, name, price, stock):
        super().__init__()
        # Object attributes
        id = Product.get_id(id)
        self._id = id
        self._name = name
        self._price = float(price)
        self._stock = int(stock)
        # Add the new object to the Product list
        Product.obj[id] = self
        Product.lst.append(id)
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # name property getter method
    @property
    def name(self):
        return self._name
    # price property getter method
    @property
    def price(self):
        return self._price
    # price property setter method
    @price.setter
    def price(self, price):
        self._price = price
    # stock property getter method
    @property
    def stock(self):
        return self._stock
    # stock property setter method
    @stock.setter
    def stock(self, stock):
        self._stock = stock
