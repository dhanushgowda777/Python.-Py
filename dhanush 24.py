
numbers = {1, 2, 3, 4, 5}

print("Original set:", numbers)

# Adding an element
numbers.add(6)
print("After adding 6:", numbers)

# Removing an element
numbers.remove(3)
print("After removing 3:", numbers)

# Checking membership
print("Is 4 in the set?", 4 in numbers)

# Looping through set
print("All elements in set:")
for n in numbers:
    print(n)