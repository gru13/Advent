# file = open(r"2022\3\input_sample.txt", "r")
file = open(r"2022\3\input.txt", "r")
j = [1]+[chr(i) for i in range(97,97+26)]+[chr(i) for i in range(65, 65+26)]
count = 0
while True:
    visted = set()
    a = file.readline()
    if not(a):
        break
    b = file.readline()
    if not(a):
        break
    c = file.readline()
    if not(a):
        break
    for p in a:
        if p in b and p in c and p !="\n" and p not in visted:
            count += j.index(p)
            visted.add(p)
            print(p)
print(count)
