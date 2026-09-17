# Name:Caleb
# Period: pm

# ============================================================
# Python Skills Check — Slides 61–116
# CONDITIONALS & FUNCTIONS — CHALLENGE VERSION
# ============================================================

# DIRECTIONS
# ============================================================
# - I recommend you create a repo first and clone it.
# - Drag this file into your repo and push when you are done.
#
# Complete each task underneath its directions.
#
# RULES:
# - Use ONLY concepts we have learned in class.
# - Use the EXACT variable and function names provided.
# - Do not delete the directions.
# - Your entire Python file must run without errors.
# - Do NOT manually type an answer that Python should determine.
# - Pay attention to indentation.
# - Read carefully. MANY questions are intentionally tricky.
# - Unless a task says otherwise, do NOT use min() or max().
# - Your conditions should work even if the variable values are changed.
#
# IMPORTANT:
# Some questions are designed so that the ORDER of your conditions matters.
# Some questions have edge cases such as ties or boundary values.
# Test your logic carefully.


# ============================================================
# SECTION 1 — COMPARISON WARM-UP
# ============================================================

# TASK 1:
# Create:
#
# number_one = 25
# number_two = 40
#
# Write an if statement that prints:
#
# number_two is greater
#
# ONLY if number_two is greater than number_one.

number_one = 25
number_two = 40
if number_two > number_one:
    print('number two is greater')


# TASK 2:
# Create:
#
# score = 80
#
# Print:
# Passing score
#
# if score is GREATER THAN OR EQUAL TO 70.

score = 80
if score >=70:
    print('passing score')


# TASK 3:
# Create:
#
# lives = 0
#
# Print:
# Game over
#
# ONLY if lives is exactly 0.

lives = 0
if lives == 0:
    print('game over')


# TASK 4:
# Create:
#
# username = "student"
#
# Print:
# Different username
#
# ONLY if username is NOT equal to "admin".

username = "student"
if username != "admin":
    print('different username')


# ============================================================
# SECTION 2 — BOUNDARIES & ORDER MATTER
# ============================================================

# TASK 5:
# Create:
#
# age = 18
#
# Print:
# Child       if age is under 13
# Teen        if age is 13 through 17
# Adult       if age is 18 through 64
# Senior      if age is 65 or older
#
# Use if / elif / else.
#
# THINK:
# Which condition should be checked first?

age = 18
if age < 13:
    print('child')
elif age >= 13 and age <= 17:
    print('teen')
elif age >= 18 and age <= 64:
    print('adult')
else:
    print('senior')


# TASK 6:
# Create:
#
# grade = 90
#
# Print:
# A if grade is 90 or higher
# B if grade is 80–89
# C if grade is 70–79
# D if grade is 60–69
# F if grade is below 60
#
# IMPORTANT:
# grade = 90 should print ONLY:
# A

grade = 90
if grade < 60:
    print('f')
elif grade >= 60 and grade <= 69:
    print('d')
elif grade >= 70 and grade <= 79:
    print('c')
elif grade >= 80 and grade <= 89:
    print('b')
else:
    print('a')


# TASK 7:
# Create:
#
# temperature = 70
#
# Print:
# Cold       if below 50
# Mild       if 50 through 69
# Warm       if 70 through 89
# Hot        if 90 or higher
#
# Be careful with 50, 70, and 90.

temperature = 70
if temperature < 50:
    print('cold')
elif temperature >= 50 and temperature < 70:
    print('mild')
elif temperature >= 70 and temperature < 90:
    print('warm')
else:
    print("hot")


# TASK 8:
# Create:
#
# speed = 65
#
# Print:
# Too Slow       if speed is below 25
# Normal         if speed is 25 through 65
# Speeding       if speed is 66 through 80
# Reckless       if speed is above 80
#
# The value 65 must print:
# Normal

speed = 65
if speed < 25:
    print('too slow')
elif speed >= 25 and speed <= 65:
    print('normal')
elif speed >= 66 and speed <= 80:
    print('speeding')
else:
    print('reckless')


# TASK 9:
# Create:
#
# amount = 100
#
# Print:
# Small purchase       if amount is below 25
# Medium purchase      if amount is 25 through 99
# Large purchase       if amount is 100 through 499
# Huge purchase        if amount is 500 or more
#
# THINK carefully about your comparison operators.

amount = 100
if amount < 25:
    print('small purchase')
elif amount >= 25 and amount <= 99:
    print('medium purchase')
elif amount >= 100 and amount <= 499:
    print('large amount')
else:
    print('huge purchase')


# ============================================================
# SECTION 3 — AND / OR THINKING
# ============================================================

# TASK 10:
# Create:
#
# age = 16
# has_ticket = True
#
# Print:
# You may enter
#
# ONLY if age is at least 13 AND has_ticket is True.
#
# Otherwise print:
# Entry denied

age = 16
has_ticket = True
if age >= 13 and has_ticket == True:
    print('you may enter')
else:
    print('entry denied')


# TASK 11:
# Create:
#
# temperature = 91
#
# Print:
# Extreme temperature
#
# if temperature is below 32 OR above 90.
#
# Otherwise print:
# Normal temperature

temperature = 91
if temperature < 32 or temperature > 90:
    print('extreme temperature')
else:
    print('normal temperature')


# TASK 12:
# Create:
#
# username = "admin"
# password = "python123"
#
# Print:
# Access granted
#
# ONLY if BOTH values are correct.
#
# Otherwise print:
# Access denied

username = "admin"
password = "python123"
if username == "admin" and password == "python123":
    print('access granted')
else:
    print('access denied')


# TASK 13:
# Create:
#
# age = 70
# has_membership = False
#
# Print:
# Discount applies
#
# if the person is 65 or older OR has_membership is True.
#
# Otherwise print:
# No discount

age = 70
has_membership = False
if age >= 65 or has_membership == True:
    print('discount applies')
else:
    print('no discount')


# TASK 14:
# Create:
#
# number = 25
#
# Print:
# In range
#
# if number is from 10 through 30 INCLUDING 10 and 30.
#
# Otherwise print:
# Out of range

number = 25
if number >= 10 and number <= 30:
    print('in range')
else:
    print('out of range')


# TASK 15:
# Create:
#
# number = 10
#
# Print:
# Outside middle range
#
# if number is LESS THAN 20 OR GREATER THAN 80.
#
# Otherwise print:
# Inside middle range
#
# Test mentally with:
# 10
# 50
# 90

number = 10
if number < 20 or number > 80:
    print('outside middle range')
else:
    print('inside middle range')


# ============================================================
# SECTION 4 — HIGHEST / LOWEST / MIDDLE
# ============================================================

