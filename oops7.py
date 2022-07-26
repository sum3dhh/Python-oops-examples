class child1:
    def __init__(self,name):
        self.name = name
    
    def getname(self):
        return self.name


class child2(child1):
    def __init__(self, name,age):
        self.age = age

        child1.__init__(self,name)
    def getage(self):
        return self.age
class grandchild(child2):
    def __init__(self, name, age,address):
        self.address = address
        child2.__init__(self,name, age)
    def getaddress(self):
        return self.address

obj = grandchild("sumedh",21,"pune")
print(obj.getname(),obj.getage(),obj.getaddress())
        