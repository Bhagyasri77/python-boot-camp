#replace the element in an array with avarage of max and min element
my_list=list(map(int,input().split(" ")))
mini=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<mini):
          mini=my_list[i]
print(mini)
maxi=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
         maxi=my_list[i]
print(maxi)                
s=maxi+mini
avg=s/2
print(avg)    




                            