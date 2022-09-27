class ShoppingCart:

    def __init__(self):
        self.cart = []

    def cart_total(self):
        total = 0
        for item in self.cart:
            total += product.item_price
        return total

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"You have added {product.item_name}")

    def empty_cart(self):
        self.cart.clear()
        print("Your cart is now empty!")