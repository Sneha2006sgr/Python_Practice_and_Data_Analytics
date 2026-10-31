# n=int(input("Enter a number:"))
# for i in range (1,11,1):
#     print (n,"*",i,"=",n*i)
# add=0
# for i in range(n+1):
  
#     temp=0+i
#     add+=temp
# print(add)
# mul=1
# for i in range(1,n+1):
#     mul=mul*i
#     print(mul)
# even=0
# odd=0
# for i in range(n+1):
#     if i%2==0:
       
#         even+=i
        
#     else:
        
#         odd+=i
        
# print(f"Sum of Even numbers:{even}")
# print(f"sum of odd numbers:{odd}")
# Factorization

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)    

# add=0
# for i in range(1,n):
#     if n%i==0:
#         temp=i
#         add+=temp
# if add==n:
#     print("The number is perfect")
# else:
#     print("The number is not perfect")

# count=0
# for i in range(1,n+1):
#     if n%i==0:
# #         count+=1
# # if count==2:
# #     print("number is prime")
# # else: 
# #     print("Number is not prime")
# # str="SNEHA"
# # b=""
# # print(str[::-1])
# # for i in range(len(str)-1,-1,-1):
# #     b=b+str[i]
# # print(b)

# str=input("Enter a word you think is palidrome:")
# rev=""
# for i in range(len(str)-1,-1,-1):
#     rev+=str[i]
# if str==rev:
#     print ("The word you entered is palindrome")
# else:
#     print("Better luck next time")

# a=input("Type whatever you want to:")
# char=0
# digit=0
# spchar=0
# for i in a:
#     if i.isalpha():
#         char+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         spchar+=1
# print(f"Numbers of characters are as follows:")
# print(f"Characters:{char}")
# print(f"Digits:{digit}")
# print(f"Special Characters:{spchar}")

# a=int(input("Enter  anumber:"))
# while a>0:
#     temp= a%10
#     print(temp)
#     a=a//10
    
# a=int(input("Enter a number:"))
# # rev=0
# # while a>0:
# #     temp=a%10
# #     rev=rev*10+temp
# #     a=a//10
# # print(rev)

# rev=0
# b=a
# while b>0:  
#     temp=b%10
#     rev=rev*10+temp
#     b=b//10
# print(rev)
# if (rev==a):
#     print("The number is palindromic")
# else:  
#    print("The number is not palindromic")
