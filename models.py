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
