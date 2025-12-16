class DiscountCalculator:
    def calculate(self, discount, price):
        return discount.apply(price)
