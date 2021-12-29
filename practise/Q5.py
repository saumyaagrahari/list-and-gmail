# a="45"
# b="4+8j"
# c="3.8"
# a=int(a)
# b=complex(b)
# c=float(c)
# print(a+b+c)


# a=4
# b=5
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# x = 6
# y = 2
# print(x ** y)
# print(x // y)

#include<stdio.h>
#include<conio.h>
# int main()
# int days;
# float fine;

# printf("Enter the number of days: ");
# scanf("%d", &days);

# if (days > 0 && days <= 5)
#     fine = 0.50 * days;

# if (days >= 6 && days <= 10)
#     fine = 1 * days;

# if (days > 10):
#     fine = 5 * days;

#     if (days > 30):
#         printf("Your membership would be canceled.\n")
        

#     printf("You have to pay 

# i=0
# sum=0
# while i<=10:
#     num=int(input("enter the number:"))
#     sum=sum+num
#     i=i+1
# print(sum)

# i=0
# while i<=10:
#     if i==5:
#         break
#     i=i+1
#     print(i)
  
# i=0
# while i<=20:
#     if i==6:
#         continue
#     print(i)
#     i=i=1  

# i=0
# sum=0
# while i<=421:
#     sum=sum+i
#     i=i+1
# print(sum)

# i=1
# sum=0
# n=int(input("enter the number:"))
# while i<=n:
#     num=int(input("enter the number:"))
#     sum=sum+num
#     i=i+1
# print(sum)

# i=1
# while i<=5:
#     num=int(input("enter the number:"))
#     if num==9:
#         print("exelent")
#         break
#     else:
#         print("incorrect number")
#     i=i+1
# else:
#     print("game over")

# c=0
# d=1
# while c<3:
#     c=c+1
#     d=d*1
#     print("loop ke andar:",c,d)
# else:
#     print("loop ke bahar:",c,d)

# i=0
# num=int(input("enter the number:"))
# while i<num:
#     if num%1==0 and num%num==0:
#         print(num,"is a prime number:")
#         break
#     i=i+1
# else:
#     print(num,"is not prime number")

# i=1
# while i<7:
#     if i==3 or i==5:
#         i=i+1
#         continue
#     print(i)
#     i=i+1

# n=6
# s=0
# i=1
# while i<=n:
#     s=s+i
#     i=i+1
# print(s)

# i=0
# while i<5:
#     j=0
#     while j<5:
#         if i>3:
#             break
#         else:
#             print("*")
#             j=j+1
#         print()
#     i=i+1

# num=int(input("enter the number:"))
# count=1
# sum=0
# while count<num:
#     if num%count==0:
#         sum=sum+count
#     count=count+1
# if sum==num:
#     print(count,"perfect number")
# else:
#     print(count,"not perfect number")

# num=int(input("enter the number"))
# n=num
# rem=0
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
#     if n%sum==0:
#         print(n,"harshad no")
#     else:
#         print(n,"not harshad no")

# num=int(input("enter the numbee:"))
# s=0
# temp=num
# while temp>0:
#     r=temp%10
#     s=s+r**3
#     temp=temp//10
# if s==num:
#     print("armstrong number")
# else:
#     print("not armstrong number")

# print(153//10)

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

# a="22 hourse"
# print(str(22+44)+"hourse")

# num=int(input("enter the number:"))
# a=num%100
# if num%10==0:
#     print("the last digit is zero")
# else:
#     print("the last digit is",a)

# i=int(input("enter the number:"))
# a=0
# x=i
# while i>0:
#     a=(a*10)+i%10
#     i=i//10
# if x==a:
#     print("palindrom number",a)
# else:
#     print("not palindrom number",a)

# num=int(input("enter the number:"))
# count=0
# i=1
# while(i<num):
#     if (num%1==0):
#         count=count+1
#     i=i+1
# if count==2:
#     print("prime number",num)
# else:
#     print("not prime number",num)

# num=int(input("enter the number:"))
# fac=1
# while num>0:
#     fac=fac*num
#     num=num-1
#     print("factorial=",fac)


# i=5
# while i>0:
#     j=5
#     while j>0:
#         print(i,end="")
#         j=j-1
#     i=i-1
#     print()

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# c=[]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print(b,"\n",c)


# a=[5,6,7,8,9,[1,2,3,4,],[5,8,9,]]
# b=[]
# i=0
# while i<len(a):
#     if type(a[i])==list:
#         j = 0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)
