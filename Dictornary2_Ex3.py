# ============================================================
# UNIT 2.3 — THE items() METHOD
# COMPLETED HOMEWORK
# ============================================================


# ============================================================
# BEGINNER — 5 POINTS
# ============================================================

print("===== BEGINNER =====")

colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}


# QUESTION 1
# Use items() to print each fruit and its color

for fruit, color in colors.items():
    print(f"The {fruit} is {color}")


# QUESTION 2
# list(colors.items())

print("\nPredicted output:")
print([
    ("apple", "red"),
    ("banana", "yellow"),
    ("grape", "purple")
])


# ============================================================
# INTERMEDIATE — 10 POINTS
# ============================================================

print("\n===== INTERMEDIATE =====")


# QUESTION 1
# Add 10% tax to each price

prices = {
    "coffee": 4.50,
    "tea": 3.00,
    "juice": 5.25
}

for item, price in prices.items():
    tax = price * 0.10
    total = price + tax

    print(
        f"{item}: ${price:.2f} + tax = ${total:.2f}"
    )


# QUESTION 2
# Count items costing more than $4

count = 0

for item, price in prices.items():
    if price > 4.00:
        count += 1

print("Items over $4:", count)


# QUESTION 3
# Swap x and y using tuple unpacking

x = 10
y = 20

x, y = y, x

print("x:", x)
print("y:", y)


# QUESTION 4
# Extended unpacking

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ============================================================
# ADVANCED — 15 POINTS
# ============================================================

print("\n===== ADVANCED =====")

scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}


# QUESTION 1
# Find the highest-scoring student

best_name, best_score = max(
    scores.items(),
    key=lambda x: x[1]
)

print(
    "Highest score:",
    best_name,
    best_score
)


# QUESTION 2
# Create passed and failed dictionaries

passed = {}
failed = {}

for name, grade in scores.items():
    if grade >= 70:
        passed[name] = grade
    else:
        failed[name] = grade

print("Passed:", passed)
print("Failed:", failed)


# QUESTION 3
# Calculate class average and deviation

average = sum(scores.values()) / len(scores)

deviations = {}

for name, grade in scores.items():
    deviations[name] = grade - average

print("Class average:", average)
print("Deviations:")

for name, deviation in deviations.items():
    print(name, deviation)


# QUESTION 4
# Compare items() with keys() + lookup

import time

big_dict = {
    i: i * 2
    for i in range(50000)
}


# items() test

start = time.time()

for key, value in big_dict.items():
    result = key + value

items_time = time.time() - start


# keys() + lookup test

start = time.time()

for key in big_dict.keys():
    value = big_dict[key]
    result = key + value

keys_time = time.time() - start


print("items() time:", items_time)
print("keys() + lookup time:", keys_time)

if items_time < keys_time:
    print("items() was faster.")
else:
    print("keys() + lookup was faster.")