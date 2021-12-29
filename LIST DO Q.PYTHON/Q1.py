# Iterate over both the values in a list and their indices


# grocery_list = ['flour','cheese','carrots']
# i=0
# while i<len(grocery_list):
#     a=grocery_list[i]
#     print(i,":",a)
#     i=i+1


# Convert Character Matrix to single String;

# list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# i=0
# b=[]
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         b.append(list[i][j])
#         j+=1
#     i+=1
# b="".join(b)
# print(b)


# for r in list:
#     for t in r:
#         print(t,end="")


# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# list=[]
# i=0
# count=0
# while i<len(input_list):
#     if input_list[i] in list:
#         pass
#     else:
#         list.append(input_list[i])
#         count+=1
#     i=i+1
# print(count,"=",list)


# number=[56,7,100,6,45,89,12,60,96]
# i=0
# max=0
# while i<len(number):
#     if number[i]>max:
#         max=number[i]
#     i=i+1
# print("first maximum numbe",max)


# second_max=0
# i=0
# while i<len(number):
#     if number[i]>second_max:
#         if number[i]!=max:
#             second_max=number[i]
#     i+=1
# print("second maximum number",second_max)


# third_max=0
# i=0
# while i<len(number):
#     if number[i]>third_max and second_max:
#         if number[i]!=max and number[i]!=second_max:
#             third_max=number[i]
#     i+=1
# print("third maximum number",third_max)


# num=input("enter the a number:")
# for i in num:
#     sum=int(i)
#     print(sum*sum,end=" ")


# i=0
# num=""
# while i <len(num):
#     sum+=str(int(num[i])*int(num[i]))
#     i+=1
# print(num)


# You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12 # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304 # Should return '70000 + 300 + 4'


# size=int(input("enter the size:"))
# a=[]
# for i in range(size):
#     num=int(input("enter the number:"))
#     a.append(num)
#     print(a)
# m=len(a)
# sum=0
# rmndr=0
# n=0
# while n<size:
#     if a[n]>0:
#         rmndr=a[n]%10
#         a[n]=a[n]//10
#         sum=a[n]*10
#         a[n]=a[n]//10
#         n+=1
#     print (sum,"+",rmndr)


# num=int(input("enter the number:"))
# i=1
# while i<=num:
#     count=1
#     while count<=10:
#         a=i*count
#         print(i,"*",count,"=",a)
#         count+=1
#     print()
#     i+=1



