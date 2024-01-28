from typedproperty import String, Integer, Float


class Stock:
    # __slots__ = ["name", "price", "_shares"]
    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares:d}, {self.price:.2f})"
