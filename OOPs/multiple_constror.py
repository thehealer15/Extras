class MyClass:
    def __init__(self):
        print("First Constructor")
    def __init__(self, age):
        print(f"Seoncd Constructor {age}")

if __name__ =="__main__" :
    a = MyClass()
    b= MyClass(2)

    