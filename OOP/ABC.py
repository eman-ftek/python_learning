from abc import ABC, abstractmethod
class Payment(ABC):
 @abstractmethod
 def process_payment(self):
    pass
class VisaPayment(Payment):
    def process_payment(self):
        return("succseful payment")
my_payment=VisaPayment()
my_payment.process_payment()
print(my_payment.process_payment())
