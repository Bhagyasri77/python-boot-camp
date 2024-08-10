#sum of digits   

#123%10=3     #12%10=2       #1%10=1
#3            #3+2=5         #5+1=6
#123/10=12    #12/10=1       #1/10=0


n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)    
