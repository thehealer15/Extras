# Using replace method:
"""
syntax:
    stringName.replace(old charecter , new charecter, how many should removed) 
    3rd argument is option , if not specified it will remove all charecters
"""
if __name__ =="__main__":
    str1 = "Python Programming"
    # remove one or all occrences of  n by using replace method. 

    print(str1.replace('n','',2))
    print("--")
    print(str1) # To let you know, .replace returns string, not updates the original string.
    