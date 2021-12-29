mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
a=mainStr.split()
subStr = "over"
i=0
b=[]
while i<len(a):
    if a[i]==subStr:
        pass
    else:
        b.append(a[i])
    i+=1
print(b)
