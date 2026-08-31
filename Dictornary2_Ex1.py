# ============================================================
# UNIT 2.1 — HOW DICTIONARIES WORK
# COMPLETED HOMEWORK
# ============================================================


# ============================================================
# BEGINNER — 5 POINTS
# ============================================================

print("===== BEGINNER =====")

a = "student_name"
b = [1, 2, 3]
c = 100
d = ("x", "y")
e = {"a": 1}
f = frozenset({1, 2})

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print("f:", f)

# Answers:
# a) valid - strings are immutable and hashable
# b) invalid - lists are mutable and unhashable
# c) valid - numbers are immutable and hashable
# d) valid - tuples are immutable and hashable
# e) invalid - dictionaries are mutable and unhashable
# f) valid - frozensets are immutable and hashable


# ============================================================
# INTERMEDIATE — 10 POINTS
# ============================================================

print("\n===== INTERMEDIATE =====")


# QUESTION 1
# Lists cannot be dictionary keys, so use tuples instead.

locations = {
    (40.7, -74.0): "New York",
    (34.0, -118.2): "Los Angeles"
}

print(locations)


# QUESTION 2
# Duplicate keys are replaced by the last value.

data = {
    "a": 1,
    "b": 2,
    "a": 3,
    "b": 4
}

print(data)
print(len(data))

# Output:
# {'a': 3, 'b': 4}
# 2


# QUESTION 3
# Hash values

name = "Goodness"

print("Hash of my name:", hash(name))
print("Hash of 100:", hash(100))

# The hash value of a string can vary between Python sessions.
# The hash of the integer 100 is 100.


# ============================================================
# ADVANCED — 15 POINTS
# ============================================================

print("\n===== ADVANCED =====")


# QUESTION 1
# Game high scores using tuples as keys

high_scores = {
    ("Alice", "Minecraft"): 950,
    ("Bob", "Fortnite"): 875,
    ("Carol", "Mario Kart"): 990
}

print(high_scores)

# Retrieve one score
print("Alice's Minecraft score:", high_scores[("Alice", "Minecraft")])


# QUESTION 2
# Compare list and dictionary search times

import time

big_list = list(range(100000))
big_dict = {i: i for i in range(100000)}

# List search
start = time.time()

result = 99999 in big_list

list_time = time.time() - start

# Dictionary search
start = time.time()

result = 99999 in big_dict

dict_time = time.time() - start

print("List search time:", list_time)
print("Dictionary search time:", dict_time)

if dict_time < list_time:
    print("Dictionary search is faster.")
else:
    print("List search is faster.")