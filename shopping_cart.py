from product import Product

class ShoppingCart:

    def __init__(self):
        self.cart = []

    def cart_total(self):
        total = 0
        for item in self.cart:
            total += item.item_price
        return total

    def add_to_cart(self, item):
        self.cart.append(item)

    def empty_cart(self):
        self.cart.clear()
        print("Your cart is now empty!")