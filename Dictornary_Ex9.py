# Exercise 9: Look up a product

products = {
    "laptop": 999.99,
    "mouse": 29.99,
    "keyboard": 79.99
}

product = input("Enter a product name: ")

price = products.get(product, "Product not available")

print(price)