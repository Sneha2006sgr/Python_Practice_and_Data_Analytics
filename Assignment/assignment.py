# Q1. Electricity Bill Calculator
# A residential electricity board calculates bills based on the following units consumed.
# Units consumed	Rate per unit
# First 100 units	₹3
# Next 100 units	₹5
# Above 200 units	₹8
# Write a Python program to accept the number of units consumed and calculate the electricity bill using conditional statements.
# Requirements:
# - Apply the rates progressively across the different slabs.
# - If units exceed 200, charge ₹8 only for the units above 200.
# - Reject negative unit values.
# - Display the total bill.
# Example: Input: 250 → Bill: ₹900

# ------------------------------------------------------------------------------------------------------------------

# Q2. ATM Withdrawal System
# Create a simple ATM simulation with an initial balance of ₹10,000.
# The user can repeatedly choose to:
# - Check balance
# - Deposit money
# - Withdraw money
# - Exit
# Use a loop to keep the program running until the user exits.
# Conditions:
# - Deposits must be positive.
# - Withdrawals must not exceed the available balance.
# - Invalid menu choices should display an error message.
# - Display the updated balance after every successful transaction.

# ------------------------------------------------------------------------------------------------------------------

# Q3. Number Pattern and Multiplication Table
# Write a program that accepts a number and prints its multiplication table up to 10.
# Extend the program to print tables from 1 to the entered number.
# Example: If the input is 3, print the multiplication tables of 1, 2 and 3.
# Use nested loops and format the output neatly.

# ------------------------------------------------------------------------------------------------------------------

# Q4. Number Analysis
# Accept a positive integer and determine:
# - Whether it is even or odd.
# - Whether it is prime.
# - Whether it is a palindrome.
# - The sum of its digits.
# - The reverse of the number.
# Solve the problem using loops and conditional statements. Do not convert the number into a string for the reversal and palindrome checks.

# ------------------------------------------------------------------------------------------------------------------

# Q5. Student Marks Analyzer
# Store the marks of 10 students in a list.
# Write a program to calculate:
# - Highest and lowest marks.
# - Average marks.
# - Number of students who passed, assuming 40 is the passing mark.
# - Number of students who scored above the class average.
# - The second-highest distinct mark.
# Handle duplicate marks correctly. Assume marks are between 0 and 100.

# ------------------------------------------------------------------------------------------------------------------

# Q6. Remove Duplicate Registrations
# A workshop registration system stores participant IDs in a list, but some participants register multiple times.
# Example:
# ["P101", "P102", "P101", "P103", "P102", "P104"]
# Perform the following tasks:
# 1. Identify the unique participant IDs using a set.
# 2. Count the number of duplicate registrations.
# 3. Display the total number of unique participants.
# 4. Create a list of unique IDs while preserving the original registration order.
# Explain why set alone cannot guarantee preservation of the original order.

# ------------------------------------------------------------------------------------------------------------------

# Q7. Employee Records Using Tuples
# Store employee records as tuples containing:
# (employee_id, employee_name, department, salary)
# Create a collection of at least five employees and perform the following operations:
# - Display employees belonging to the IT department.
# - Find the employee earning the highest salary.
# - Calculate the average salary.
# - Count employees whose salary exceeds ₹50,000.
# - Explain why tuples are suitable for individual employee records when the fields should not be changed accidentally.

# ------------------------------------------------------------------------------------------------------------------

# Q8. Product Inventory Dictionary
# Create a dictionary in which product names are keys and their available quantities are values.
# Example:
# {"Laptop": 10, "Mouse": 25, "Keyboard": 15}
# Implement these operations:
# - Add a new product.
# - Update an existing product's quantity.
# - Search for a product.
# - Reduce stock after a sale.
# - Display products with zero stock.
# - Display products whose quantity is below five.
# Prevent stock from becoming negative and handle products that do not exist.

# ------------------------------------------------------------------------------------------------------------------

# Q9. Reusable Calculator
# Create separate functions for addition, subtraction, multiplication, division and modulus.
# Requirements:
# - Accept two numbers and an operator.
# - Return the calculated result from the appropriate function.
# - Handle division and modulus by zero.
# - Use a menu-driven loop to allow multiple calculations.
# - Stop only when the user selects Exit.
# Challenge: Use a dictionary to map operators to their corresponding functions.

# ------------------------------------------------------------------------------------------------------------------

# Q10. Custom Sorting Using Lambda
# Consider the following student data:
# students = [    ("Aarav", 82),    ("Diya", 95),    ("Kabir", 76),    ("Meera", 95),    ("Rohan", 68)]



# Perform the following operations using lambda functions with sorted():
# 1. Sort students by marks in ascending order.
# 2. Sort students by marks in descending order.
# 3. Sort students alphabetically by name.
# 4. Sort by marks descending, then by name alphabetically for tied marks.
# Explain the purpose of the key and reverse parameters.

