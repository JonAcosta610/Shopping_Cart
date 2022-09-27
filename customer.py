from shopping_cart import ShoppingCart

class Customer:

    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def add_to_cart(self, item):
        self.cart.add_to_cart(item)
        print(f"{self.name} has added {item} to the cart!")

    def items_in_cart(self):
        for item in self.cart.item:
            print(item.name)