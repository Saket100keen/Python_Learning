from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass

class Phonepe(PaymentGateway):
    def pay(self):
        print("Payment done using Phonepe")

class razorpay(PaymentGateway):
    def pay(self):
        print("Payment done using Razorpay")


class Purchase:
    def __init__(self, gateway : Phonepe):
        self.gateway = gateway

    def checkout(self):
        print("Checking out the purchase...") 
        
        self.gateway.pay()


gateway1 = razorpay()
gateway2 = Phonepe()
purchase1 = Purchase(gateway2)

purchase1.checkout()