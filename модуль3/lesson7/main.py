class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        return self.price + other.price


item1 = Item('videokarta', 15_000, 0.8)
item2 = Item('processor', 20_000, 0.2)


# total_sum = item1.price + item2.price
total_sum = item1 + item2
print(total_sum)