# ------------------------------------------------------------------------------------------------------------------

# Q11. Employee Salary Processing
# Store employee information in a list of dictionaries, including name, department and salary.
# Write a program that:
# - Uses a function to filter employees earning more than ₹40,000.
# - Uses a lambda expression to sort employees by salary.
# - Uses a loop to calculate the total monthly salary expense.
# - Uses conditional statements to classify salary as Low (below ₹25,000), Medium (₹25,000–₹50,000) or High (above ₹50,000).
# Do not modify the original employee records while producing the sorted result.

# ------------------------------------------------------------------------------------------------------------------

# Q12. Function to Find Common Elements
# Write a function that accepts two lists and returns:
# - Elements common to both lists.
# - Elements present only in the first list.
# - Elements present only in the second list.
# - All unique elements from both lists.
# Use sets for membership operations.
# Challenge: Return all four results in a dictionary with meaningful keys.

# ------------------------------------------------------------------------------------------------------------------

# Q13. Online Shopping Cart
# Design a shopping cart using a dictionary where each product name maps to its price and quantity.
# Example structure:
# cart = {    "Notebook": {"price": 50, "quantity": 3},    "Pen": {"price": 10, "quantity": 5}}



# Implement functions to:
# - Add a product.
# - Update quantity.
# - Remove a product.
# - Calculate the subtotal.
# - Apply a 10% discount when the subtotal exceeds ₹1,000.
# - Display the final invoice.
# Handle invalid quantities and prevent the same product from being unintentionally duplicated.

# ------------------------------------------------------------------------------------------------------------------

# Q14. Attendance Management System
# Three classes have attendance records stored as sets of student IDs.
# class_a = {"S01", "S02", "S03", "S04"}class_b = {"S03", "S04", "S05", "S06"}class_c = {"S02", "S04", "S06", "S07"}



# Find:
# 1. Students present in all three classes.
# 2. Students present in at least two classes.
# 3. Students present only in Class A.
# 4. Students present in any class.
# 5. Students present in exactly one class.
# Use set operations and, where required, loops or functions to count how often each student appears.

# ------------------------------------------------------------------------------------------------------------------

# Q15. Word Frequency Counter
# Accept a paragraph from the user and count the occurrences of every word.
# Requirements:
# - Convert words to lowercase.
# - Ignore common punctuation.
# - Store the results in a dictionary.
# - Display the most frequently occurring word.
# - Display words that appear only once.
# - Sort the output by frequency.
# Example: "Python is easy. Python is useful."
# Expected counts: python: 2, is: 2, easy: 1, useful: 1.
# You may use Python's built-in string module for punctuation handling. No external libraries are required.

# ------------------------------------------------------------------------------------------------------------------

# Q16. Library Book Management
# Create a library system using a dictionary of books, where each book has a title, author, availability status and number of copies.
# Create functions to:
# - Add a book.
# - Search for a book by title.
# - Issue a book.
# - Return a book.
# - Display all available books.
# - Count the total number of available copies.
# Apply conditions to prevent issuing unavailable books or returning books that were not issued. Use a loop to keep the system running until the librarian exits.

# ------------------------------------------------------------------------------------------------------------------

# Q17. Expense Tracker
# Build a personal expense tracker using a list of dictionaries.
# Each expense should contain:
# - Expense ID
# - Category
# - Amount
# - Payment mode
# Your program must:
# 1. Add and remove expenses using functions.
# 2. Calculate total spending.
# 3. Calculate category-wise spending.
# 4. Identify the highest expense.
# 5. Find all expenses above a user-defined limit.
# 6. Display unique categories using a set.
# 7. Sort expenses by amount using a lambda function.
# 8. Warn the user when total spending exceeds a monthly budget.
# Validate that expense amounts are positive.
# Critical-thinking extension: How would you prevent two expenses from having the same ID?

# ------------------------------------------------------------------------------------------------------------------

# Q18. Quiz Application
# Create a quiz application with at least 10 questions.
# Each question should contain the question text, options, correct answer and marks.
# Use suitable data structures to store the quiz.
# Requirements:
# - Display questions one at a time using a loop.
# - Accept answers from the user.
# - Validate the answer.
# - Calculate the score using a function.
# - Use conditions to determine whether the user passed.
# - Store the result of each question.
# - Display the final score, percentage and incorrect answers.
# - Allow the user to retake the quiz.
# Challenge: Randomize the order of questions using the built-in random module.

# ------------------------------------------------------------------------------------------------------------------

# Q19. Password Strength Analyzer
# Create a program that evaluates a password based on the following rules:
# - At least eight characters long.
# - Contains at least one uppercase letter.
# - Contains at least one lowercase letter.
# - Contains at least one digit.
# - Contains at least one special character.
# Create a function that checks each condition and returns a dictionary containing each rule and its result.
# Classify the password as Weak, Moderate or Strong based on the number of conditions satisfied.
# Challenge: Reject passwords containing spaces and explain the difference between checking password strength and verifying a user's identity.

