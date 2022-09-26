from product import Product
from customer import Customer
from shopping_cart import ShoppingCart

grocery = Product("apple", "fruit", 0.30)
print(grocery.item_name)
print(grocery.item_category)
print(grocery.item_price)

customer_cart = ShoppingCart()