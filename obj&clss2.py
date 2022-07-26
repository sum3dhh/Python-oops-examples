class dog:
    animal = 'dog'

    def __init__(self,breed,color):
        self.breed = breed
        self.color = color

tyson = dog("dobberman", "brown")
ronnie = dog("husky","white")

print("Tyson details :")
print(" animal :", tyson.animal)
print("breed :" , tyson.breed)
print("color :", tyson.color)
print("Ronnie details :")
print(" animal :", ronnie.animal)
print("breed :" , ronnie.breed)
print("color :", ronnie.color)