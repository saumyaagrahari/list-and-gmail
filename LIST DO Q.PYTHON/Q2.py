# list=[1,1,2,3,4,4,5,1]
# i=0
# a=[]
# while i<len(list):
#     j=0
#     b=[]
#     count=0
#     while j<len(list):
#         if list[0]==list[i]:
#             count+=1
#             a.append(list)
#             print(count+[i])
#         else:
#             pass


# n=int(input("Enter a number:"))
# tot=0
# while(n>0):
#     dig=n%10
#     tot=tot+dig
#     n=n//10
# print("The total sum of digits is:",tot)


# list=[[3,5,7,],[4,0,8],[1,45,9]]
# i=0
# while i<len(list):
#     j=0
#     max=0
#     while j<len(list[i]):
#         if list[i][j]>max:
#             max=list[i][j]
#         j+=1
#     i+=1
#     print(max)

# user=int(input("enter the number:"))
# for i in range (user):
#     if user[i]+user[i[1]]:
#         print(user)


# num=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# count=1
# max=num[i]
# while i<len(num):
#     if len(max)<len(num[i]):
#         max=num[i]
#         count+=1
#     i+=1
# print(max,count)


# num=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# count=1
# min=num[i]
# while i>len(num):
#     if len(min)>len(num[i]):
#         min=num[i]
#         count+=1
#     i+=1
# print(min,count)


# list=[[3,5,7,],[4,0,8],[1,45,9]]
# i=0
# while i<len(list):
#     j=0
#     min=3000
#     while j<len(list[i]):
#         if list[i][j]<min:
#             min=list[i][j] 
#         j+=1
#     # print(min)
#     i+=1
#     print(min)



# num=int(input("enter the number:"))
# i=1
# while i<=num:
#     j=1
#     while j<=num-i:
#         print("",end=" ")
#         j+=1
#     a=1
#     while a<=i:
#         print(j,end="")
#         a+=1
#     print() 
#     i+=1


# for i in range(-4,5,1):
#     print(i,end=" ")
#     if i==-1:
#         break


# for i in range (0,6):
#     print(i)


# i=0
# a=[]
# while i<10:
#     num=int(input("enter the number:"))
#     a.append(num)
#     i+=1
# print(a)
# b=int(input("enter the number:"))


# a=["zero","one","two","three","four","five","six","seven","eight","nine"]
# user=input("enter the number:")
# i=0
# while i<len(user):
#     k=int(user[i])
#     print(a[k])
#     i+=1


# list=[3,1,2,1,4,1,3,1,5,1,2]
# b=[]
# c=[]
# i=0
# while i<len(list):
#     if list[i]==1:
#         b.append(list[i])
#     else:
#         c.append(list[i])
#     i+=1
# print(c)


# a="12/3/2021"
# sum=0
# for i in range(len(a)):
#     if type(a[i])==int:
#         sum+=int(a[i])
#     else:
#         continue
#     print(sum)


# a="12/03/2021"
# sum=0
# for i in range(len(a)):
#     if type(a[i])==str:
#         if "/" in a:
#             continue
#         else:
#             sum+=int(a[i])
#             print(sum)
    

# list=[1,5,2,5,3,5,4,6,5,7,5,8,5,9,8]
# a=[]
# c=[]
# i=0
# count=0
# while i<len(list):
#     j=0
#     while j<len(list):
#         if list[i]==list[j]:
#             count+=1
#             a.append(list[i])
#         else:
#             c.append(list[i])
#         j+=1
#     i+=1
# # print(c)
# print(a)


# a="52 saumya 3"
# b=[]
# i=0
# while i<len(a):
#     a=int(a)
#     if a(i)==str:
#         pass
#     else:
#         b.append(a)
# print(b)
# i+=1

# a="52saumya3"
# b=[]
# i=0
# while i<len(a):
#     i[3:9]
#     b.append(a)
#     i+=1
# print(a)

# a="52saumya3"
# b=[]
# i=0
# while i<len(a):
#     if a.isalnum():
#         b.append(a)
#         i+=1
# print(b)

# a="52saumya3"
# b=[]
# c=[]
# i=0
# while i<len(a):
#     if a.split():
#         b.append(a)
#     else:
#         c.append(a)
#     # print(c)
#     i+=1
# print(b)

# a="52saumya3"
# b=[]
# i=0
# while i<len(a):
#     x=a[2:8]
#     b.append(x)
#     i+=1
# print(b)

# txt = "welcome to the jungle"
# x = txt.split()
# print(x)

# a="@52#saumya@"
# a=[]
# c=[]
# d=[]

# txt = "Company 12"
# x = txt.isalnum()
# print(x)

# txt = "CompanyX"
# x = txt.isalpha()
# print(x)

# num=input("enter the number:")
# print(list(num))
# i=0
# b=[]
# while i<len(num):
#     if num[i]!="/":
#         b.append(num[i])
#     i+=1
# # print(b)
# i=0
# sum=0
# while i<len(b):
#     c=int(b[i])
#     sum+=c
#     i+=1
# print(sum)

# user=(input("enter the number"))
# sum=0
# for i in user:
#     if i !="/":
#         sum+=int(i)
# print(sum)