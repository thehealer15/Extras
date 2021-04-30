
if __name__ =="__main__":
    str1 = 'ABCDEF_PYTHON_ABCD_PYTHON'    
    print(str1.translate({ord(i): None for i in 'PYTHON'}))
#  If "PYTHON" found, put it's value as none i.e. don't put anything
"""
# Syntax #:
  string.translate(mapping)
  mapping – a dictionary(key value pair) having mapping between two characters. . 
   translate() returns a string that is modified string of givens string according to given translation mappings.
   Replace each character in the string using 
   the given translation table.
   table Translation table, which must be a mapping of Unicode ordinals to 
   Unicode ordinals, strings, or None.

"""