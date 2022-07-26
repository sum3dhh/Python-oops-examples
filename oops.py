class Addition:
    num1 = 0
    num2 = 0
    ans = 0

    def __init__(self,n1,n2):
        self.num1 = n1
        self.num2 = n2
        

    def Display(self):
        print("First number :" + str(self.num1))
        print("Second number :" + str(self.num2))
        print(" Sum of both numbers : " + str(self.ans))

    def calculations(self):
        self.ans = self.num1 + self.num2
        return self.ans

math = Addition(347,467)
math.calculations()
math.Display()