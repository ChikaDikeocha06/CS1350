# ============================================================
# UNIT 2.2 — keys() AND values()
# COMPLETED HOMEWORK
# ============================================================


# ============================================================
# BEGINNER — 5 POINTS
# ============================================================

print("===== BEGINNER =====")

temps = {
    "Monday": 72,
    "Tuesday": 75,
    "Wednesday": 68
}

# 1. Print all day names using keys()

print("Days:")
for day in temps.keys():
    print(day)


# 2. Print all temperatures using values()

print("\nTemperatures:")
for temperature in temps.values():
    print(temperature)


# 3. Print how many days are in the dictionary

print("\nNumber of days:", len(temps))


# ============================================================
# INTERMEDIATE — 10 POINTS
# ============================================================

print("\n===== INTERMEDIATE =====")

temps = {
    "Monday": 72,
    "Tuesday": 75,
    "Wednesday": 68
}


# QUESTION 1
# Find highest and lowest temperatures

highest = max(temps.values())
lowest = min(temps.values())

print("Highest temperature:", highest)
print("Lowest temperature:", lowest)


# QUESTION 2
# Check if Friday exists

if "Friday" in temps:
    print("Friday is in the dictionary.")
else:
    print("Friday is not in the dictionary.")


# QUESTION 3
# Add Thursday only if it does not exist

temps.setdefault("Thursday", 70)

print("After adding Thursday:", temps)


# QUESTION 4
# Demonstrate that views are dynamic

keys_view = temps.keys()

print("Before adding Friday:", keys_view)

temps["Friday"] = 80

print("After adding Friday:", keys_view)


# ============================================================
# ADVANCED — 15 POINTS
# ============================================================

print("\n===== ADVANCED =====")

prices = {
    "laptop": 999,
    "phone": 699,
    "tablet": 449,
    "watch": 299
}


# QUESTION 1
# Calculate total and average price

total = sum(prices.values())
average = total / len(prices)

print("Total value:", total)
print("Average price:", average)


# QUESTION 2
# Find most and least expensive items

most_expensive = max(prices, key=prices.get)
least_expensive = min(prices, key=prices.get)

print(
    "Most expensive:",
    most_expensive,
    "$",
    prices[most_expensive]
)

print(
    "Least expensive:",
    least_expensive,
    "$",
    prices[least_expensive]
)


# QUESTION 3
# Compare memory usage

import sys

keys_view = prices.keys()
keys_list = list(prices.keys())

print("Keys view size:", sys.getsizeof(keys_view), "bytes")
print("Keys list size:", sys.getsizeof(keys_list), "bytes")


# QUESTION 4
# Add 3 products using update()

prices.update({
    "headphones": 199,
    "keyboard": 129,
    "mouse": 59
})

print("\nAll products:")

for product, price in prices.items():
    print(product, "$", price)
