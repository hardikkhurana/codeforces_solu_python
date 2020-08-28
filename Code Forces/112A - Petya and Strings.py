a=input()
b=input()
a=a.upper()
b=b.upper()
if ord(a)>ord(b):
    print("1")
elif ord(b)>ord(a):
    print("-1")
else:
    print("0")