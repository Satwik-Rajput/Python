class twoDvectoe():
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The resultant vector is: {self.i}i+{self.j}j")


class threeDvectoe(twoDvectoe):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"The resultant vector is: {self.i}i+{self.j}j+{self.k}k")

a= twoDvectoe(3,4)
a.show()
b=threeDvectoe(7,4,5)
b.show()