'''my_list=[1,2,3,4]
print(my_list)
print(*my_list)
my_list.append(9999)
print(my_list)
my_list.insert(2,99)
print(my_list)
my_list_2=[5,6,7,8]
new_list=my_list+my_list_2
print(new_list)
new_list=my_list.copy()
new_list.pop()
print(*new_list)
cnt=my_list.count(2)
print(cnt)
#aggrigate functions
'''
'''my_list=[1,-2,-13,41,28,4,9999]
#pop
my_list.pop()
print(my_list)
my_list.pop(2)
print(my_list)
'''
#my_list=list(map(int,input().split(",")))
#print(mylist)
'''my_list=[5,7,9,1,3,4]
my_list.sort()
print(my_list)
'''
'''my_list=list(map(int,input().split(",")))
#print(my_list)
#if we use more then 2 inputs then use map
#print(*my_list)
#my_list.append(3411)
#print(my_list)
#my_list.pop()
#print(my_list)
''''

my_list=list(map(int,input().split(",")))
user=int(input())
if user==1:
    print(my_list.append())
elif user==2:
    print(my_list.pop())
elif user==3:
    print(my_list.sort()) 
else:
    print("hellow"+str(len(my_list)))           




