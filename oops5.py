class student:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)
    
class info(student):
    def __init__(self, name, id,hobby,town) -> None:
        self.hobby = hobby
        self.town = town

        super().__init__(name, id)


obj = info("sumedh", 214021, "coding", "pune")
obj.display()










