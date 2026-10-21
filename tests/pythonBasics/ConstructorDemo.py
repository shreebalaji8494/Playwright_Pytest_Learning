
class Parent:
    num = 10 #This is a class variable
    def __init__(self,a,b): #self keyword is mandatory in the constructor and methods of a class to refer to the instance of the class. 
        #It is used to access instance variables and methods of the class.
        self.firstnumber = a #This is an instance variable
        self.secondnumber = b #This is an instance variable
        print("I am the Parent Constructor")

    def sumOfTwoNumbers(self): #This is a method that returns the sum of two instance variables and class variable
        return self.firstnumber + self.secondnumber  + Parent.num #Accessing class variable using class name or we can use self keyword

object = Parent(5, 10) #Creating an object of the Parent class and passing values to the constructor    
print(object.sumOfTwoNumbers()) #Calling the method on the object and printing the result

object1 = Parent(15, 20) #Creating another object of the Parent class and passing values to the constructor
print(object1.sumOfTwoNumbers()) #Calling the method on the object and printing the result

#A class variable is shared among all instances of a class, while an instance variable is unique to each instance. 
# In this example, the class variable num is shared among all instances of the Parent class, while the 
# instance variables firstnumber and secondnumber are unique to each instance.