# ------------------------------------------------------------------------------------------------------------------

# Q20. Student Performance Management
# Create a student management system using a dictionary of student records.
# Each record should contain a student ID, name, marks in five subjects and attendance percentage.
# Write functions to:
# - Add and search for a student.
# - Calculate total and average marks.
# - Calculate the percentage.
# - Assign grades using conditional statements.
# - Identify students who failed in any subject.
# - Identify students with attendance below 75%.
# - Sort students by average marks using lambda.
# - Display the top three students.
# - Find the subject with the highest class average.
# Define a clear grading scale and handle ties when determining the top three students.
# Critical-thinking extension: Should a student with a high average but attendance below 75% be classified as eligible? Implement a configurable eligibility rule.

# ------------------------------------------------------------------------------------------------------------------

# Q21. Inventory Reorder Alert
# A store maintains product names, stock quantities and minimum stock levels in a dictionary.
# Build a system that:
# - Accepts new stock entries and sales.
# - Updates the inventory after every transaction.
# - Displays products that need reordering.
# - Calculates the total value of the inventory.
# - Identifies the product with the highest stock value.
# - Prevents sales when sufficient stock is unavailable.
# - Uses functions to separate transaction logic from reporting logic.
# Challenge: Maintain a transaction history using tuples and identify products that have never been sold.

# ------------------------------------------------------------------------------------------------------------------

# Q22. Duplicate and Similar Data Detection
# A registration system stores records containing a person's name, email and phone number.
# Develop a program that identifies:
# - Exact duplicate records.
# - Different records sharing the same email.
# - Different records sharing the same phone number.
# - Records with missing values.
# Use lists, sets, dictionaries, loops and functions.
# Critical-thinking extension: Explain why checking only the person's name is insufficient to identify duplicate registrations. Treat email and phone normalization consistently before comparing them.

# ------------------------------------------------------------------------------------------------------------------

# Q23. Smart Parking Lot System
# Design a parking management system with a fixed number of parking slots.
# Each vehicle record should contain its registration number, vehicle type and entry time.
# Implement:
# - Vehicle entry and exit.
# - Slot availability checking.
# - Prevention of duplicate vehicle entries.
# - Parking fee calculation based on the duration.
# - Different hourly rates for cars and bikes.
# - Daily revenue calculation.
# - A report of currently parked vehicles.
# - A history of completed parking sessions.
# Use functions, dictionaries, sets, tuples, loops and conditional statements.
# Rules: Define the billing policy yourself, including how partial hours are charged. Handle invalid exits and full parking capacity.

# ------------------------------------------------------------------------------------------------------------------

# Q24. Mini Banking System with Transaction History
# Develop a banking simulation that supports multiple accounts.
# Each account should have an account ID, holder name, balance and transaction history.
# Features:
# - Create an account.
# - Deposit and withdraw money.
# - Transfer money between accounts.
# - Check account balance.
# - Display transaction history.
# - Calculate total money held across all accounts.
# - Identify accounts with balances below a minimum threshold.
# Store transaction records as tuples and account data in dictionaries.
# Critical-thinking requirements:
# - Prevent negative deposits and invalid withdrawals.
# - Ensure transfers debit and credit the correct accounts.
# - Validate both account IDs before a transfer.
# - Avoid modifying balances if any transfer validation fails.
# - Use functions for every major operation.

# ------------------------------------------------------------------------------------------------------------------

# Q25. Course Recommendation Engine
# A learning platform stores courses, student interests and completed courses.
# Build a basic recommendation system that recommends courses based on overlapping interests.
# For each student:
# - Store interests as a set.
# - Store completed course IDs as a set.
# - Store course details in a dictionary.
# - Calculate the number of matching interests for each course.
# - Exclude courses already completed.
# - Rank the remaining courses using a lambda function.
# - Display the top three recommendations.
# Critical-thinking extension: What should happen if two courses have the same number of matching interests? Add a secondary sorting criterion and explain why the recommendation is only a simple rule-based system, not a guarantee of learning success.

# ------------------------------------------------------------------------------------------------------------------

# Q28. Mini Data Analysis Without Pandas
# A company provides a list of dictionaries representing sales records. Each record contains the salesperson's name, region, product and sales amount.
# Build a report generator that calculates:
# - Total revenue.
# - Region-wise revenue.
# - Product-wise revenue.
# - Best-performing salesperson.
# - Average sale amount.
# - Number of transactions above the average.
# - Top three sales transactions.
# - Regions with no sales records.
# - Duplicate transaction IDs, if transaction IDs are included.
# Use only core Python data structures and functions.
# Critical-thinking extension: Explain why the average transaction amount and average revenue per salesperson are different metrics. Handle empty datasets and tied results.

# ------------------------------------------------------------------------------------------------------------------

