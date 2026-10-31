# ------------------------------------------------------------
# 1. VARIABLES AND PRINT STATEMENTS
# ------------------------------------------------------------

# Variables store values.
student_name = "Aarav"
student_age = 21
course = "Data Analytics"
fees = 45000.50
is_enrolled = True

# Display individual values.
print(student_name)
print(student_age)

# Display multiple values.
print("Student:", student_name, "| Age:", student_age)

# f-strings make output readable.
print(f"{student_name} is studying {course}.")

# TODO 1:
# Create variables for employee_name, department, salary,
# experience_years and is_active.
# Print all details using f-strings.


# ------------------------------------------------------------
# 2. PYTHON DATA TYPES
# ------------------------------------------------------------

name = "Priya"                 # str
age = 22                       # int
salary = 35000.75              # float
is_employee = True             # bool



print(type(name))
print(type(age))
print(type(salary))
print(type(is_employee))

# Python is dynamically typed.
value = 100
print(value)

value = "One Hundred"
print(value)

# TODO 2:
# Create one variable for each of the five data types above.
# Print its value and type.


# ------------------------------------------------------------
# 3. TYPE CONVERSION
# ------------------------------------------------------------

# input() accepts user input as a string.
# Uncomment these lines when running interactively.

# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# monthly_salary = float(input("Enter your salary: "))

number_text = "250"
number = int(number_text)

price_text = "199.99"
price = float(price_text)

quantity = 5
quantity_text = str(quantity)

print(number + 50)
print(price)
print("Quantity: " + quantity_text)

# Convert a number to a float.
print(float(10))

# Convert a float to an integer (decimal part is discarded).
print(int(12.9))

# TODO 3:
# Convert "45000" to an integer.
# Convert "89.5" to a float.
# Convert 2026 to a string.
# Explain why int("89.5") raises an error.


# ------------------------------------------------------------
# 4. ARITHMETIC OPERATORS
# ------------------------------------------------------------

a = 17
b = 5

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor division
print(a % b)    # Remainder
print(a ** b)   # Exponentiation

# Practical example: calculate a discount.
original_price = 2000
discount_percentage = 15

discount = original_price * discount_percentage / 100
final_price = original_price - discount

print("Discount:", discount)
print("Final price:", final_price)

# TODO 4:
# An employee earns 35000 per month.
# Calculate annual salary, 10% bonus and annual salary
# after adding the bonus.
#
# A store sells 7 items at Rs. 125 each.
# Calculate total sales and the average price per item.


# ------------------------------------------------------------
# 5. COMPARISON AND LOGICAL OPERATORS
# ------------------------------------------------------------

x = 20
y = 30

print(x == y)    # Equal to
print(x != y)    # Not equal to
print(x > y)     # Greater than
print(x < y)     # Less than
print(x >= y)    # Greater than or equal to
print(x <= y)    # Less than or equal to

# Logical operators: and, or, not
age = 24
salary = 40000

print(age >= 18 and salary >= 30000)
print(age < 18 or salary >= 30000)
print(not (age < 18))

# Membership operators.
department = "Data Analytics"

print("Data" in department)
print("Finance" not in department)

# Identity operators: is and is not.
first_value = None
print(first_value is None)

# Note: == compares values; is checks object identity.
# Use "is None" to check for None.

# TODO 5:
# A candidate is eligible if:
# age >= 21 AND experience >= 1 AND salary >= 25000.
# Write a Boolean expression to check eligibility.
#
# A product needs restocking if stock < 10 OR stock == 0.
# Write the condition.


# ------------------------------------------------------------
# 6. CONDITIONAL STATEMENTS
# ------------------------------------------------------------

marks = 78

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

# Nested conditions.
age = 23
has_id = True

if age >= 18:
    if has_id:
        print("Entry permitted")
    else:
        print("ID required")
else:
    print("Entry denied")

# Conditional expression (ternary expression).
sales = 50000
target = 45000

status = "Achieved" if sales >= target else "Not achieved"
print(status)

# TODO 6:
# Classify a transaction:
# amount <= 0: Invalid
# amount < 1000: Small transaction
# amount < 10000: Medium transaction
# otherwise: Large transaction.
#
# Determine whether a year is a leap year.
# Hint: use %, and consider divisibility by 400 and 100.


# ------------------------------------------------------------
# 7. STRINGS AND STRING METHODS
# ------------------------------------------------------------

customer_name = "  riya sharma  "

print(customer_name.upper())
print(customer_name.lower())
print(customer_name.title())
print(customer_name.strip())

# Replace part of a string.
email = "user@gmail.com"
print(email.replace("gmail.com", "outlook.com"))

# Find string length.
print(len(customer_name))

# Indexing: positions start at 0.
word = "PYTHON"
print(word[0])
print(word[-1])

