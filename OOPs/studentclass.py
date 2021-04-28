"""
Let's create a student class which holds information about name, age, dob
"""
class student:
    
    def __init__(self,name, age, DoB):
        self.name=name # this is how object peoprties are create
        self.age= age 
        self.date_of_birth = DoB
    def display(self):
        print(f"Name of Student is: {self.name}\nAge of student is: {self.age}\n Date of birth of student is: {self.date_of_birth}")
if __name__ =="__main__":
    # creating instances 
    john = student("John",10,"15-05-2011")
    john.display()

    student("Akshay",18,"15-05-2002").display()
    # this is quite advance concept it is known as anonymous object as you can see I don't have
    # refrence to hold data type Though this is not neccessary and not recommended for beginners. 
