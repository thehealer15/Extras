# Animal will be parent class -> dog in inheriting animal class -> dog child inheriting dog class
# this is known as multi level inheritance
class Animal:  
    def speak(self):  
        print("Animal class Speaking")  
     
class Dog(Animal):  
    def bark(self):  
        print("Barking")  
        
class DogChild(Dog):  
    def sleep(self):  
        print("Sleeping  ")  

if __name__ =="__main__":
    obj = DogChild()  
    obj.bark()  
    obj.speak()  
    obj.sleep() 

    