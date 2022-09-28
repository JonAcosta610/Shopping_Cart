
class ShoppingCart:

    def __init__(self):
        self.items = []

    def cart_total(self):
        cart_total = 0
        for item in self.items:
            cart_total += item.item_price
        return cart_total

    def add_item_to_cart(self, item):
        self.items.append(item)
        print(f"Added {item.item_name} to the cart.")

    def empty_cart(self):
        self.items.clear()
        print("Your cart is now empty!")