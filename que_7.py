# you are given with a , separated 1 to 10 print only  even numbers
'''for i in range(1,11):
    if i%2==0:
        print(i,end=",")
        '''


#7.2 how many even number are in a given list
'''n=list(map(int,input().split(" ")))
count=0
for i in range(1,len(n)):
    if i%2==0:
        count+=1
print(count)
'''
    



# 7.3 you are given with a space separated integer list find num of evn elements and odd elements in a given list
'''my_list=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(my_list)):
    if my_list[i]%2==0:
        even+=1
    else:
        odd+=1
print(even,odd)
'''



