
# def hello():
#     print("This is a function")
# hello()


# def sum(a,b):
#     # print(f"The sum of thenumbers is:{a+b}")
#     return (a+b)

# print(sum(1,2))
# sum(-1,-4)
# sum(12,8)

# def person(name,age):
#     print(f"Hello {name}, you're age is {age}")
# person(age=20,name='sneha')

# def add(a=23,b=4):
#     print(f"The sum of given number is:{a+b}")
# add()
# add(12,2)

# a=(input("Enter a string:- "))

# def reverse(a):
#     rev=""
#     for i in range(len(a)-1,-1,-1):
#         rev+=a[i]
#     print(rev)

# def palindrome(a):
#     rev=""
#     for i in range(len(a)-1,-1,-1):
#         rev+=a[i]
#     if a==rev:
#         print("The string is palindrome")
#     else:
#         print("The string you entered is not palindrome")
# reverse(a)
# palindrome(a)

# def add(a,b):
#         return(f"The addition of numbers {a} and {b} is {a+b}")

# def sub(a,b):
#         return(f"The Subtraction of numbers {a} and {b} is {a-b}")
# def mul(a,b):
#     return(f"The product of numbers {a} and {b} is {a*b}")
# def div(a,b):
#     try:
#         div=a/b
#         print(f"The Quotient on dividing numbers {a} and {b} is {div}")
#     except Exception as err:
#         print(f"An error named {err} occured")    
# def rem(a,b):
#         return(f"The remainder on dividing numbers {a} and {b} is {a%b}") 

a=lambda a,x,y:(a+x-y)

print(a(5,2,3))

even=lambda x:"even" if x%2==0 else "odd" 
                      
print(even(2))