# Slicing: end position is excluded.
print(word[0:3])
print(word[2:])
print(word[:4])
print(word[::-1])

# Check whether a string contains digits or letters.
code = "A123"
print(code.isalnum())
print("123".isdigit())
print("hello".isalpha())

# Split and join.
full_name = "Riya Sharma"
name_parts = full_name.split(" ")
print(name_parts)
print("-".join(name_parts))

# Remove unnecessary spaces from user-entered data.
raw_city = "  Mumbai  "
clean_city = raw_city.strip()

# TODO 7:
# Given "  DATA ANALYST  ":
# 1. Remove extra spaces.
# 2. Convert to lowercase.
# 3. Count its characters.
# 4. Check whether "analyst" appears in it.
# 5. Reverse the string.
#
# Given "sales,finance,marketing":
# Split it into a list of departments.


# ------------------------------------------------------------
# 8. LOOPS: FOR AND WHILE
# ------------------------------------------------------------

# for loop using range().
for number in range(1, 6):
    print(number)

# range(start, stop, step).
for number in range(2, 11, 2):
    print(number)

# Iterate over a string.
for character in "DATA":
    print(character)

# while loop.
counter = 1

while counter <= 5:
    print(counter)
    counter += 1

# break: exit the loop.
for number in range(1, 10):
    if number == 5:
        break
    print(number)

# continue: skip the current iteration.
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# pass: placeholder for code to be written later.
for number in range(3):
    pass

# Loop with an else clause.
# The else block runs if the loop finishes without break.
for number in range(3):
    print(number)
else:
    print("Loop completed")

# TODO 8:
# Print all numbers from 1 to 100.
# Print only multiples of 7 between 1 and 100.
# Calculate the sum of numbers from 1 to 50.
# Print a multiplication table for any number.
# Count the digits in a positive integer using a while loop.
# Find the factorial of a positive integer using a loop.


# ------------------------------------------------------------
# 9. LOGIC BUILDING AND NUMBER PROBLEMS
# ------------------------------------------------------------

# Sum of digits.
number = 583
digit_sum = 0
temporary = number

while temporary > 0:
    digit = temporary % 10
    digit_sum += digit
    temporary //= 10

print("Sum of digits:", digit_sum)

# Reverse a positive integer.
number = 1234
reversed_number = 0
temporary = number

while temporary > 0:
    digit = temporary % 10
    reversed_number = reversed_number * 10 + digit
    temporary //= 10

print("Reversed number:", reversed_number)

# Prime number check.
number = 17
is_prime = number >= 2

for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        break

print("Prime:", is_prime)

# TODO 9:
# Check whether a number is a palindrome.
# Check whether a number is an Armstrong number.
# Print the Fibonacci sequence for n terms.
# Find all prime numbers between 1 and 100.
# Find the greatest common divisor of two positive integers.
# Print the following pattern for 5 rows:
# *
# **
# ***
# ****
# *****


# ------------------------------------------------------------
# 10. LISTS
# ------------------------------------------------------------

sales = [1200, 1500, 900, 2100, 1800]

print(sales)
print(sales[0])
print(sales[-1])
print(sales[1:4])
print(len(sales))

# Lists are mutable.
sales[0] = 1300
print(sales)

# Add elements.
sales.append(2500)
sales.insert(1, 1400)
sales.extend([1700, 1900])
print(sales)

# Remove elements.
sales.remove(900)       # Removes first matching value
last_item = sales.pop() # Removes and returns last item

print(last_item)
print(sales)

# Sorting.
sales.sort()
print(sales)

sales.sort(reverse=True)
print(sales)

# sorted() returns a new sorted list.
original = [4, 1, 3, 2]
sorted_copy = sorted(original)

print(original)
print(sorted_copy)

# Other useful operations.
numbers = [10, 20, 30, 40]
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(numbers.count(20))
print(numbers.index(30))

# List membership.
print(20 in numbers)

# Loop over a list.
for amount in numbers:
    print(amount)

# List comprehension.
squares = [number ** 2 for number in range(1, 6)]
print(squares)

# Filter values using a condition.
high_values = [amount for amount in numbers if amount >= 25]
print(high_values)

# enumerate() gives index and value.
for index, amount in enumerate(numbers):
    print(index, amount)

# TODO 10:
# Given daily_sales = [500, 1200, 800, 2500, 1800]:
# Calculate total and average sales.
# Find the highest and lowest sales.
# Count days with sales greater than 1000.
# Create a list containing only sales above the average.
# Remove duplicate values from a list without using set().
# Find the second-largest distinct number in a list.


# ------------------------------------------------------------
# 11. TUPLES
# ------------------------------------------------------------

# Tuples are ordered and immutable.
employee = ("E101", "Aarav", "Analytics", 35000)

