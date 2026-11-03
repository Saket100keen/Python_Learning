# a = 5
# b = 6
# #c = a+b
# c = int.__add__(a,b) #what happens in the backgound when we use + operator
# c = a.__add__(b) 

# print(c)

#operator overloading is a concept in object-oriented programming that allows developers 
#to define custom behavior for standard operators (like +, -, *, etc.) 
#when they are used with user-defined classes. 
#This means that you can specify how these operators should behave 
#when applied to instances of your own classes, enabling more intuitive and expressive code.

class Account:
    def __init__(self, name,balance):
        self.name = name
        self.balance = balance
    
    def __str__(self):#Operator overloading for str() function
        return f'{self.name} : {self.balance}'

    def __add__(self, other):#operator overloading for + operator
        return Account('combined balance:', self.balance + other.balance)
    
    def __gt__(self, other):#operator overloading for > operator
        return self.balance > other.balance

user1 = Account("Vivek", 5000)
user2 = Account("Saket", 2000)
combined_balance = user1 + user2


print(user1.__str__())
print(user2)#__str__() method is called when we use print() function on an object either we write it or not it will be called.
print(combined_balance)

if user1 > user2:
    print(f"{user1.name} pays the bill")
else:
    print(f"{user2.name} pays the bill ")
