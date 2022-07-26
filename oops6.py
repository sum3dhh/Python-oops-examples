class base1:
    def __init__(self):
        self.str1 = " sumedh"
        print("base1")


class base2(base1):
    def __init__(self):
        self.str2 = "aditya"
        print("base2")
    

class Derived( base2 ):

    def __init__(self): 
        base1.__init__(self)
        base2.__init__(self)
        print("Combined")
    def prnts(self):
        print(self.str1,self.str2)


obj = Derived()
obj.prnts()