print(employee[0])
print(employee[1])
print(len(employee))
print(employee.count("Analytics"))
print(employee.index("Aarav"))

# Tuple unpacking.
employee_id, employee_name, team, salary = employee

print(employee_id, employee_name, team, salary)

# A single-element tuple needs a comma.
single_value = (10,)
print(type(single_value))

# Convert between list and tuple.
numbers = [10, 20, 30]
numbers_tuple = tuple(numbers)
numbers_list = list(numbers_tuple)

print(numbers_tuple)
print(numbers_list)

# TODO 11:
# Store a product's ID, name, category and price in a tuple.
# Unpack its values into separate variables.
# Explain why you cannot change an element of a tuple.


# ------------------------------------------------------------
# 12. SETS
# ------------------------------------------------------------

# Sets store unique elements.
departments = {"Sales", "HR", "Finance", "Sales"}
print(departments)  # Duplicate values are removed.

departments.add("Analytics")
departments.update(["IT", "Marketing"])
print(departments)

departments.discard("HR")
print(departments)

# Set operations.
online_students = {"Aarav", "Riya", "Kabir"}
offline_students = {"Riya", "Meera", "Kabir"}

print(online_students | offline_students)  # Union
print(online_students & offline_students)  # Intersection
print(online_students - offline_students)  # Difference
print(online_students ^ offline_students)  # Symmetric difference

# Membership and unique values.
print("Aarav" in online_students)

cities = ["Mumbai", "Delhi", "Mumbai", "Pune", "Delhi"]
unique_cities = set(cities)
print(unique_cities)

# Set iteration order is not guaranteed.
# Use sorted(unique_cities) for a sorted list.

# TODO 12:
# Find unique customer IDs in a list.
# Find customers who purchased both product A and product B.
# Find customers who purchased A but not B.
# Find customers who purchased either A or B, but not both.


# ------------------------------------------------------------
# 13. DICTIONARIES
# ------------------------------------------------------------

# Dictionaries store key-value pairs.
employee = {
    "id": "E101",
    "name": "Riya",
    "department": "Analytics",
    "salary": 42000
}

print(employee)
print(employee["name"])
print(employee.get("salary"))
print(employee.get("age", "Not available"))

# Add or update values.
employee["city"] = "Mumbai"
employee["salary"] = 45000

# Delete a key.
employee.pop("city")

print(employee)

# View keys, values and key-value pairs.
print(employee.keys())
print(employee.values())
print(employee.items())

for key, value in employee.items():
    print(key, ":", value)

# Count category frequencies.
cities = ["Mumbai", "Pune", "Mumbai", "Delhi", "Pune", "Mumbai"]
city_count = {}

for city in cities:
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print(city_count)

# Dictionary comprehension.
squares = {number: number ** 2 for number in range(1, 6)}
print(squares)

# TODO 13:
# Create a dictionary for five products and their prices.
# Update the price of one product.
# Calculate the total value of all products.
# Count the number of times each word appears in a sentence.
# Find the employee with the highest salary from a list
# of employee dictionaries.


# ------------------------------------------------------------
# 14. NESTED DATA STRUCTURES
# ------------------------------------------------------------

# A list of dictionaries resembles a small data table.
employees = [
    {"name": "Aarav", "department": "Sales", "salary": 30000},
    {"name": "Riya", "department": "Analytics", "salary": 45000},
    {"name": "Kabir", "department": "Sales", "salary": 35000}
]

for employee in employees:
    print(employee["name"], employee["salary"])

# Filter employees.
for employee in employees:
    if employee["salary"] > 32000:
        print(employee["name"])

# Aggregate salaries.
total_salary = sum(employee["salary"] for employee in employees)
print("Total salary:", total_salary)

# TODO 14:
# Calculate average salary.
# Find the highest-paid employee.
# Calculate total salary department-wise.
# Display employees whose salary is above average.
# Count employees in each department.


# ------------------------------------------------------------
# 15. FUNCTIONS
# ------------------------------------------------------------

# Basic function.
def greet():
    print("Welcome to Python!")

greet()

# Function with parameters.
def greet_student(name):
    print(f"Welcome, {name}!")

greet_student("Riya")

# Function with a return value.
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(250, 4)
print(total)

# Default parameter.
def calculate_discount(amount, percentage=10):
    return amount * percentage / 100

print(calculate_discount(1000))
print(calculate_discount(1000, 20))

# Keyword arguments.
def employee_details(name, department):
    print(name, department)

employee_details(department="Analytics", name="Aarav")

# Return multiple values as a tuple.
def calculate_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = calculate_stats([10, 20, 30])
print(minimum, maximum, total)

# Local variables exist within their function scope.
def example():
    message = "Local variable"
    print(message)

example()

