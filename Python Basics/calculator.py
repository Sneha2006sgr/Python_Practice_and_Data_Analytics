# Calculator using class
class Calculator:
    def add(self,a,b):
        return(f"The addition of numbers {a} and {b} is {a+b}")

    def sub(self,a,b):
        return(f"The Subtraction of numbers {a} and {b} is {a-b}")

    def mul(self,a,b):
        return(f"The product of numbers {a} and {b} is {a*b}")

    def div(self,a,b):
        try:
            div=a/b
            print(f"The Quotient on dividing numbers {a} and {b} is {div}")
        except Exception as err:
            print(f"An error named {err} occured")    
        

    def rem(self,a,b):
        return(f"The remainder on dividing numbers {a} and {b} is {a%b}") 

print("Hellooo Welcome to the Calculation Numbers")
print("----------------------------------------------------------")
print("1. Enter 1 for Adding two numbers")
print("2. Enter 2 for Subtracting two numbers")
print("3. Enter 3 for Multiplying two numbers")
print("4. Enter 4 to know quotient of two numbers")
print("5. Enter 5 to know remainders of two numbers")

check=int (input("Kindly  mention your choice:- "))

obj=Calculator()

if check==1:
    a=int(input("Tell me your First number:- "))
    b=int(input("Tell me your Second number:- "))
    print(obj.add(a,b))
elif check==2:
    a=int(input("Tell me your First number:- "))
    b=int(input("Tell me your Second number:- "))
    print(obj.sub(a,b))
elif check==3:
    a=int(input("Tell me your First number:- "))
    b=int(input("Tell me your Second number:- "))
    print(obj.mul(a,b))
elif check==4:
    a=int(input("Tell me your First number:- "))
    b=int(input("Tell me your Second number:- "))
    obj.div(a,b)
elif check==5:
    a=int(input("Tell me your First number:- "))
    b=int(input("Tell me your Second number:- "))
    print(obj.rem(a,b))
else:
    print("Kindly mention the correct input:")



