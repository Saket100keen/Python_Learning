class A:
    def __init__(self):
        print("This is class A constructor")

    def s1(self):
        print("This is method s1 from class A")
    
    def s2(self):
        print("This is method s2 from class A")

    def show(self):
        print("This is method show from class A")

class B(A): #single level inheritance
    def __init__(self):
        print("This is class B constructor")

    def s3(self):
        print("This is method s3 from class B") 

    def show(self):
        print("This is method show from class B")

class C(B): #multilevel inheritance
    def __init__(self):
        print("This is class C constructor")

    def s4(self):
        print("This is method s4 from class B")

    def show(self):
        print("This is method show from class C")

class D():
    def __init__(self):
        print("This is class D constructor")

    def s5(self):
        print("This is method s5 from class D")

    def show(self):
        print("This is method show from class D")

class E(A, D): #multiple inheritance  
    def __init__(self):
        print("This is class E constructor")
        super().__init__() #calling the constructor of class A

    def s6(self):
        super().s1() #calling the method s1 of class A
        print("This is method s6 from class E")

    def show(self):
        print("This is method show from class E")
    
object_1 = E()
object_1.show()#MRO(Method Resolution Order) it searches it own class first then the first parent class(A,D) i.e. A then D.
object_1.s6()