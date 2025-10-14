# Program using list as an array

# Creating an array (list)
arr = [10, 20, 30, 40, 50]

# Printing elements
print("Array elements are:")
for i in arr:
    print(i)

# Accessing specific element
print("\nFirst element:", arr[0])
print("Last element:", arr[-1])

# Modifying an element
arr[2] = 99
print("\nArray after modification:", arr)

# Adding new element
arr.append(60)
print("Array after appending:", arr)

# Removing an element
arr.remove(20)
print("Array after removing 20:", arr)
