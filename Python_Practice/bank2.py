# Python Program using Primitive Data Types

# Integer (int)
principal = 10000   # principal amount in rupees

# Float (float)
rate_of_interest = 7.5   # annual interest rate in %

# String (str)
customer_name = "Rahul"

# Boolean (bool)
is_senior_citizen = True   # seniors get extra interest

# Logic
if is_senior_citizen:
    rate_of_interest += 1.0   # senior citizens get 1% extra

# Simple Interest Formula: SI = (P * R * T) / 100
time = 5   # years (int)
simple_interest = (principal * rate_of_interest * time) / 100

# Output (using string + variables)
print("---- Bank Interest Calculation ----")
print("Customer Name:", customer_name)       # string
print("Principal Amount:", principal)        # int
print("Rate of Interest:", rate_of_interest) # float
print("Time (years):", time)                 # int
print("Senior Citizen:", is_senior_citizen)  # bool
print("Simple Interest:", simple_interest)   # float
