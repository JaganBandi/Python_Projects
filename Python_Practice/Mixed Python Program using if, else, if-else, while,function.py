# Mixed Python Program using if, else, if-else, while, arrays, and functions

# Function to check positive/negative using simple if, else
def check_sign(num):
    if num >= 0:     # simple if
        print(num, "is Positive")
    else:            # else
        print(num, "is Negative")

# Function to check even/odd using if-else
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

# Function to calculate sum of array elements using while loop
def sum_of_array(arr):
    total = 0
    i = 0
    while i < len(arr):   # while loop
        total += arr[i]
        i += 1
    return total

# Main program
def main():
    # Taking input for array
    n = int(input("Enter number of elements in array: "))
    numbers = []

    i = 0
    while i < n:   # while loop for input
        val = int(input(f"Enter element {i+1}: "))
        numbers.append(val)
        i += 1

    print("\nArray Elements:", numbers)

    # Check each element using functions
    for num in numbers:
        check_sign(num)
        check_even_odd(num)

    # Find sum of array
    total = sum_of_array(numbers)
    print("\nSum of Array Elements:", total)

    # if-else to check sum condition
    if total > 100:
        print("Sum is greater than 100")
    else:
        print("Sum is less than or equal to 100")

# Run the program
main()
