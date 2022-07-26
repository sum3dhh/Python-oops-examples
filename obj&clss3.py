class dog:
    animal = "dog"

    def __init__(self,breed):
        self.breed = breed

    def setcolor(self,color):
        self.color = color

    def getcolor(self):
        return self.color

ranga = dog("husky")
ranga.setcolor("black")
print(ranga.getcolor())