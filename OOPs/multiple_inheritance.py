class A:
    def __init__(self):
       pass
class B:
    def __init__(self):
        pass
class C: 
    def __init__(self):
        pass
class D:
    def __init__(self):
        pass
class E:
    def __init__(self):
        pass

class final(A,B,C,D,E):
    def __init__(self):
        print("This is final class")

if __name__ =="__main__":
    obj = final()
    