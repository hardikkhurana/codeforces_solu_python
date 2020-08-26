sum=0
n=int(input())
for i in range(n):
    temp=input()
    if temp[1]=="+":
        sum+=1
    else:
        sum-=1
print(sum)