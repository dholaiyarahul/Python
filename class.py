class Base:
    def __init__(self,val):
        self.var1=1
        self.var2=val

    def add(self):
        return (self.var1+self.var2)

a=Base(2)
print(a.add())
