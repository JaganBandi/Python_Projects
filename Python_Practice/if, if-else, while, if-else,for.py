# Python program using if, if-else, while, if-else inside while, and for loop

# 1. Simple if
num = 10
if num > 5:
    print(f"{num} is greater than 5")

# 2. if-else
num2 = 7
if num2 % 2 == 0:
    print(f"{num2} is even")
else:
    print(f"{num2} is odd")

# 3. while loop
print("\nWhile Loop (Counting 1 to 5):")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# 4. if-else inside while
print("\nChecking even/odd numbers from 1 to 10 using while loop:")
n = 1
while n <= 10:
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
    n += 1

# 5. for loop
print("\nFor Loop (Numbers 1 to 5):")
for i in range(1, 6):
    print(i)
