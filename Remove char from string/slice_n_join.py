# if __name__=="__main__":
#     str1 = "Python"
#     print ("Original string: " + str1) 
#     # remove at index 2
#     str1 = str1[:2]+str1[3:]
#     # as in range [a:b] b is excluded and associativity is from left to right
#     # we can take advantage of this methods.
#     print ("String after removal of character: " + str1) 

if __name__ == "__main__":
    str1="String"
    # str1[start index: end index(Not exluded): gap number]
    print(str1[::-1])  # will print reverse 
    print(str1[::2]) # if nothing given , it will take whole string with gap of 2, exclduing charecters
    print(str1[:3:-1]) # reverses string in 1 to 3 index
    """
    # output:
    gnirtS
    Srn
    gn"""