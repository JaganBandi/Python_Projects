import array as arr

# -------------------------------
# Function to check if a number is greater than 5 (using if)
def check_greater(num):
    if num > 5:
        print(f"{num} is greater than 5")

# Function to check even/odd (using if-else)
def even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Function to print numbers using while loop
def while_count(n):
    print("\nWhile Loop (Counting 1 to n):")
    count = 1
    while count <= n:
        print("Count:", count)
        count += 1

# Function to check even/odd using while loop (if-else inside while)
def while_even_odd(n):
    print(f"\nEven/Odd numbers from 1 to {n} using while loop:")
    i = 1
    while i <= n:
        if i % 2 == 0:
            print(i, "is Even")
        else:
            print(i, "is Odd")
        i += 1

# Function to print numbers using for loop
def for_loop(n):
    print(f"\nFor Loop (Numbers 1 to {n}):")
    for i in range(1, n + 1):
        print(i)

# Function to demonstrate array operations
def array_operations():
    print("\nArray Operations:")
    numbers = arr.array('i', [10, 20, 30, 40, 50])

    print("Original Array:", numbers.tolist())

    # Traversing
    print("Array elements:")
    for x in numbers:
        print(x)

    # Modify element
    numbers[2] = 99
    print("After updating 3rd element:", numbers.tolist())

    # Append new element
    numbers.append(60)
    print("After appending 60:", numbers.tolist())

    # Remove element
    numbers.remove(20)
    print("After removing 20:", numbers.tolist())

# -------------------------------
# Main Program
print("Python Program Demonstrating (if, if-else, while, if-else inside while, for loop, arrays, functions)\n")

# Call functions
check_greater(10)       # if
even_odd(7)             # if-else
while_count(5)          # while
while_even_odd(10)      # if-else inside while
for_loop(5)             # for loop
array_operations()      # arrays
