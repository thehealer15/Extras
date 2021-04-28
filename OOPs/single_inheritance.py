class Base:
    x=10
    cnt=0
    def __init__(self):
        print("Cnostructor is called")

    def display(self):
        print("Value of X is: "+str(x))
    
class childClass(Base):
    x =15
    y=20
    def __init__(self):
        print("Child Constuctor")
    def display(self):
        print(f"Value of X: {self.x}\nValue of y: {self.y}")

if __name__ =="__main__":
    obj = childClass()
    obj.display()