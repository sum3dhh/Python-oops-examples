

class spies:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)


class mini(spies):
    def many(self):
        print("my work is hard;-;")


obj = mini("sumedh", 214021)
obj.display()
obj.many()
