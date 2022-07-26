class mother:
    mothername = ""

    def mothern(self):
        print(self.mothername)
class father:
    fathername = ""

    def fathern(self):
        print(self.fathername)

class child(mother,father):
    def parent(self):
        print("MOTHER NAME: ", self.mothername)
        print("FATHER NAME: ", self.fathername)

obj = child()
obj.fathername = " Uday"
obj.mothername = " Sarika"
obj.parent()