# TASK 16:
# Create:
#
# a = 12
# b = 7
# c = 19
#
# WITHOUT using max(), determine which variable contains
# the HIGHEST value.
#
# Print:
# a is highest
# OR
# b is highest
# OR
# c is highest

a = 1100
b = 2000
c = 19
if a > b and a > c:
    print('a is highest')
else:
    if b > a and b > c:
        print('b is highest')
    else:
        if c > a and c > b:
            print('c is highest')


# TASK 17:
# Create:
#
# x = 44
# y = 13
# z = 28
#
# WITHOUT using min(), determine which variable contains
# the LOWEST value.
#
# Print the correct variable name followed by:
# is lowest

x = 44
y = 13
z = 28
if x < y and x < z:
    print('x is the lowest')
else:
    if y < x and y < z:
        print('y is the lowest')
    else:
        if z < x and z < y:
            print('z is the lowest')


# TASK 18:
# Create:
#
# num1 = 10
# num2 = 30
# num3 = 20
#
# WITHOUT using min(), max(), or sorting,
# determine the MIDDLE value.
#
# Print:
# Middle: [value]
#
# HINT:
# The middle value is not the highest and not the lowest.

num1 = 50
num2 = 100
num3 = 20
if num1 > num2 and num1 < num3 or num1 < num2 and num1 > num3:
    print(f'middle: {num1}')
else:
    if num2 > num1 and num2 < num3 or num2 < num1 and num2 > num3:
        print(f'middle: {num2}')
    else:
        if num3 > num2 and num3 < num1 or num3 < num2 and num3 > num1:
            print(f'middle: {num3}')


# TASK 19:
# Create:
#
# first = 20
# second = 20
# third = 8
#
# Determine what is highest.
#
# Your program must correctly handle the tie.
#
# Possible outputs:
# first is highest
# second is highest
# third is highest
# first and second are tied for highest
# first and third are tied for highest
# second and third are tied for highest
# all three are tied

first = 28
second = 20
third = 28
if first > second and first > third:
    print('first is highest')
elif first == second == third:
    print('all three are tied')
elif first > third and first == second:
    print('first and second are tied for highest')
elif first > second and first == third:
    print('first and third are tied for highest')
else:
    if second > first and second > third:
        print('second is highest')
    elif second > first and second == third:
        print('second and third are tied for highest')
    else:
        if third > first and third > second:
            print('third is highest')


# TASK 20:
# Create:
#
# first = 5
# second = 5
# third = 5
#
# Determine whether:
#
# - all three are equal
# - exactly two are equal
# - none are equal
#
# Print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# Your code should still work if the values are changed.

first = 3
second = 5
third = 4
if first == second == third:
    print('all three are equal')
elif first == second and first != third or first == third and first != second:
    print('exactly two equal')
else:
    if second == first and second != third or second == third and second != first:
        print('exactly two equal')
    else:
        print('all different')


# TASK 21:
# Create:
#
# a = 9
# b = 4
# c = 9
#
# Determine whether AT LEAST TWO numbers match.
#
# Print:
# A match exists
#
# Otherwise print:
# No match

a = 10
b = 9
c = 9
if a == b or a == c:
    print('a match exists')
elif b == c:
    print('a match exists')
else: print('no match')


# TASK 22:
# Create:
#
# a = 14
# b = 7
# c = 20
#
# Determine whether a is BETWEEN b and c.
#
# Print:
# a is between b and c
#
# if that is true.
#
# Otherwise print:
# a is not between b and c
#
# IMPORTANT:
# Your code should still work if b is greater than c.

a = 14
b = 7
c = 20
if a > b and a < c or a < b and a > c:
    print('a is between b and c')
else:
    print('a is not between b and c')


# TASK 23:
# Create:
#
# a = 50
# b = 20
# c = 80
#
# Determine whether b is the lowest AND c is the highest.
#
# If BOTH are true, print:
# Correct order
#
# Otherwise print:
# Different order

a = 50
b = 20
c = 80
if b < a and b < c and c > a:
    print('correct order')
else:
    print('different order')


# ============================================================
# SECTION 5 — USER INPUT LOGIC
# ============================================================

# TASK 24:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# first_number
# second_number
# third_number
#
# WITHOUT using min() or max(), print the LOWEST number.

first_number = int(input('give first whole number'))
second_number = int(input('give second whole number'))
third_number = int(input('give third whole number'))
if first_number < second_number and first_number < third_number:
    print(f'first number is the lowest: {first_number}')
elif second_number < first_number and second_number < third_number:
    print(f'second number is the lowest: {second_number}')
elif third_number < first_number and third_number < second_number:
    print(f'third number is the lowest: {third_number}')


# TASK 25:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# value1
# value2
# value3
#
# WITHOUT using min() or max(), print the HIGHEST number.

value1 = int(input('give me your first whole number'))
value2 = int(input('give me your second whole number'))
value3 = int(input('give me your third whole number'))
if first_number > second_number and first_number > third_number:
    print(f'first number is the highest: {first_number}')
elif second_number > first_number and second_number > third_number:
    print(f'second number is the highest: {second_number}')
elif third_number > first_number and third_number > second_number:
    print(f'third number is the highest: {third_number}')


# TASK 26:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# n1
# n2
# n3
#
# Determine whether the user entered them in STRICTLY increasing order.
#
# Example:
# 3, 8, 10 -> Increasing
#
# 3, 3, 10 -> NOT Increasing
#
# Print:
# Increasing
# OR
# Not increasing

n1 = int(input('give me your first whole number pls'))
n2 = int(input('give me your second whole number pls'))
n3 = int(input('give me your third whole number pls'))
if n3 > n2 and n2 > n1:
    print('increasing')
else:
    print('not increasing')


# TASK 27:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# n1
# n2
# n3
#
# Determine whether the numbers are in STRICTLY decreasing order.
#
# Print:
# Decreasing
# OR
# Not decreasing

n1 = int(input('pls give your first whole number'))
n2 = int(input('pls give your second whole number'))
n3 = int(input('pls give your third whole number'))
if n1 > n2 and n2 > n3:
    print('decreasing')
else:
    print('not decreasing')


# TASK 28:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# a
# b
# c
#
# Print:
# All same
# if all three match
#
# Two same
# if exactly two match
#
# All different
# if none match

a = int(input('GIVE ME YOUR FIRST WHOLE NUMBER'))
b = int(input('GIVE ME YOU SECOND WHOLE NUMBER'))
c = int(input('GIVE ME YOU THIRD WHOLE NUMBER'))
if a == b == c:
    print('all three of your numebrs match')
