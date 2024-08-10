#find the missing num in an array
'''arr=[1,2,3,4,5,7,8,9,10]
sum=0
for i in range(0,len(arr)):
    sum=sum+arr[i]
a=55-sum
print(a)   
'''
my_list=list(map(int,input().split(" ")))
num=int(input())
sum=0
miss=0
for i in range(0,len(my_list),1):
    sum+=my_list[i]
miss=num-sum
print(miss)





