# Data Structures

# a=[12,34,56,8,90,23]
# print(a)
# # indexing through index of list
# for i in range(len(a)):
#     print(a[i])
# # indexing through elements in list
# for i in a:
#     print(i)

# sample=[3,2,6,7.6,1,45,'Sneha','Mumbai','A','a','/','*','/']
# sample2=[1,3,5,2,7,8]
# # print(sample)
# sample.append(5)
# print(sample)
# print(sample.count('/'))
# sample.pop(3)
# print(sample)
# sample.append('rahul')
# print(sample)
# sample2.sort()
# print(sample2)
# sample.remove('*')
# print(sample)

# help(list)

# print(dir(list))
# list=[1,2,3,4,5,'sneha',True,20.5]
# print(list)
# list=[-1,-3,-90,-43,12,443,2,2]
# for i in list:
#     if i>=0:
#         print(f"The positive numbers in the list are:{i}")
# for i in list:
#     if i<0:print(f"The negative numbers in the list are:{i}")

# list=[1,2,3,4,5,6,7,8,9]
# sum=0
# for i in list:
#     sum+=i
# print(sum/len(list))

# list=[23,12,8,56,34,9,12,54]
# greatest=0
# for i in list:
#     if greatest<i:
#         greatest=i
# print(greatest)

# l=[12,134,4352,214,53,1343,2513]
# greatest=l[0]
# for i in range(len(l)):
#     if greatest<l[i]:
#         greatest=l[i]
#         index=i
# print(f"The greatest number in list is {greatest} and is found on index number {index}")

# l=[1,2,223,4,24,5143,54,5674]
# large=l[0]
# slarge=l[0]
# for i in l:
#     if large<i:
#         slarge=large
#         large=i
#     elif slarge<i:
#         slarge=i
# print(f"The second largest number is {slarge}")

# l=[1,2,3,4,5,6,7]
# large=l[0]
# sl=l[0]
# for i in range(len(l)):
#     if large<l[i]:
#         sl=large
#         large=l[i]
#     elif sl<l[i]:
#         sl=l[i]
# print(sl)

# l=[23,34,12,24,4]
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         print("List is not sorted")
#         break
#     else:
#         print("List is sorted")
#         continue

# TUPLES
# help(tuple)   
# a=(1,2,3,4,5,5,56)
# print(type(a))

# index=a.index(4)
# print(index)

# count=a.count(3)
# print(count)

# unpacking of tuple
# a,b,c,d=(1,2,3,4)
# print(type(a))

# a=(9,)
# print (type(a))

# b=(9)
# print(type(b))

# s={1,2,3,4,5}

# print(hash(1))
# s.add(8)
# print(s)
# s.remove(1)
# print(s)
# s.discard(3)
# print(s)
# s.pop()
# print(s)

# a={1,2,3,4}
# b={4,5,6,7,8}

# print(a.union(b))
# print(a|b)
# print(a.intersection(b))
# print(a&b)
# print(a.difference(b))
# print(a-b)
# print(a.symmetric_difference(b))
# print(a^b)
# Set Also suppport compound operations
# dict={}
# print (type(dict))

# Dictionaries
d={1:"Sneha",2:"Sachin",3:"Mudit",4:23000}
print (type(d))
# Key should be unique, can't be changed or updated once created
# Values can be duplicated, can be changed
# key=index (both are of multiple datatypes)
print(d[1])
d[1]=1000 #updating
print(d)
d.update({'sneha':"hello"})
d[30]=4000 #creating
# del d[40]
print(d)
d={1:"Sneha",2:"Sachin",3:"Mudit",4:23000}
# for i in d:
#     print(i)
#     print(d[i])

# for i in d.values():
#     print(i)
# d.clear()
# c=d.copy() #shallow copy changes done only in copied dict
# print(c)
# c[23]=3400
# print(d)
# a=d #deep copy changes are done in both
# a[5]=2000 
# print(d)
# d2=d.get(d[1])
# print(d.items())

# merge dictionary to other
# d1={10:100,20:200,30:300}
# d2={40:400,50:500,60:600}
# d1['d2']=d2
# print(d1)
# for i in d2:
#     d1[i]=d2[i]
# print(d1)

# d1={10:100,20:200,30:300}
# sum=0
# for i in d1:
#     sum=sum+d1[i]
# print(sum)

# list=[1,1,2,3,231,12,1,2,2,2,2,3,4]
# count=0
# for i in list:
#     count+=1
# print (count)
# # to know count of all elements available
# # d={1:3,2:5} <= This is logic
# d={}
# for i in list:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
# To sum if same keys exist or else create the key
# d1={10:100,20:200,30:300,40:500}
# d2={40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i]+=d2[i]
#     else:
#         d1[i]=d2[i]
# print(d1)
