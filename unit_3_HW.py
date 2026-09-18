
# Week 2 Lecture 1 Dictionary III

print("Unit 3.1 Practice Exercises Beginner 5, Intermediate 10, Advanced 15")

# Beginner
inventory = {"apples": 50, "bananas": 30, "oranges": 25}

# 1. Print each product name
for fruit in inventory:
    print(fruit)

# 2. Calculate total items
total = sum(inventory.values())
print("Total items:", total)

# 3. Print each product with quantity
for name, quantity in inventory.items():
    print(f"{name}: {quantity}")


# Intermediate
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

# 1. Print products sorted alphabetically
for product in sorted(prices):
    print(product)

# 2. Print products sorted by price
for product in sorted(prices, key=prices.get):
    print(product, prices[product])

# 3. Find most expensive item
most_expensive = max(prices.items(), key=lambda item: item[1])
print("Most expensive:", most_expensive)


# Advanced
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

# 1. Calculate average temperature
average = sum(temps.values()) / len(temps)
print("Average temperature:", average)

# 2. Find hottest and coldest days
hottest_day = None
coldest_day = None

for day, temp in temps.items():
    if hottest_day is None or temp > temps[hottest_day]:
        hottest_day = day

    if coldest_day is None or temp < temps[coldest_day]:
        coldest_day = day

print("Hottest day:", hottest_day, temps[hottest_day])
print("Coldest day:", coldest_day, temps[coldest_day])

# 3. Count days above average
count = 0

for temp in temps.values():
    if temp > average:
        count += 1

print("Days above average:", count)


# Unit 3.2

print("Unit 3.2 Practice Exercises Beginner 5, Intermediate 10, Advanced 15")

# Beginner
products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}

# 1. Print laptop price
print("Laptop price:", products["laptop"]["price"])

# 2. Print each product with stock
for product, info in products.items():
    print(product, "stock:", info["stock"])


# Intermediate

# 1. Create dictionary using zip()
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

country_capitals = dict(zip(countries, capitals))
print(country_capitals)

# 2. Add tablet
products["tablet"] = {"price": 449, "stock": 30}
print(products)

# 3. Remove products with stock less than 20
products = {
    name: info
    for name, info in products.items()
    if info["stock"] >= 20
}

print(products)


# Advanced

company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000}
}

# 1. Print all employees with salaries
for department, employees in company.items():
    for employee, salary in employees.items():
        print(employee, salary)

# 2. Calculate average salary per department
for department, employees in company.items():
    average_salary = sum(employees.values()) / len(employees)
    print(department, "average salary:", average_salary)

# 3. Find highest-paid employee
highest_employee = None
highest_salary = 0

for department, employees in company.items():
    for employee, salary in employees.items():
        if salary > highest_salary:
            highest_salary = salary
            highest_employee = employee

print("Highest-paid employee:", highest_employee)
print("Salary:", highest_salary)


# Unit 3.3

print("Unit 3.3 Practice Exercises Beginner 5, Intermediate 10, Advanced 15")

# Beginner

# 1. Map numbers 1-5 to their cubes
cubes = {}

for number in range(1, 6):
    cubes[number] = number ** 3

print("Cubes:", cubes)

# 2. Convert Fahrenheit to Celsius
temps = {"Mon": 72, "Tue": 68, "Wed": 75}

celsius = {}

for day, temp in temps.items():
    celsius[day] = (temp - 32) * 5 / 9

print("Celsius:", celsius)


# Intermediate

scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}

# 1. Passing scores
passing = {}

for student, score in scores.items():
    if score >= 70:
        passing[student] = score

print("Passing:", passing)

# 2. Convert scores to letter grades
letter_grades = {}

for student, score in scores.items():
    if score >= 90:
        letter_grades[student] = "A"
    elif score >= 80:
        letter_grades[student] = "B"
    elif score >= 70:
        letter_grades[student] = "C"
    elif score >= 60:
        letter_grades[student] = "D"
    else:
        letter_grades[student] = "F"

print("Letter grades:", letter_grades)

# 3. Invert student IDs
student_ids = {"Alice": 101, "Bob": 102}

ids_to_students = {}

for student, student_id in student_ids.items():
    ids_to_students[student_id] = student

print("IDs:", ids_to_students)


# Advanced

sales = [
    ("North", "Alice", 5000),
    ("South", "Bob", 4500),
    ("North", "Carol", 6000),
    ("South", "Alice", 3500)
]

# 1. Total sales by region
region_sales = {}

for region, person, amount in sales:
    if region not in region_sales:
        region_sales[region] = 0

    region_sales[region] += amount

print("Sales by region:", region_sales)

# 2. Total sales by salesperson
person_sales = {}

for region, person, amount in sales:
    if person not in person_sales:
        person_sales[person] = 0

    person_sales[person] += amount

print("Sales by person:", person_sales)

# 3. Nested dictionary
nested_sales = {}

for region, person, amount in sales:
    if region not in nested_sales:
        nested_sales[region] = {}

    if person not in nested_sales[region]:
        nested_sales[region][person] = 0

    nested_sales[region][person] += amount

print("Nested sales:", nested_sales)


# ==========================================================
# WEEK 2 LECTURE 2 - SETS
# ==========================================================

