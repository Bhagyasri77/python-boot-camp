#3 jars fill with chocolate with equally dividing


n=int(input())
arr=[10,20,30]
total_cho_a=0
for i in arr:
    total_cho_a+=i//3
    if i%3!=0:
        total_cho_a+=1
print(total_cho_a)        

