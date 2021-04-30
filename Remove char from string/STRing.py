
if __name__ == "__main__":
    # How string are created. 
    string1 = "This is String 'in double inverted'"
    string2 = 'This is Also a "string" '
    string3 = """Multiline string should be used inside three times double/single inverted comma"""

    print(f"String 1: {string1}")
    print(f"String 2: {string2}")
    print(f"String 3: {string3}")
    # Output:
    #String 1 : This is String 'in double inverted'
    # String 2: This is Also a "string" 
    # String 3: Multiline string should be used inside three times double/single inverted comma
    # Remeber how variables are stored?
    # comiler/interpriter have a hashMap like data structure which allows searching O(1)
    # That's why you can't create varible with same name(In other languages) python simply overrites they 
    # value. In hashMap, memory location of value/literal is stored with name. 