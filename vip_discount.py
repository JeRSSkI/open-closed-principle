from discount import Discount

class VipDiscount(Discount):
    def apply(self, price):
        return price * 0.7
