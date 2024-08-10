#find the duplicates in an array
my_list=list(map(int,input().split(" ")))
a=[]
for i in my_list:
    if(i not in a):
        a.append(i)
print(a)     







