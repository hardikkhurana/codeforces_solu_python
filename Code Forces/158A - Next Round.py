n,k = map(str,input().split())
line2=input()
list2=line2.split(" ")
people_advanced=0
for i in list2:
    if i>=k and i<=n:
        people_advanced+=1
print(people_advanced)