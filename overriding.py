
class A:
    def show(self):
        print("This is method show from class A")
    
class B(A):
    def show(self):#overriding show function of class B overrides the show function of class A as it has one if it don't have one it will use the show function of class A.
        print("This is method show from class B")

obj1 = B()
obj1.show()