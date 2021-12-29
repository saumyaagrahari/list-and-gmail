# Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki file mein nayi line mein daalo.
#  Aapki list yeh rahi:

# banks_list = open("test_file.txt","w")
# banklst=["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda"]
# for i in banklst:
#     banks_list.write(i)
# banks_list.close()

banks_list=open("test_file.txt","r")
read=banks_list.read()
print(read)
banks_list.close()

