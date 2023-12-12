


# txt = open("./sample.txt","r")
txt = open("./input.txt","r")
lines = txt.readlines()
total = 0

for a in lines:
    first = "0"
    last = "0"
    for b in a:
        if b.isdigit():
            first = b
            break
    for b in a[::-1]:
        if b.isdigit():
            last = b
            break
    total += int(first+last)

print(total)
