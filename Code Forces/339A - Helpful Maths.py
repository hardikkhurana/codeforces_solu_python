seq=input()
seq=seq.split("+")
seq.sort()
str=""
for i in seq:
    str=str+i+"+"
str=str[:-1]
print(str)