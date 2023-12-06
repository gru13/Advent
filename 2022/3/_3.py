# file = open(r"2022\3\input_sample.txt", "r")
file = open(r"2022\3\input.txt", "r")
j = [1]+[chr(i) for i in range(97,97+26)]+[chr(i) for i in range(65, 65+26)]

count = 0
for i in file:
    a,b = i[:len(i)//2], i[(len(i)//2):]
    visted = set()
    for k in a:
        if k in b and k not in visted:
            count += j.index(k)

            visted.add(k)

print(count)