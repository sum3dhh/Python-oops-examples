class grandfather:
    def __init__(self,grandfathername):
        self.grandfathername = grandfathername

class father(grandfather):
    def __init__(self, grandfathername,fathername):
        self.fathername = fathername

        grandfather.__init__(self,grandfathername)

class child(father):
    def __init__(self, grandfathername, fathername,childname):
        self.childname = childname
        father.__init__(self,grandfathername,fathername)
    
    def display(self):
        print("Grandfather :", self.grandfathername)
        print("Father :" , self.fathername)
        print("Child :", self.childname)

obj = child("Shubhash","Uday","Sumedh")
obj.display()
         