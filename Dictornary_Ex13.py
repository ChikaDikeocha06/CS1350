#Create a simple shopping cart system:

#1. Start with an empty cart dictionary
shopping_cart={}
#2. Add 3 items with prices
shopping_cart["apple"]=0.99
shopping_cart["bannana"]=0.59
shopping_cart["orange"]=0.79
#3. Update the price of one item
shopping_cart["bannana"]=0.80
#4. Remove one item and print what was removed
shopping_cart.pop("orange")
#5. Print the final cart
print(shopping_cart)

sum= shopping_cart["apple"] + shopping_cart["bannana"]
print("Total cost of items in the cart: $", sum)