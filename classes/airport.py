#classe realizada por Maria Carvalho
from classes.gclass import Gclass
class Airport(Gclass):
    obj=dict()
    lst=list()
    pos=0
    sortkey=''
    att=['_id', '_build_date', '_name']
    header='Airport'
    des=['Id', 'Build Date', 'Name']
    def __init__(self, id, build_date, name):
        super().__init__()
        id=Airport.get_id(id)
        self._id=int(id)
        self._build_date= build_date
        self._name=name
        Airport.obj[id]=self
        Airport.lst.append(id)
    @property
    def id(self):
        return self._id
    @property
    def build_date(self):
        return self._build_date
    @build_date.setter
    def build_date(self, build_date):
        self._build_date= build_date
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name=name


