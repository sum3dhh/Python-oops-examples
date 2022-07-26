class parent:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("my name is ", self.name)

obj = parent("sumedh")
obj.display()