elif a == b and a != c or a == c and a != b or b == c and b != a:
    print('two of your numbers match')
else:
    print('none match lol')


# TASK 29:
# Ask the user for a score from 0 to 100.
#
# Store it in:
#
# user_score
#
# FIRST determine if the score is valid.
#
# If it is below 0 OR above 100, print:
# Invalid score
#
# Otherwise print the letter grade:
# A, B, C, D, or F
#
# THINK:
# You should not assign a letter grade to an invalid score.

user_score = int(input('give me a score from 0 to 100'))
if user_score < 0 or user_score > 100:
    print('invalid score')
else:
    if user_score < 60:
        print('f')
    elif user_score >= 60 and user_score < 70:
        print('d')
    elif user_score >= 70 and user_score < 80:
        print('c')
    elif user_score >= 80 and user_score < 90:
        print('b')
    else:
        print('a')


# ============================================================
# SECTION 6 — FUNCTIONS BASICS
# ============================================================

# TASK 30:
# Create a function named:
#
# say_hello
#
# It should print:
# Hello!
#
# Call it once.

def say_hello():
    print('hello!')
say_hello()


# TASK 31:
# Create a function named:
#
# greet_student
#
# Give it ONE parameter:
#
# name
#
# Print:
# Hello [name]
#
# Call it THREE times using different names.

def greet_student(name):
    print('hello', name)
greet_student('caleb')


# TASK 32:
# Create a function named:
#
# add_three
#
# Give it THREE parameters:
#
# a
# b
# c
#
# Print the sum of all three.
#
# Call it at least TWO times.

def add_three(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum
print(add_three(1,100,200))
print(add_three(289374,38459,239874293))


# ============================================================
# SECTION 7 — FUNCTIONS + CONDITIONALS
# ============================================================

# TASK 33:
# Create a function named:
#
# check_number
#
# Give it ONE parameter:
#
# number
#
# Print:
# Positive
# Negative
# or
# Zero
#
# Call it using:
# 10
# -5
# 0

def check_number(number):
    if number > 0:
        print('positive')
    elif number < 0:
        print('negative')
    else:
        print('zero')

check_number(10)
check_number(-5)
check_number(0)


# TASK 34:
# Create a function named:
#
# check_even_odd
#
# Give it ONE parameter:
#
# number
#
# Print:
# Even
# OR
# Odd
#
# Test it at least FOUR times.

def check_even_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')
check_even_odd(1)
check_even_odd(2)
check_even_odd(3)
check_even_odd(4)


# TASK 35:
# Create a function named:
#
# ticket_type
#
# Give it ONE parameter:
#
# age
#
# Print:
# Child
# Teen
# Adult
# Senior
#
# using these ranges:
#
# Child: under 13
# Teen: 13–17
# Adult: 18–64
# Senior: 65+
#
# Test boundary values:
# 12
# 13
# 17
# 18
# 64
# 65

def ticket_type(age):
    if age < 13:
        print('child')
    elif age >= 13 and age < 18:
        print('teen')
    elif age >= 18 and age < 65:
        print('adult')
    else:
        print('senior')

ticket_type(12)
ticket_type(13)
ticket_type(17)
ticket_type(18)
ticket_type(64)
ticket_type(65)


# TASK 36:
# Create a function named:
#
# find_highest
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using max(), print the highest value.
#
# Test:
# find_highest(5, 20, 11)
# find_highest(100, 25, 60)
# find_highest(8, 9, 30)

def find_highest(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)
find_highest(5,20,11)
find_highest(100,25,60)
find_highest(8,9,30)



# TASK 37:
# Create a function named:
#
# find_lowest
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), print the lowest value.
#
# Test at least THREE times.

def find_lowest(a,b,c):
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    elif c < a and c < b:
        print(c)

find_lowest(1,2,3)
find_lowest(5,100,7)
find_lowest(324221312312,43636,1231212)


# TASK 38:
# Create a function named:
#
# find_middle
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), max(), or sorting,
# print the MIDDLE value.
#
# Test:
# find_middle(10, 30, 20)
# find_middle(100, 5, 50)
# find_middle(7, 9, 8)

def find_middle(a,b,c):
    if a > b and a < c or a < b and a > c:
        print(a)
    elif b > a and b < c or b < a and b > c:
        print(b)
    elif c > a and c < b or c < a and c > b:
        print(c)
find_middle(10, 30, 20)
find_middle(100, 5, 50)
find_middle(7, 9, 8)


# TASK 39:
# Create a function named:
#
# compare_three
#
# Give it THREE parameters:
#
# a
# b
# c
#
# Print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# Test all three situations.

def compare_three(a,b,c):
    if a ==b ==c:
        print('all equal')
    elif a ==b and a != c or a == c and a != b or b == c and b !=a:
        print('exactly two equal')
    else:
        print('all different')
compare_three(1,1,1)
compare_three(1,1,0)
compare_three(1,0,1)
compare_three(0,1,1)
compare_three(1,2,3)


# TASK 40:
# Create a function named:
#
# is_in_range
#
# Give it THREE parameters:
#
# number
# low
# high
#
# Print:
# In range
#
# if number is between low and high INCLUDING the endpoints.
#
# Otherwise print:
# Out of range
#
# IMPORTANT:
# Your function should still work if low and high
# are accidentally passed in backwards.
#
# Example:
# is_in_range(50, 100, 1)
#
# should still print:
# In range

def is_in_range(number, low, high):
    if number > low and number < high:
        print('in range')
    else:
        print('out of range')
is_in_range(50,100,1)

# ============================================================
# SECTION 8 — RETURN VALUES
# ============================================================

# TASK 41:
# Create a function named:
#
# multiply_numbers
#
# Give it TWO parameters:
#
# num1
# num2
#
# RETURN their product.
#
# Store the result of:
# multiply_numbers(6, 7)
#
# inside:
# multiplication_result
#
# Print multiplication_result.

def multiply_numbers(num1, num2):
    product = num1 * num2
    return product
multiplication_result = multiply_numbers(6,7)
print(multiplication_result)


# TASK 42:
# Create a function named:
#
# larger_number
#
# Give it TWO parameters:
#
# a
# b
#
# RETURN the larger value.
#
# If they are equal, RETURN that value.
#
# Store the result of:
# larger_number(15, 40)
#
# inside:
# bigger
#
# Print bigger.

