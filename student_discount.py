from discount import Discount

class StudentDiscount(Discount):
    def apply(self, price):
        return price * 0.8
