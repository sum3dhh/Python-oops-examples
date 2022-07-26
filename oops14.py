from datetime import date

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def birthyr(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def ifadult(age):
        return age > 18

person_1 = person("sumedh",4)
person_2 = person.birthyr("sumedh",2006)

print(person_1.age)
print(person_2.age)
print(person.ifadult(23))