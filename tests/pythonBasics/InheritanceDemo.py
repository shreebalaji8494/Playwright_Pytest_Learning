from ConstructorDemo import Parent

class Child(Parent): #This class inherits from the Parent class.
    num2 = 35 #This is a class variable of the Child class.
    def __init__(self): #This is the child class constructor in which we should be calling the parent class constructor if it has any executable code.
        Parent.__init__(self, 5, 10) #Calling the parent class constructor and passing values to it.
        print("I am the Child Constructor")

    def multiplyTwoNumbers(self):
        #Accessing class variable using class name or we can use self keyword
        return self.firstnumber * self.secondnumber * Child.num2 * Parent.num  

object2 = Child() #Creating an object of the Child class which will call the child class constructor and also the parent class constructor.
print(object2.multiplyTwoNumbers()) #Calling the method on the object and printing the result.