n,k = map(int,input().split())
que=list(input())
j=0
for i in range(k):
    j=1
    while j<n:
        if que[j-1]=="B" and que[j]=="G":
            que[j-1],que[j]=que[j],que[j-1]
            j+=1
        j+=1
str1 = ""  
for ele in que:  
    str1 += ele   
print (str1) 