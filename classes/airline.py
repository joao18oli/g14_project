# -*- coding: utf-8 -*-
#Rodrigo Paiva's class
"""
Created on Tue Apr  7 11:41:01 2026

@author: joaof
"""

from classes.gclass import Gclass

class Airline(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id','_denomination','_classe']
    header = 'Airline'
    des = ['Id','Denomination','Classe']
    def __init__(self, id, denomination, classe):
        super().__init__()
        # Object attributes
        id = Airline.get_id(id)
        self._id = int(id)
        self._denomination = denomination
        self._classe = classe
        Airline.obj[id] = self
        Airline.lst.append(id)
    @property
    def id(self):
        return self._id
    @property
    def denomination(self):
        return self._denomination
    @denomination.setter
    def denomination(self, denomination):
        self._denomination = denomination
    @property
    def classe(self):
        return self._classe
    @classe.setter
    def classe(self, classe):
        self._classe = classe
