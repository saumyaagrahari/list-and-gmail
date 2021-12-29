# name=open("my_file","w")
# name.write("saumya ")
# name.close()

# name=open("my_file","a")
# name.write("anu")
# name.close()

# name=open("my_file","r")
# print(name.read())
# name.close()


user_number=int(input("enter the number:"))
i=1
us=[]
while i<=user_number:
    input=int(input("enter the number:"))
    us.append(input)
    i+=1
# print(user_input)
# user_input=[1,2,3]
j=0
while j<len(us):
    k=0
    while k<len(us):
        p=0
        while p<len(us):
            if j!=k or j!=p or k!=p:
                print(us[j],us[k],us[p])
            p+=1
        k+=1
    j+=1
