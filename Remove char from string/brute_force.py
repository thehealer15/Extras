if __name__ =="__main__":
    str1 = "Python" # string created. 
    result = "" # this will hold out result.
    # remove P from str1
    for i in str1:
        if(i!="P"):
            result+= i
    
    print(result) #output ython
    # Position based.
    # remove charecter at 3rd index.

    result =""
    for i in range(len(str1)):
        if( i !=3 ):
            result+=str1[i]
    print(result ) # output Pyton
    """
    Drawback:
    String are immuatble in python
    so in strp result += i we are creating length(str1) -1 new strings 
    This can lead to memory consumption for high length strings. 
    """