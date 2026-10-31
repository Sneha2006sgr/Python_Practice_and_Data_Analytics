# Decorator modifies a function without modifying it's code
# Example: Imagine a cake decorator is icing on it which doesn't chang ethe taste only it appears nice

# def decorate (func): # func here is argument function here is hello
#     def wrapper(a,b):
#         # print("I will print myself before the function")
#         print("The addition of two numbers are")
#         func()
#         # print("I will print after the function")
#         print("I hope you got the correct answer")
#     return wrapper

# @decorate
# # def Hello():
# #     print("Hello I am Sneha Gond")

# def add(a,b):
#     print(f"Your total is {a+b}")

# # Hello()
# add()

# -----------------ARGS & KARGS-------- Used in decorators
# Special is * and ** you can use any name instead args and kargs
#  *args==> stores valus in tuples

# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum + i
#     print(sum)

# add(12,1,3,4,56,4623,345,5221,4)

# def information(**kwargs):
#     print("your information is \n\n")
#     for i in kwargs:
#         print(f"{i}:{kwargs[i]}")

# information(name='Sneha',age=21,designation='Scientist')

# ---------------------Comprehension------------------------

# l=[i for i in range(1,20) if i%2==0]
# print(l)

# d={x:x**2 for x in range(1,10)}
# print(d)

# s={s for s in range(1,10)}
# print(s)

# -------------------LAMBDA FUNCTIONS-------------------
# Anonymous inline function defined using lambda keyword
# Used for short simple functions that are used only once or temporarily
# You can have multiple arguments but only one expression

# def add(a,d):
#     print("The sum is ",(a+d))
# add(1,2)

# add=lambda a,b:a+b
# print(add(1,3))

# num=lambda a:"even" if a%2==0 else "odd"
# print(num(23))

# ---------------MAP AND FILTER----------------
# Map is used for applying a function  to multiple items
# Takes a list or sequence
# applies same function to every item in that list
# Gives you back a new list/ map object which colud be converted into  a list

# a=[1,2,3,4,5]
# result=map(lambda x:x*2,a)
# def double(x):
#     return x*2

# res=map(double,a)
# print (result)
# print (list(result))
# print (res)
# print(list(res))

# Filter is used to filter out the stuff
# Takes a listCheck each item using a functionKeep sthe titem who passed it

# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# a=[1,2,3,4,5,2,342,343,5,43,24]

# res=filter(even,a)
# res=filter(lambda x: True if x%2==0 else False,a)
# print(list(res))

# ----------------MODULES CREATION---------
# 
# from maths import addition

# print(addition(12,12))

# ------------------PACKAGES--------
# Package have multiple modules
# from packaaageees.sample import maths
# from packaaageees.sample import hello
