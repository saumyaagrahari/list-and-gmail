
student_marks = [23, 45, 89, 90, 56, 80] 
length = len(student_marks)
index = 0
total_marks = 0
while index < len(student_marks):
    total_marks = student_marks[index] + total_marks
    index = index + 1
# print (total_marks)
print ("Total Marks:" + str(total_marks))


# a=[45,45,67,89,4,3,]
# b=len(a)
# i=0
# total=0
# while i<len(a):
#     total=a[i]+total
#     i=i+1
# print("total:"+str(total))