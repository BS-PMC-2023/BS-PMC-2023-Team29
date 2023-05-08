class User:
    def __init__(self):
        self.id = None
        self.email = None
        self.password = None
        self.type= 1
        self.name = None
        self.lastname = None

    def insert(self,email,password,name,lastname,type =1):
        self.id = None
        self.email = email
        self.password = password
        self.type= 1
        self.name = name
        self.lastname = lastname

    def tupple_insert(self, tupple_insert):
        self.id = tupple_insert[0]
        self.email = tupple_insert[1]
        self.password = tupple_insert[2]
        self.type= tupple_insert[3]
        self.name = tupple_insert[4]
        self.lastname = tupple_insert[5]

    def totuple(self):
        if not self.id:
            return (self.email, self.password,self.type,self.name,self.lastname)
        else :
            return (self.id,self.email, self.password, self.type, self.name, self.lastname)

    def __str__(self):
        return str(self.totuple())

class supply:
    def __init__(self):
        self.id = None
        self.type= None
        self.name = None
        self.all_units = None
        self.available_units = None

    def insert(self,id,type,name,all_units,available_units ):
        self.id = id
        self.type = type
        self.name = name
        self.all_units = all_units
        self.available_units = available_units

    def tupple_insert(self, tupple_insert):
        self.id = tupple_insert[0]
        self.name = tupple_insert[1]
        self.all_units = tupple_insert[2]
        self.available_units = tupple_insert[3]
        self.type = tupple_insert[4]

    def borrow(self,how_much_items):
        if self.available_units - how_much_items >= 0:
            return True
        return False

    def totuple(self):
        return (self.id, self.name,self.all_units,self.available_units,self.type)

    def __str__(self):
        return str(self.totuple())