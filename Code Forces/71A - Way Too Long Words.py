num_of_lines=int(input())
for i in range(num_of_lines):
    word=input()
    if len(word)<=10:
        print(word)
    else:
        print((word[0]+str(len(word)-2)+word[-1]))