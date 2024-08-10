#find the reverse of a num 123
#12 23 36 44 45 57

n=int(input())
rev=" "
while n>0:
    r=n%10
    rev=rev+str(r) 
    n=n//10
print(int(rev)) 