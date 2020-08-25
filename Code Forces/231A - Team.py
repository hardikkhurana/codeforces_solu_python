no_cases=int(input())
solved=0
for i in range(no_cases):
    case=str(input())
    if case.count("1")>=2:
        solved+=1
print(solved)