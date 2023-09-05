file = open(r"2022\1\input.txt", "r")
a,b,c = 0,0,0

cur = 0

for l in file:
    if l == "\n":
        if cur > a:
            c = b
            b = a
            a = cur
        elif cur > b:
            c = b
            b = cur
        elif cur > c:
            c = cur
        cur = 0
    else:
        cur += int(l)
print(a+b+c)