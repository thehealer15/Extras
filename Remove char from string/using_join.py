"""
Join method :
lis1 = ['P','Y','T','O','N']
    s = "==" 
    s = s.join(lis1) 
    print(s,type(s))
    # output :
    #P==Y==T==O==N <class 'str'>
To Concatenate any number of strings.
The string whose method is called is inserted in between each given string. 
The result is returned as a new string
"""

if __name__ =="__main__":
    str1 = "Python"
    print("Original string: " + str1) 
    
    # Removing char at index 2 
    # using join() + list comprehension 
    result_str = ''.join([str1[i] for i in range(len(str1)) if i != 2])
    # quite same as brute force method. But using join, we are not creating multiple strings. 
    # As join is pure concatenating methdo. 
    
    
  
    print ("String after removal of character: " + result_str) 