
class MyClass:
    def greet(self): 
        # self is parameter getting passes automatically. 
        # It means context self is context of itself. 
        # of greet function
        # note: YOu can name it whatever you want, but naming is done w.r.t. it's purpose.
        return "Welcome to object oriented Programming"

#class keyword is used to create a class
if __name__ == "__main__":
# if name == main is practice followed by python community. 
    obj = MyClass()
# created instance of Myclass, this is syntax of creating instance of class
    print(obj.greet())
# To call a atriibute we can use object.instance_name / object.attrinbute_name