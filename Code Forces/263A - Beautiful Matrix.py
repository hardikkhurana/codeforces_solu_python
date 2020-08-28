row=1
moves=0
for i in range(5):
    line=input()
    line=line.split()
    for j in line:
        if j=="1":
            moves=(moves+abs((3-((line.index("1"))+1))))+abs(3-row)
            break
    row+=1
print (moves)
