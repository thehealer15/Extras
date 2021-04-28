class Student:
  
    # Initializing
    def __init__(self):
        print('Student created.')
        # though it's not recommended to use print statements in
        # construcor in destrucor. 

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
  
obj = Student()
del obj # here destructor is called