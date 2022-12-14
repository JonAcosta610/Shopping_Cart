from product import Product
from customer import Customer

customer_one = Customer("Mike Jones")
print(f"The customer's name is {customer_one.name}")

apple = Product("apple", "fruit", 0.35)
bread = Product("bread", "grains", 2.15)
milk = Product("milk", "dairy", 3.20)

# testing out code to make sure that the product files worked properly
# print(apple.item_name, apple.item_category, apple.item_price)
# print(bread.item_name, bread.item_category, bread.item_price)
# print(milk.item_name, milk.item_category, milk.item_price)

customer_one.add_to_cart(apple)
customer_one.add_to_cart(bread)
customer_one.add_to_cart(milk)

total = customer_one.cart.cart_total()
print(f"{customer_one.name}'s total is {total}")

customer_one.cart.empty_cart()

customer_one.items_in_cart()
