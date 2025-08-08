"""
Day 3: Lists, Tuples, and Loops in Python
Author: Captain
Date: 2025-08-09
Description:
This file contains examples of Python lists, tuples, and loops.
Each example includes beginner-friendly explanations for GitHub learning repo.
"""

# ----------------------------
# 1. LISTS - Creation & Access
# ----------------------------

# Creating a list of fruits
fruits = ["apple", "banana", "cherry", "mango"]
print("Original fruits list:", fruits)

# Accessing items using index
print("First fruit:", fruits[0])   # Index starts at 0
print("Last fruit:", fruits[-1])   # Negative index for reverse access

# Updating an item
fruits[1] = "blueberry"
print("After updating second fruit:", fruits)

# Adding items
fruits.append("orange")  # Adds at the end
print("After append:", fruits)

# Inserting at a specific position
fruits.insert(2, "kiwi")
print("After insert:", fruits)

# Removing items
fruits.remove("apple")
print("After remove:", fruits)

# Removing last item
last_item = fruits.pop()
print("Popped item:", last_item)
print("After pop:", fruits)

# ----------------------------
# 2. LIST SLICING
# ----------------------------
numbers = [10, 20, 30, 40, 50, 60, 70]
print("Original numbers list:", numbers)

print("First 3 numbers:", numbers[:3])      # 0 to 2
print("Middle slice:", numbers[2:5])        # 2 to 4
print("From index 4 to end:", numbers[4:])  # 4 to last
print("Every second number:", numbers[::2]) # Skip step 2

# ----------------------------
# 3. TUPLES - Immutable Lists
# ----------------------------
colors = ("red", "green", "blue")
print("Colors tuple:", colors)
print("First color:", colors[0])

# Attempting to modify will cause an error:
# colors[0] = "yellow"  # ❌ Uncomment to test

# Tuple unpacking
r, g, b = colors
print("Red:", r, "Green:", g, "Blue:", b)

# ----------------------------
# 4. LOOPS
# ----------------------------

# For loop over list
print("\nLooping through fruits:")
for fruit in fruits:
    print(fruit)

# For loop with range()
print("\nNumbers from 1 to 5:")
for num in range(1, 6):
    print(num)

# While loop
print("\nWhile loop example:")
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1

# ----------------------------
# 5. NESTED LOOPS
# ----------------------------
adjectives = ["fresh", "ripe", "sweet"]

print("\nNested loops example:")
for adj in adjectives:
    for fruit in fruits:
        print(adj, fruit)

# ----------------------------
# 6. REAL-WORLD USE CASE
# ----------------------------
print("\nGrocery List Example:")

grocery_items = ["milk", "bread", "eggs", "butter"]

# Display with numbering
for index, item in enumerate(grocery_items, start=1):
    print(f"{index}. {item}")

# ----------------------------
# END OF DAY 3
# ----------------------------

