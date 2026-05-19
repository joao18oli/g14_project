"""
@author: António Brito / Carlos Bragança (2025)
#objective: class OrderProduct
"""""
# Class OrderProduct
from classes.customerorder import CustomerOrder
from classes.product import Product
# Import the generic class
from classes.gclass import Gclass

class OrderProduct(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier id, attribute must be the first on the list
    att = ['_id', '_order_id','_product_id','_quantity','_price']
    # Class header title
    header = 'Order lines'
    # field description for use in, for example, input form
    des = ['Id','Order_id','Product_id','Quantity','Price']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, order_id, product_id, quantity, price):
        super().__init__()
        # Object attributes
        # Check the order and product referential integrity
        order_id = int(order_id)
        product_id = int(product_id)
        if order_id in CustomerOrder.lst:
            if product_id in Product.lst:
                id = OrderProduct.get_id(id)
                self._id = id
                self._order_id = order_id
                self._product_id = product_id
                self._quantity = float(quantity)
                self._price = float(price)
                # Add the new object to the OrderProduct list
                OrderProduct.obj[id] = self
                OrderProduct.lst.append(id)
            else:
                print('Product ', product_id, ' not found')
        else:
            print('Order ', order_id, ' not found')
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # order property getter method
    @property
    def order_id(self):
        return self._order_id
    # product property getter method
    @property
    def product_id(self):
        return self._product_id
    # quantity property getter method
    @property
    def quantity(self):
        return self._quantity
    # quantity property setter method
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = float(quantity)
    # price property getter method
    @property
    def price(self):
        return self._price
    # price property setter method
    @price.setter
    def price(self, price):
        self._price = float(price)
        