# TODO 15:
# Write a function to calculate simple interest.
# Write a function to check whether a number is even.
# Write a function that returns the average of a list.
# Write a function that accepts a list and returns only
# the values greater than a given threshold.
# Write a function to calculate net salary after deductions.


# ------------------------------------------------------------
# 16. LAMBDA FUNCTIONS
# ------------------------------------------------------------

# Lambda functions are small anonymous functions.
square = lambda number: number ** 2
print(square(5))

add = lambda a, b: a + b
print(add(10, 20))

# Sort tuples by the second value.
products = [("Laptop", 60000), ("Mouse", 800), ("Phone", 30000)]
products_sorted = sorted(products, key=lambda item: item[1])
print(products_sorted)

# Sort dictionaries by salary.
employees = [
    {"name": "Aarav", "salary": 30000},
    {"name": "Riya", "salary": 45000},
    {"name": "Kabir", "salary": 35000}
]

employees_sorted = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)

print(employees_sorted)

# map() applies a function to each item.
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda number: number ** 2, numbers))
print(squared_numbers)

# filter() selects items matching a condition.
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)

# TODO 16:
# Use lambda to calculate the cube of a number.
# Sort products by price from highest to lowest.
# Use map() to increase every price by 10%.
# Use filter() to find sales greater than 5000.
# Use sorted() and lambda to rank employees by salary.


# ------------------------------------------------------------
# 17. USEFUL BUILT-IN FUNCTIONS
# ------------------------------------------------------------

values = [12, 5, 30, 8, 20]

print(len(values))
print(sum(values))
print(min(values))
print(max(values))
print(sorted(values))
print(any(value > 25 for value in values))
print(all(value > 0 for value in values))

# zip() combines corresponding items.
names = ["Aarav", "Riya", "Kabir"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(name, score)

# Convert parallel lists into a dictionary.
score_dictionary = dict(zip(names, scores))
print(score_dictionary)

# TODO 17:
# Use any() to check whether any sales value is negative.
# Use all() to check whether every score is at least 40.
# Use zip() to combine product names and prices.
# Use enumerate() to print numbered rows of a list.


# ------------------------------------------------------------
# 18. BASIC EXCEPTION HANDLING
# ------------------------------------------------------------

# Handle invalid user input safely.
user_input = "abc"

try:
    number = int(user_input)
    print(number * 2)
except ValueError:
    print("Please provide a valid integer.")

# Handle division by zero.
try:
    result = 100 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# finally executes whether an exception occurs or not.
try:
    number = int("25")
    print(number)
except ValueError:
    print("Invalid number.")
finally:
    print("Operation finished.")

# TODO 18:
# Convert a string to a float using try-except.
# Handle division by zero in a calculator.
# Explain the difference between a syntax error and
# a runtime exception.


# ------------------------------------------------------------
# 19. DATA ANALYST LOGIC CHALLENGES
# ------------------------------------------------------------

# Challenge 1: Sales summary.
sales = [1200, 4500, 3000, 5200, 1800]

# TODO:
# Calculate total sales, average sales, highest sales,
# lowest sales and number of days above average.


# Challenge 2: Employee analysis.
employees = [
    {"name": "Aarav", "department": "Sales", "salary": 30000},
    {"name": "Riya", "department": "Analytics", "salary": 45000},
    {"name": "Kabir", "department": "Sales", "salary": 35000},
    {"name": "Meera", "department": "HR", "salary": 40000}
]

# TODO:
# Calculate average salary.
# Find the highest-paid employee.
# Count employees department-wise.
# Calculate total salary department-wise.
# Display employees earning above average salary.


# Challenge 3: Customer purchase analysis.
customer_orders = [
    {"customer": "A", "amount": 1200},
    {"customer": "B", "amount": 500},
    {"customer": "A", "amount": 800},
    {"customer": "C", "amount": 2500},
    {"customer": "B", "amount": 1500}
]

# TODO:
# Calculate total spending for each customer.
# Find the highest-spending customer.
# Count unique customers.
# Find customers with total spending above 1500.


# Challenge 4: Data cleaning.
raw_names = [" riya ", "AARAV", "", " kabir ", "RIYA", "   "]

# TODO:
# Remove empty or whitespace-only entries.
# Remove extra spaces.
# Convert names to title case.
# Identify unique cleaned names.
# Explain why cleaning should happen before analysis.


# Challenge 5: Business decision.
monthly_revenue = [50000, 65000, 48000, 80000, 72000]
monthly_expenses = [35000, 40000, 39000, 50000, 45000]

# TODO:
# Calculate monthly profit.
# Calculate total profit and average profit.
# Identify the month with maximum profit.
# Count months with profit above 25000.
# Calculate profit margin as a percentage:
# profit_margin = profit / revenue * 100

