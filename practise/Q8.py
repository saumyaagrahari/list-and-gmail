# counter=1
# num=int(input("enter the number:"))
# count=2*num-2
# for row in range((num*2)+1):
#     if not(row%2==0):
#         for col in range(row):
#             print(" ",end=" ")
#         count=count-2
#         for col in range(row):
#             if col%2==0:
#                 print("1",end="")
#             else:
#                 print("0",end="")
#         print()


# counter=1
# num=int(input("enter the number:"))
# count=num
# for row in range (num):
#     for col in range(0,count):
#         print(" ",end="")
#     count=count-1
#     for col in range(row+1):
#         print(counter,end="")
#         counter+=1
#     print()
#     counter=1

# c=1
# n=int(input("enter the number:"))
# o=2*n-2
# while c<len((n*2)+1):
#     if not(c%2==0):
#         print(end=" ")
#     p=p-2
#     while p<len(n):
#         if p%2==0:
#             print("1",end="")
#         else:
#             print("0",end="")
#     print() 

# a=[1,2,3,4,5,6,7]
# b=[8,9,1,2,3,4,5]
# a.extend (b)
# print(a)

# a="12hours"
# print(str(12+12)+"hours")

# a="12hours"
# b=a[:2]
# b=int(b)
# a=b*a
# print(a+b)

# string=input("enter the string:")
# if "ly" in string:
#     new=string.replace("ly","ing")
#     print(new)
# elif "ing" in string:
#     new_1=string.replace("ing","ly")
#     print(new_1)
# else:
#     new_3=string+"ing"+"ly"
#     print(new_3)

# num=int(input("enter the number:"))
# if num>=0:
#     print(-num)
# else:
#     print(-(num))


# i=1
# while i<10:
#     if i%2==0:
#         print("even",i)
#     else:
#         print("odd",i)
#     i=i+1

# num=int(input("enter the number:"))
# a=num%10
# b=num//10%10
# c=num//100%10
# d=num//10000%10
# reverse=a*10000+b*100+c*10+d*1
# if reverse<100000:
#     print(reverse)
# # if a==3:
#     print("dgdfhf",num)
# else:
#     print("dddddd")

# i=1
# while i<100:
#     if i%3==0:
#         print(i,"nav")
#     if i%7==0:
#         print(i,"gurukul")
#     if i%3==0 and %7==0:
#         print(i,"navgurukul")
#     else:
#         print(i)
#     i=i+1