print("Week 2 Lecture 2 Set")


# Unit 1

print("Unit 1: Set Practice Exercises")


# Beginner

# 1. Create a set of vowels
vowels = {"a", "e", "i", "o", "u"}
print("Vowels:", vowels)

# 2. Create a set from the list
numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print("Set:", numbers)
print("Number of elements:", len(numbers))

# 3. What's wrong with this?
empty = {}
print("Type of empty:", type(empty))

# Correct way to create an empty set
empty_set = set()
print("Empty set:", empty_set)


# Intermediate

# 1. Unique characters in Mississippi
text = "mississippi"

unique_letters = set(text)

print("Unique letters:", unique_letters)
print("Number of unique letters:", len(unique_letters))

# 2. Remove duplicates from email list
emails = [
    "a@b.com",
    "c@d.com",
    "a@b.com",
    "e@f.com",
    "c@d.com"
]

unique_emails = list(set(emails))

print("Unique emails:", unique_emails)

# 3. Why does this fail?
# s = {[1, 2], [3, 4]}

# Lists cannot be inside a set because lists are mutable.


# Advanced

# 1. Compare set and list
numbers_set = set(range(1000000))
numbers_list = list(range(1000000))

print(999999 in numbers_set)
print(999999 in numbers_list)

# Sets are generally faster for checking membership.


# 2. Frozenset as dictionary key
my_set = frozenset(["Python", "SQL"])

skills = {
    my_set: "Programming skills"
}

print("Frozenset dictionary:", skills)


# 3. Unique nodes
edges = [
    (1, 2),
    (2, 3),
    (1, 3),
    (3, 4)
]

nodes = set()

for edge in edges:
    nodes.update(edge)

print("Unique nodes:", nodes)


# ==========================================================
# Unit 2 - Set Operations
# ==========================================================

print("Unit 2: Set Operations")


# Beginner

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1. Union
print("Union:", a | b)

# 2. Intersection
print("Intersection:", a & b)

# 3. Difference
print("Difference:", a - b)


# Intermediate

morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

# 1. Employees who work all shifts
all_shifts = morning_shift & evening_shift & weekend_shift
print("All shifts:", all_shifts)

# 2. Employees who work at least one shift
any_shift = morning_shift | evening_shift | weekend_shift
print("Any shift:", any_shift)

# 3. Employees who ONLY work morning
only_morning = morning_shift - evening_shift - weekend_shift
print("Only morning:", only_morning)

# 4. Employees who work exactly one shift
exactly_one = set()

for employee in any_shift:
    shifts = 0

    if employee in morning_shift:
        shifts += 1

    if employee in evening_shift:
        shifts += 1

    if employee in weekend_shift:
        shifts += 1

    if shifts == 1:
        exactly_one.add(employee)

print("Exactly one shift:", exactly_one)


# Advanced

prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

# 1. Students eligible to enroll
eligible = prereqs_met & has_space & paid_tuition
print("Eligible:", eligible)

# 2. Students who met prerequisites but haven't paid
not_paid = prereqs_met - paid_tuition
print("Met prerequisites but haven't paid:", not_paid)

# 3. Students missing at least one requirement
all_students = prereqs_met | has_space | paid_tuition

needs_requirement = all_students - eligible
print("Missing at least one requirement:", needs_requirement)


# ==========================================================
# Unit 3 - Set Manipulation
# ==========================================================

print("Unit 3: Set Manipulation")


# Beginner

# 1. Add 4 and remove 1
numbers = {1, 2, 3}

numbers.add(4)
numbers.remove(1)

print("Updated set:", numbers)

# 2. Even numbers from 0-20
even_numbers = set()

for number in range(21):
    if number % 2 == 0:
        even_numbers.add(number)

print("Even numbers:", even_numbers)

# 3. discard vs remove
numbers = {1, 2, 3}

numbers.discard(5)
print("After discard:", numbers)

# remove() would give an error if the item doesn't exist.


# Intermediate

# 1. Remove duplicates while preserving order
numbers = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]

unique_numbers = list(dict.fromkeys(numbers))

print("Without duplicates:", unique_numbers)

# 2. Unique words
sentence = "To be or not to be that is the question"

unique_words = set()

for word in sentence.lower().split():
    unique_words.add(word)

print("Unique words:", unique_words)

# 3. Find missing numbers
expected = set(range(1, 11))

actual = {1, 2, 4, 5, 7, 8, 10}

missing = expected - actual

print("Missing numbers:", missing)


# Advanced

# 1. Function to find duplicates
def find_duplicates(lst):
    duplicates = set()

    for item in lst:
        if lst.count(item) > 1:
            duplicates.add(item)

    return duplicates


print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))


# 2. Employee skills

alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}

# Skills all three have
all_three = alice & bob & carol
print("Skills all three have:", all_three)

# Skills only Alice has
only_alice = alice - bob - carol
print("Skills only Alice has:", only_alice)

# All unique skills
all_skills = alice | bob | carol
print("All unique skills:", all_skills)


# 3. Common characters function
def common_chars(string1, string2):
    return set(string1) & set(string2)


print("Common characters:", common_chars("hello", "world"))

