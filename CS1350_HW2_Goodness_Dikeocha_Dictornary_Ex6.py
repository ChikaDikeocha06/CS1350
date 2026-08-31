# Exercise 6: Safely access a missing key

pet = {
    "name": "Buddy",
    "type": "dog",
    "age": 3
}

print(pet.get("color", "unknown"))