def larger_number(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a
bigger = larger_number(15,40)
print(bigger)


# TASK 43:
# Create a function named:
#
# highest_of_three
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using max(), RETURN the highest value.
#
# Store:
# highest_of_three(18, 42, 27)
#
# inside:
# highest_result
#
# Print highest_result.

def highest_of_three(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
highest_result = highest_of_three(18,42,27)
print(highest_result)


# TASK 44:
# Create a function named:
#
# lowest_of_three
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), RETURN the lowest value.
#
# Test it at least THREE times.

def lowest_of_three(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    elif c<a and c<b:
        return c

print(lowest_of_three(1,5,3))
print(lowest_of_three(1213123,5,3543))
print(lowest_of_three(1,52131,3))


# TASK 45:
# Create a function named:
#
# middle_of_three
#
# Give it THREE parameters:
#
# a
# b
# c
#
# RETURN the middle value.
#
# Do NOT use min(), max(), or sorting.
#
# Test:
# middle_of_three(10, 30, 20)
# middle_of_three(50, 5, 25)
# middle_of_three(8, 7, 9)

def middle_of_three(a,b,c):
    if a > b and a < c or a > c and a < b:
        return a
    elif b > a and b < c or b > c and b < a:
        return b
    elif c > a and c < b or c > b and c < a:
        return c

print(middle_of_three(10, 30, 20))
print(middle_of_three(50, 5, 25))
print(middle_of_three(8, 7, 9))
    


# ============================================================
# SECTION 9 — RETURN + REUSE
# ============================================================

# TASK 46:
# Create a function named:
#
# get_highest
#
# Give it THREE parameters and RETURN the highest number.
#
# Then create another function named:
#
# get_lowest
#
# Give it THREE parameters and RETURN the lowest number.
#
# Use:
#
# a = 30
# b = 10
# c = 20
#
# Store the returned values in:
#
# highest
# lowest
#
# Then calculate:
#
# difference
#
# by subtracting lowest from highest.
#
# Print difference.
#
# IMPORTANT:
# Do NOT repeat the highest/lowest logic outside the functions.
def get_highest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
def get_lowest(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < a:
        return c
highest = get_highest(30,10,20)
lowest = get_lowest(30,10,20)
difference = highest - lowest
print(difference)


# TASK 47:
# Create:
#
# a = 9
# b = 4
# c = 15
#
# Use your get_highest() and get_lowest() functions from above.
#
# Store both returned values.
#
# Then determine if the difference between highest and lowest
# is greater than 10.
#
# Print:
# Large spread
#
# or:
# Small spread

a = 9
b = 4
c = 15
high = get_highest(a,b,c)
low = get_lowest(a,b,c)
dif = high - low
if dif > 10:
    print('large spread')
else:
    print('small spread')


# TASK 48:
# Create a function named:
#
# best_of_two
#
# Give it TWO parameters and RETURN the larger value.
#
# Then use it to determine the highest of THREE numbers
# WITHOUT writing a new three-number comparison.
#
# You should call best_of_two() more than once.
#
# Use:
# a = 12
# b = 50
# c = 31
#
# Store the final answer in:
#
# highest
#
# Print highest.
#
# THINK:
# How can one function call feed into another?

a = 12
b = 50
c = 31

def best_of_two(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

wow = best_of_two(a,b)
highest = best_of_two(wow,c)
print(highest)



# TASK 49:
# Create a function named:
#
# worst_of_two
#
# Give it TWO parameters and RETURN the smaller value.
#
# Use it more than once to find the LOWEST of:
#
# a = 22
# b = 5
# c = 17
#
# Store the final result in:
#
# lowest
#
# Print lowest.

def worst_of_two(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
a=22
b=5
c=17
wow2 = worst_of_two(a,b)
lowest = worst_of_two(wow2,c)


# ============================================================
# SECTION 10 — LOGIC CHALLENGES
# ============================================================

# TASK 50:
# Create:
#
# a = 12
# b = 7
# c = 19
#
# Determine whether b is the MIDDLE value.
#
# Print:
# b is middle
#
# or:
# b is not middle
#
# Do NOT calculate the middle value separately first.

a=12
b=7
c=19
if b > a and b < c or b < a and b > c:
    print('b is middle')
else:
    print('b is not middle')



# TASK 51:
# Create:
#
# a = 25
# b = 25
# c = 10
#
# Determine whether the HIGHEST value appears more than once.
#
# Print:
# Highest is tied
#
# or:
# Highest is unique

a = 25
b = 25
c = 10

tuff_string = "highest is unique"
tuff_string1 = "highest is tied"

if a > b and a > c:
    print(tuff_string)
elif b > a and b > c:
    print(tuff_string)
elif c > a and c > b:
    print(tuff_string)
else:
    print(tuff_string1)


# TASK 52:
# Create:
#
# a = 3
# b = 8
# c = 5
#
# Determine whether the numbers are:
#
# Strictly increasing
# Strictly decreasing
# Neither
#
# Print ONE result.

a=3
b=8
c=5
if a < b < c:
    print('strictly increasing')
elif a > b > c:
    print('strictly decreasing')
else:
    print('neither')


# TASK 53:
# Create:
#
# a = 5
# b = 5
# c = 10
#
# Determine whether the values are in NON-DECREASING order.
#
# This means each value may stay the same or get larger.
#
# Examples:
# 3, 3, 7 -> yes
# 3, 7, 7 -> yes
# 3, 7, 2 -> no
#
# Print:
# Non-decreasing
# OR
# Not non-decreasing

a = 5
b = 5
c = 10
if a < c:
    print('non-decreasing')
elif a > c:
    print('not non-decreasing')


# TASK 54:
# Create:
#
# age = 17
# has_permission = True
# has_ticket = False
#
# A person may enter if:
#
# - they are 18 or older
#
# OR
#
# - they are under 18 AND have_permission is True AND have_ticket is True
#
# Print:
# Entry allowed
#
# or:
# Entry denied
#
# Read this one carefully.

age = 17
has_permission = True
has_ticket = False

if age >= 18 or has_permission == True and has_ticket == True:
    print('entry allowed')
else:
    print('entry denied')


# TASK 55:
# Create:
#
# score = 88
# attendance = 92
#
# Print:
# Honors
#
# if score is at least 90 AND attendance is at least 90.
#
# Print:
# Pass
#
# if score is at least 70 AND attendance is at least 75,
# but the student did not qualify for Honors.
#
# Otherwise print:
# Fail
#
# Only ONE message should print.

score = 88
attendance = 92
if score >= 90 and attendance >= 90:
    print('honors')
elif score >= 70 and attendance >= 75:
    print('pass')
else:
    print('fail')


# ============================================================
# SECTION 11 — DEBUGGING CHALLENGES
# ============================================================

# TASK 56:
# The programmer wants exactly ONE result.
#
# Fix the code so score = 95 prints ONLY:
#
# Excellent
#
# score = 95
#
# if score >= 70:
#     print("Passing")
# if score >= 90:
#     print("Excellent")

score = 95
if score >= 70:
    print('passing')
elif score >= 90:
    print('excellent')


# TASK 57:
# The programmer wants 18 to count as Adult.
#
# Fix the logic.
#
# age = 18
#
# if age > 18:
#     print("Adult")
# else:
#     print("Minor")

age = 18
if age >= 18:
    print('adult')
else:
    print('minor')


# TASK 58:
# The programmer wants numbers from 10 through 20,
# INCLUDING 10 and 20, to print:
#
# Valid
#
# Fix the condition.
#
# number = 20
#
# if number > 10 and number < 20:
#     print("Valid")
# else:
#     print("Invalid")

number = 20
if number >= 10 and number <= 20:
    print('valid')
else:
    print('invalid')


# TASK 59:
# The programmer wants the function to RETURN the answer.
#
# Fix it.
#
# def add_numbers(a, b):
#     total = a + b
#     print(total)
#
# result = add_numbers(4, 6)
# print(result)

def add_numbers(a,b):
    total = a + b
    return total
result = add_numbers(4,6)
print(result)


# TASK 60:
# Fix the function so the variable result works outside
# of the function.
#
# def subtract(a, b):
#     answer = a - b
#
# result = subtract(20, 8)
# print(result)

def subtract(a,b):
    answer = a-b
    return answer
result = subtract(20,8)
print(result)


# ============================================================
# FINAL BOSS 1 — THREE NUMBER ANALYZER
# ============================================================

# TASK 61:
# Create a function named:
#
# analyze_three_numbers
#
# Give it THREE parameters:
#
# a
# b
# c
#
# It must:
#
# 1. Determine the highest value.
# 2. Determine the lowest value.
# 3. Determine the middle value.
# 4. Determine whether all three are equal.
# 5. Determine whether exactly two are equal.
#
# Print:
#
# Highest: [value]
# Lowest: [value]
# Middle: [value]
#
# Then print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Test:
# analyze_three_numbers(8, 3, 15)
# analyze_three_numbers(20, 20, 20)
# analyze_three_numbers(5, 5, 9)
# analyze_three_numbers(-5, 0, -12)

def analyze_three_numbers(a, b, c):
    highest = 0
    lowest = 0
    middle = 0
    if a > b and a > c:
        highest = a
    elif b > a and b > c:
        highest = b
    elif c > a and c > b:
        highest = c
    else:
        if a > b and a == c:
            highest = a or c
        elif a > c and a == b:
            highest = a or b
        elif b > a and b == c:
            highest = b or c
        elif a == b == c:
            highest = a or b or c
    if a < b and a < c:
        lowest = a
    elif b < a and b < c:
        lowest = b
    elif c < a and c < b:
        lowest = c
    else:
        if a < b and a == c:
            lowest = a or c
        elif a < c and a == b:
            lowest = a or b
        elif b < a and b == c:
            lowest = b or c
        elif a == b == c:
            lowest = a or b or c
    if a > b and a < c or a < b and a > c:
        middle = a
    elif b > a and b < c or b < a and b > c:
        middle = b
    elif c > a and c < b or c < a and c > b:
        middle = c
    else:
        if a == b == c:
            middle = a or b or c
        else:
            middle = -1000000
    print(f'highest: {highest}')
    print(f'lowest: {lowest}')
    if middle == -1000000:
        print('middle: doesnt exist')
    else:
        print(f'middle: {middle}')
    if a == b == c:
        print('all the same')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('exactly two are the same')
    else:
        print('all different')
analyze_three_numbers(8, 3, 15)
analyze_three_numbers(20, 20, 20)
analyze_three_numbers(5, 5, 9)
analyze_three_numbers(-5, 0, -12)

    
    


# ============================================================
# FINAL BOSS 2 — NUMBER RANKING
# ============================================================

# TASK 62:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# user_num1
# user_num2
# user_num3
#
# Print the numbers from LOWEST to HIGHEST.
#
# Example:
# User enters:
# 30
# 10
# 20
#
# Output:
# 10
# 20
# 30
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Your program must still work if the order of inputs changes.

user_num1 = int(input('give first number pls'))
user_num2 = int(input('give second number pls'))
user_num3 = int(input('give third number pls'))
def sort(a,b,c):
    if a < b and a < c:
        if b < c:
            return a,b,c
        else:
            return a,c,b
    elif b < a and b < c:
        if a < c:
            return b,a,c
        else:
            return b,c,a
    elif c < a and c < b:
        if a < b:
            return c,a,b
        else:
            return c,b,a
print(sort(user_num1,user_num2,user_num3))
            


# ============================================================
# FINAL BOSS 3 — FUNCTION REUSE
# ============================================================

# TASK 63:
# Create these THREE functions:
#
# get_highest(a, b, c)
# get_lowest(a, b, c)
# get_middle(a, b, c)
#
# Each function must RETURN the correct value.
#
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# first
# second
# third
#
# Call all three functions.
#
# Store the returned results in:
#
# highest
# lowest
# middle
#
# Then print:
#
# Highest: [highest]
# Middle: [middle]
# Lowest: [lowest]
#
# Do NOT use min(), max(), or sorting.

first = int(input('give your first number'))
second = int(input('give your second number'))
third = int(input('give your third number'))
def get_highest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
def get_lowest(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
def get_middle(a,b,c):
    if a > b and a < c or a < b and a > c:
        return a
    elif b > a and b < c or b < a and b > c:
        return b
    elif c > a and c < b or c < a and c > b:
        return c
    else:
        if a == b == c:
            return a or b or c
highest = get_highest(first,second,third)
lowest = get_lowest(first,second,third)
middle = get_middle(first,second,third)

print(f'highest = {highest}\nlowest = {lowest}\nmiddle = {middle}')

# ============================================================
# FINAL BOSS 4 — CONDITIONAL DECISION SYSTEM
# ============================================================

# TASK 64:
# Create a function named:
#
# admission_decision
#
# Give it THREE parameters:
#
# grade
# attendance
# interview
#
# Rules:
#
# - If grade is 90 or higher AND attendance is 90 or higher,
#   print "Accepted"
#
# - Otherwise, if grade is 80 or higher AND attendance is 80 or higher
#   AND interview is "pass", print "Accepted"
#
# - Otherwise print "Not accepted"
#
# Test:
#
# admission_decision(95, 95, "fail")
# admission_decision(85, 85, "pass")
# admission_decision(85, 85, "fail")
# admission_decision(75, 100, "pass")
#
# THINK:
# The first person should still be accepted even though
# the interview value is "fail".

def admission_decision(grade, attendance, interview):
    if grade >= 90 and attendance >= 90:
        print('accepted')
    elif grade >= 80 and attendance >= 80 and interview == "pass":
        print('accepted')
    else:
        print('not accepted')
admission_decision(95, 95, "fail")
admission_decision(85, 85, "pass")
admission_decision(85, 85, "fail")
admission_decision(75, 100, "pass")


# ============================================================
# FINAL BOSS 5 — THINK CAREFULLY
# ============================================================

# TASK 65:
# Create:
#
# a = 15
# b = 8
# c = 15
#
# Your program must determine BOTH:
#
# 1. The highest value
# 2. Whether that highest value is unique or tied
#
# Print:
#
# Highest: [value]
#
# Then print ONE of:
#
# Unique highest
# Tied highest
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Your logic should still work if the variable values change.
a=15
b=8
c=15
def high_checker(a,b,c):
    if a > b and a > c:
        return a, "unique highest"
    elif b > a and b > c:
        return b, "unique highest"
    elif c > a and c > b:
        return c, "unique highest"
    else:
        if a > b and a == c:
            return a or c, "tied highest"
        elif a > c and a == b:
            return a or b, "tied highest"
        elif b > a and b == c:
            return b or c, "tied highest"
        else:
            return a or b or c, "tied highest"
highest, epic_string = high_checker(a,b,c)
print(f'highest: {highest}\n{epic_string}')






# ============================================================
# SECTION 12 — LEETCODE-STYLE REAL PROBLEM CHALLENGES
# ============================================================
#
# These problems are intentionally DIFFERENT from the earlier tasks.
# Instead of simply asking you to find the highest number, check a range,
# or assign a grade, each problem gives you a small situation to solve.
#
# RULES:
# - Use the EXACT function name and parameters given.
# - Do NOT use input() unless the problem specifically tells you to.
# - RETURN the answer unless the problem specifically tells you to print.
# - Your function must work for ALL valid test cases.
# - Do NOT hard-code the example answers.
# - Use only concepts covered in class.
# - Test every example after writing your function.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 66 — TEMPERATURE CONVERTER
# ------------------------------------------------------------
#
# Write a function named:
#
# convert_temperature
#
# Parameters:
#
# temperature
# scale
#
# The scale will be either:
#
# "C"
# or
# "F"
#
# If scale is "C", the temperature given is Celsius.
# Convert it to Fahrenheit using:
#
# Fahrenheit = Celsius * 1.8 + 32
#
# If scale is "F", the temperature given is Fahrenheit.
# Convert it to Celsius using:
#
# Celsius = (Fahrenheit - 32) / 1.8
#
# RETURN the converted temperature.
#
# Examples:
#
# convert_temperature(0, "C")      -> 32
# convert_temperature(100, "C")    -> 212
# convert_temperature(32, "F")     -> 0
# convert_temperature(68, "F")     -> 20
#
# CHALLENGE:
# The same function must be able to convert in BOTH directions.

def convert_temperature(temperature, scale):
    if scale == "C":
        fahrenheit = temperature * 1.8 + 32
        return fahrenheit
    elif scale == "F":
        celsius = (temperature - 32) / 1.8
        return celsius
print(convert_temperature(0, "C"))  
print(convert_temperature(100, "C"))   
print(convert_temperature(32, "F"))    
print(convert_temperature(68, "F"))     



# ------------------------------------------------------------
# LEETCODE-STYLE TASK 67 — KELVIN CONVERTER
# ------------------------------------------------------------
#
# Write a function named:
#
# to_kelvin
#
# Parameters:
#
# temperature
# scale
#
# If scale is "C":
#
# Kelvin = Celsius + 273.15
#
# If scale is "F":
#
# First convert Fahrenheit to Celsius:
#
# Celsius = (Fahrenheit - 32) / 1.8
#
# Then convert Celsius to Kelvin.
#
# RETURN the Kelvin temperature.
#
# Examples:
#
# to_kelvin(0, "C")     -> 273.15
# to_kelvin(100, "C")   -> 373.15
# to_kelvin(32, "F")    -> 273.15
# to_kelvin(212, "F")   -> 373.15
#
# THINK:
# One input can require TWO calculations before you return the answer.
def to_kelvin(temperature, scale):
    if scale == "C":
        kelvin = temperature + 273.15
        return kelvin
    elif scale == "F":
        celsius = (temperature - 32) / 1.8
        kelvin = celsius + 273.15
        return kelvin
print(to_kelvin(0, "C"))
print(to_kelvin(100, "C"))
print(to_kelvin(32, "F"))
print(to_kelvin(212, "F"))

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 68 — PARKING GARAGE
# ------------------------------------------------------------
#
# Write a function named:
#
# parking_cost
#
# Parameter:
#
# hours
#
# Parking costs:
#
# First hour: $5
# Each additional hour: $3
#
# If the car is parked for more than 8 hours,
# the maximum daily charge is $25.
#
# RETURN the total parking cost.
#
# Examples:
#
# parking_cost(1)   -> 5
# parking_cost(2)   -> 8
# parking_cost(5)   -> 17
# parking_cost(9)   -> 25
# parking_cost(20)  -> 25
#
# THINK:
# Do not accidentally charge $3 for the first hour.
def parking_cost(hours):
    if hours <= 1:
        cost = 5
        return cost
    elif hours > 1:
        additional = (hours-1) * 3
        cost = additional + 5
        return cost
print(parking_cost(1))
print(parking_cost(2))
print(parking_cost(5))
print(parking_cost(9))
print(parking_cost(20))
    


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 69 — MOVIE TICKET TOTAL
# ------------------------------------------------------------
#
# Write a function named:
#
# movie_total
#
# Parameters:
#
# age
# is_weekend
#
# Ticket prices:
#
# Under 13: $8
# Ages 13–64: $12
# Age 65+: $7
#
# On weekends, add $3 to the ticket price.
#
# RETURN the final ticket price.
#
# Examples:
#
# movie_total(10, False)  -> 8
# movie_total(10, True)   -> 11
# movie_total(30, False)  -> 12
# movie_total(70, True)   -> 10
#
# THINK:
# First determine the base ticket price.
# Then decide whether something must be added.
def movie_total(age, is_weekend):
    price1 = 8
    price2 = 12
    price3 = 7
    additional = 3
    if age < 13:
        if is_weekend:
            final = price1 + additional
            return final
        else:
            return price1
    elif age >= 13 and age < 65:
        if is_weekend:
            final = price2 + additional
            return final
        else:
            return price2
    else:
        if is_weekend:
            final = price3 + additional
            return final
        else:
            return price3
print(movie_total(10, False))
print(movie_total(10, True)) 
print(movie_total(30, False)) 
print(movie_total(70, True))
            



# ------------------------------------------------------------
# LEETCODE-STYLE TASK 70 — ELECTRIC BILL
# ------------------------------------------------------------
#
# Write a function named:
#
# electric_bill
#
# Parameter:
#
# usage
#
# The bill is calculated using these rules:
#
# 0–100 units:
# $0.10 per unit
#
# More than 100 units:
# The first 100 units cost $0.10 each.
# Every unit AFTER 100 costs $0.20 each.
#
# RETURN the total bill.
#
# Examples:
#
# electric_bill(50)   -> 5.0
# electric_bill(100)  -> 10.0
# electric_bill(120)  -> 14.0
# electric_bill(200)  -> 30.0
#
# IMPORTANT:
# For 120 units, only 20 units should be charged at $0.20.

def electric_bill(usage):
    if usage <= 0:
        usage == 0
    if usage <= 100:
        cost = usage * 0.1
        return cost
    else:
        add_units = (usage - 100) * 0.2
        cost = add_units + 10
        return cost
print(electric_bill(50))
print(electric_bill(100))
print(electric_bill(120))
print(electric_bill(200))


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 71 — LEAP YEAR
# ------------------------------------------------------------
#
# Write a function named:
#
# is_leap_year
#
# Parameter:
#
# year
#
# A year is a leap year if:
#
# - it is divisible by 400
#
# OR
#
# - it is divisible by 4 BUT NOT divisible by 100
#
# RETURN True if it is a leap year.
# Otherwise RETURN False.
#
# Examples:
#
# is_leap_year(2024)  -> True
# is_leap_year(2025)  -> False
# is_leap_year(1900)  -> False
# is_leap_year(2000)  -> True
#
# This problem is intentionally tricky.
#
# THINK:
# A year divisible by 100 is NOT automatically a leap year.

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 >= 1:
        return True
    else:
        return False
print(is_leap_year(2024))
print(is_leap_year(2025))
print(is_leap_year(1900))
print(is_leap_year(2000))



# ------------------------------------------------------------
# LEETCODE-STYLE TASK 72 — TRIANGLE VALIDITY
# ------------------------------------------------------------
#
# Write a function named:
#
# valid_triangle
#
# Parameters:
#
# a
# b
# c
#
# Three side lengths can form a triangle only if:
#
# a + b > c
# a + c > b
# b + c > a
#
# ALL THREE conditions must be true.
#
# RETURN True if the sides can form a triangle.
# Otherwise RETURN False.
#
# Examples:
#
# valid_triangle(3, 4, 5)   -> True
# valid_triangle(5, 5, 5)   -> True
# valid_triangle(1, 2, 10)  -> False
# valid_triangle(2, 3, 5)   -> False
#
# Notice that 2 + 3 = 5 is NOT enough.
# It must be GREATER THAN.
def valid_triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False
print(valid_triangle(3, 4, 5))
print(valid_triangle(5, 5, 5))
print(valid_triangle(1, 2, 10))
print(valid_triangle(2, 3, 5))

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 73 — TRIANGLE TYPE
# ------------------------------------------------------------
#
# Write a function named:
#
# triangle_type
#
# Parameters:
#
# a
# b
# c
#
# First, determine whether the three sides form a valid triangle.
#
# If they do NOT, RETURN:
#
# "invalid"
#
# If all three sides are equal, RETURN:
#
# "equilateral"
#
# If exactly two sides are equal, RETURN:
#
# "isosceles"
#
# Otherwise RETURN:
#
# "scalene"
#
# Examples:
#
# triangle_type(3, 3, 3)   -> "equilateral"
# triangle_type(5, 5, 8)   -> "isosceles"
# triangle_type(3, 4, 5)   -> "scalene"
# triangle_type(1, 2, 10)  -> "invalid"
#
# THINK:
# Check whether the triangle is valid BEFORE classifying it.
def triangle_type(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        if a == b == c:
            return "equilateral"
        elif a == b and a != c or a == c and a != b or b == c and b != a:
            return "isosceles"
        else:
            return "scalene"
    else:
        return "invalid"
print(triangle_type(3, 3, 3))
print(triangle_type(5, 5, 8))
print(triangle_type(3, 4, 5))
print(triangle_type(1, 2, 10))

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 74 — ROCK PAPER SCISSORS
# ------------------------------------------------------------
#
# Write a function named:
#
# rps_winner
#
# Parameters:
#
# player1
# player2
#
# Each argument will be:
#
# "rock"
# "paper"
# or
# "scissors"
#
# RETURN:
#
# "tie"
#
# if both players choose the same thing.
#
# RETURN:
#
# "player1"
#
# if player 1 wins.
#
# RETURN:
#
# "player2"
#
# if player 2 wins.
#
# Rules:
#
# rock beats scissors
# scissors beats paper
# paper beats rock
#
# Examples:
#
# rps_winner("rock", "scissors")  -> "player1"
# rps_winner("paper", "rock")     -> "player1"
# rps_winner("rock", "paper")     -> "player2"
# rps_winner("paper", "paper")    -> "tie"
#
# This is a logic problem.
# There are several possible combinations.

def rps_winner(player1, player2):
    if player1 == player2:
        return 'tie'
    else:
        if player1 == 'rock':
            if player2 == 'paper':
                return 'player2'
            elif player2 == 'scissors':
                return 'player1'
        elif player1 == 'paper':
            if player2 == 'rock':
                return 'player1'
            elif player2 == 'scissors':
                return 'player2'
        elif player1 == 'scissors':
            if player2 == 'rock':
                return 'player2'
            elif player2 == 'paper':
                return 'player1'
print(rps_winner("rock", "scissors"))
print(rps_winner("paper", "rock"))
print(rps_winner("rock", "paper"))
print(rps_winner("paper", "paper"))
# ------------------------------------------------------------
# LEETCODE-STYLE TASK 75 — CLOSEST TO 100
# ------------------------------------------------------------
#
# Write a function named:
#
# closest_to_100
#
# Parameters:
#
# a
# b
#
# RETURN whichever number is closer to 100.
#
# If they are equally far away from 100, RETURN:
#
# -1
#
# Examples:
#
# closest_to_100(90, 80)    -> 90
# closest_to_100(105, 120)  -> 105
# closest_to_100(90, 110)   -> -1
#
# RESTRICTION:
# Do NOT use abs().
#
# THINK:
# A number may be above OR below 100.
# You will need to determine each number's distance from 100.
def closest_to_100(a,b):
    if a == 100:
        return a
    elif b == 100:
        return b
    def higher_than_100(num):
        if num > 100:
            return True
        elif num < 100:
            return False
    checka = higher_than_100(a)
    checkb = higher_than_100(b)
    finala = 0
    finalb = 0
    if checka == True:
        finala = a - 100
    else:
        finala = 100 - a
    if checkb == True:
        finalb = b - 100
    else:
        finalb = 100 - b
    if finala < finalb:
        return a
    elif finala > finalb:
        return b
    else:
        return -1


print(closest_to_100(90, 80))
print(closest_to_100(105, 120))
print(closest_to_100(90, 110)) 


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 76 — DELIVERY FEE
# ------------------------------------------------------------
#
# Write a function named:
#
# delivery_fee
#
# Parameters:
#
# order_total
# distance
#
# Rules:
#
# If order_total is $50 or more AND distance is 5 miles or less:
# RETURN 0
#
# Otherwise, if distance is 5 miles or less:
# RETURN 5
#
# Otherwise:
# RETURN 10
#
# Examples:
#
# delivery_fee(60, 3)  -> 0
# delivery_fee(30, 3)  -> 5
# delivery_fee(60, 8)  -> 10
# delivery_fee(30, 8)  -> 10
#
# THINK:
# A large order does NOT always mean free delivery.

def delivery_fee(order_total, distance):
    if order_total >= 50 and distance <= 5:
        return 0
    elif distance <= 5:
        return 5
    else:
        return 10
print(delivery_fee(60, 3))
print(delivery_fee(30, 3))
print(delivery_fee(60, 8))
print(delivery_fee(30, 8))

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 77 — ATM WITHDRAWAL
# ------------------------------------------------------------
#
# Write a function named:
#
# can_withdraw
#
# Parameters:
#
# balance
# amount
#
# A withdrawal is allowed only if:
#
# - amount is greater than 0
# - amount is less than or equal to balance
# - amount is divisible by 20
#
# RETURN True if the withdrawal is allowed.
# Otherwise RETURN False.
#
# Examples:
#
# can_withdraw(500, 100)  -> True
# can_withdraw(500, 125)  -> False
# can_withdraw(50, 100)   -> False
# can_withdraw(500, 0)    -> False
#
# ALL conditions must be true.

def can_withdraw(balance, amount):
    if amount > 0 and amount <= balance and amount % 20 == 0:
        return True
    else:
        return False
print(can_withdraw(500, 100))
print(can_withdraw(500, 125))
print(can_withdraw(50, 100))
print(can_withdraw(500, 0))

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 78 — RESTAURANT TIP
# ------------------------------------------------------------
#
# Write a function named:
#
# tip_amount
#
# Parameters:
#
# bill
# service
#
# service will be:
#
# "poor"
# "good"
# or
# "excellent"
#
# Tip rules:
#
# poor       -> 10%
# good       -> 18%
# excellent  -> 25%
#
# RETURN the tip amount.
#
# Examples:
#
# tip_amount(100, "poor")       -> 10
# tip_amount(100, "good")       -> 18
# tip_amount(100, "excellent")  -> 25
# tip_amount(80, "good")        -> 14.4
#
# THINK:
# RETURN only the TIP, not the final bill.
def tip_amount(bill, service):
    if service == 'poor':
        tip = bill * (1/10)
        return tip
    elif service == 'good':
        tip = bill * (18/100)
        return tip
    elif service == "excellent":
        tip = bill * (1/4)
        return tip
print(tip_amount(100, "poor"))
print(tip_amount(100, "good"))
print(tip_amount(100, "excellent"))
print(tip_amount(80, "good"))



# ------------------------------------------------------------
# LEETCODE-STYLE TASK 79 — PHONE BATTERY WARNING
# ------------------------------------------------------------
#
# Write a function named:
#
# battery_status
#
# Parameters:
#
# battery
# is_charging
#
# RETURN:
#
# "critical"
# if battery is 5 or lower AND it is NOT charging
#
# "low"
# if battery is 20 or lower AND it is NOT charging
#
# "charging"
# if is_charging is True
#
# "normal"
# otherwise
#
# Examples:
#
# battery_status(3, False)   -> "critical"
# battery_status(15, False)  -> "low"
# battery_status(3, True)    -> "charging"
# battery_status(80, False)  -> "normal"
#
# THINK:
# The order of the conditions matters.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 80 — TAXI FARE
# ------------------------------------------------------------
#
# Write a function named:
#
# taxi_fare
#
# Parameters:
#
# miles
# is_night
#
# Fare rules:
#
# Base fare: $4
# Each mile: $2
#
# If is_night is True, add a $5 night fee.
#
# RETURN the total fare.
#
# Examples:
#
# taxi_fare(0, False)  -> 4
# taxi_fare(5, False)  -> 14
# taxi_fare(5, True)   -> 19
#
# Build the final answer from the rules instead of
# hard-coding different totals.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 81 — GAME DAMAGE
# ------------------------------------------------------------
#
# Write a function named:
#
# calculate_damage
#
# Parameters:
#
# attack
# defense
# critical
#
# First calculate:
#
# damage = attack - defense
#
# If damage would be less than 0, damage becomes 0.
#
# If critical is True, DOUBLE the damage.
#
# RETURN the final damage.
#
# Examples:
#
# calculate_damage(20, 5, False)  -> 15
# calculate_damage(20, 5, True)   -> 30
# calculate_damage(5, 20, False)  -> 0
# calculate_damage(5, 20, True)   -> 0
#
# THINK:
# The critical hit should happen AFTER defense is removed.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 82 — STORE COUPON
# ------------------------------------------------------------
#
# Write a function named:
#
# final_price
#
# Parameters:
#
# price
# coupon
#
# coupon will be:
#
# "none"
# "SAVE10"
# "SAVE25"
#
# Rules:
#
# "none"   -> no discount
# "SAVE10" -> 10% off
# "SAVE25" -> 25% off
#
# RETURN the FINAL price after the discount.
#
# Examples:
#
# final_price(100, "none")    -> 100
# final_price(100, "SAVE10")  -> 90
# final_price(100, "SAVE25")  -> 75
# final_price(80, "SAVE25")   -> 60
#
# THINK:
# A 25% discount means the customer pays 75% of the price.


# ============================================================
# GIT CHECK
# ============================================================

# When you are completely finished:
#
# 1. Save your file.
# 2. Run your ENTIRE program.
# 3. Fix all errors.
# 4. Make sure you can explain your code.
#
# Then use:
#
# git status
# git add .
# git commit -m "Complete conditionals and functions challenge"
# git push
