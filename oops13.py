from unicodedata import name


class CSEstudent:
    stream = "CSE"

    def __init__(self, name, id):
        self.name = name
        self.id = id


a = CSEstudent("sumedh", 214021)
b = CSEstudent("aditya", 214011)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.id)
print(b.id)

a.stream = "B.tech"
print(a.stream)
print(b.stream)

CSEstudent.stream = "M.tech"
print(a.stream)
print(b.stream)
