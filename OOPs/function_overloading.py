class Point:
    # initializing 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    # If you print point object and you want your code rather than custom memory location/ python
    # decided output, overload this method. 

    # OverLoading ' < ' i.e. less than method. 
    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

class Print:
    pass

class custome_print:
    def __str__(self):
        return "Python is Great to learn "
if __name__ =="__main__":
    p1 = Point(6,1)
    p2 = Point(2 ,-3)
    p3 = Point(-1,12)

    # use less than 
    print(p1<p2)
    print(p2<p3)
    print(p1<p3)
    print(p1,p2,p3)
    obj1 = Print()
    obj2 = custome_print()

    print(f"__str__ overlaoded: {obj1}")
    print(f"__str__ not overloaded: {obj2}")