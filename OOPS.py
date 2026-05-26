# To reduce redundancy and increase reusability
class Student: # creating class
    college_name = "IIT Delhi" # a class instance
    def __init__(self, fullname, marks):
        self.name = fullname # name, marks is variable inside init function --> object instance
        self.marks = marks
        print("Adding new student in database...")
    
    def hello(self):
        print("Hello!", self.name)
    
    def get_marks(self):
        return self.marks



s1 = Student("Harshith", 88) # creating student --> calls init function
print(s1.name)
print(s1.name, s1.marks)

# attributes : all the data and variables that are passed into functions inside class

s2 = Student("Ved", 98)
print(s2.college_name)

# the init function is an example of parameterised constructors while init if used with only 'self' is referred to as default constructors

s2.hello() # calling using object
Student.hello(s2) # calling passing object as parameter
print(s2.get_marks())

class Subjects:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "your average score is : ", sum/3)

    @staticmethod # converts a normal function into static function that don't use self parameter
    def college_name():
        print("IIT Delhi")

s1 = Subjects("Harshith", [88, 93, 98])
s1.get_avg()

s1.name = "IronMan" # can change the parameters stored directly
s1.get_avg()
s1.college_name() 
# decorators are those which inputs a function, changes its behavior and returns it back without completely modifying it

# Abstraction : Hiding the implementation details and show only the essential features to user

class Cr:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started.....")

s1 = Cr()
s1.start() # hid the clutch and acc turning True

# Encapsulation : wrapping data and functions into a single unit (object)
# all the above classes we used are the capsules

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance is :", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance is :", self.get_balance())

    def get_balance(self):
        return self.balance

a1 = Account(1000, 123)
a1.get_balance()
a1.debit(50)
a1.credit(100)
a1.get_balance()

# del keyword : to delete info related to any object or the whole object itself
del a1.account_no
print(a1.account_no)

# Private attributes and methods : The data and methods that can't be publicly accessed
class Acc:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # privated the pass --> same for method, using __
    
    def reset(self):
        print(self.__acc_pass) # it works only inside the class --> more importantly the privated attributes and methods are called with self.

a1 = Acc("12345", "abcde")
# print(a1.acc_pass) # can't be accessed publicly
a1.reset()

# Inheritance : when one class (child/ derived) inherits the properties and methods from another class (parent/ base)

class Car:
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
car1.start()

# Above example is an example of single inheritance

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
car1.start()

# Above is an example of multi level inheritance

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varA)

# Above is an example of an Multiple inheritance

class Car2:
    def __init__(self, type):
        self.type = type

    @staticmethod # decorator
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar2(Car2):
    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type) # now the type passed through ca1 will be stored in parent class Car2

ca1 = ToyotaCar2("Prius", "diesel")
print(ca1.type) # gives error if super method is not used --> for this we need to call for method in parent which has type attribute

class Person:
    name = "Anonymous"

    def changeName(self, name):
        self.name = name
    
    @classmethod # allows to change the data of class --> takes cls as argument while static method doesn't take any, while instance method take self
    # Its a decorator
    def changeName2(cls, name):
        cls.name = name

p1 = Person()
# now if we try changing the name common to class through changeName method, we can't since the name passed through this method is the instance's name
# can change it using Person.name = name, instead of self.name = name --> Person.name == self.__class__.name
p1.changeName("Harsh")
print(p1.name)
print(Person.name)
p1.changeName2("Harsh")
print(Person.name) # name changed

class Student2:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property # used while returning something that needs to change when the data changes (according to recent data)
    def Percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student2(98, 97, 95)
print(stu1.Percentage)
stu1.phy = 86
print(stu1.Percentage) # updates according to newest data

# also study about @getter and @setter decorators

# Polymorphism : same property has multiple defined uses. For ex:-

print(1 + 2) # addition of numericals
print("1" + "2") # concatenation
print([1, 2, 3] + [4, 5, 6]) # merge

# Creating our own class for Complex numbers

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")
    
    # def add(self, obj2):
    #     newReal = self.real + obj2.real
    #     newImg = self.img + obj2.img
    #     return Complex(newReal, newImg)
    
    def __add__(self, obj2): # Dunder functions
        newReal = self.real + obj2.real
        newImg = self.img + obj2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, obj2):
        newReal = self.real - obj2.real
        newImg = self.img - obj2.img
        return Complex(newReal, newImg)

obj1 = Complex(1, 3)
obj1.showNumber()
obj2 = Complex(-4, 7)
obj2.showNumber()

# obj3 = obj1.add(obj2) # this is done using the function add but we need to output a new obj3 = obj1 + obj2 instead of obj1.add(obj2), etc
# obj3.showNumber()

obj3 = obj1 + obj2 # this is known as operator overloading --> implementation of polymorphism
obj3.showNumber()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1 = Order("Chips", 20)
odr2 = Order("Tea", 15)
print(odr1 > odr2)