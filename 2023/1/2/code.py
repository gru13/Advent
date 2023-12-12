

txt = open("./input.txt", 'r')
lines = txt.readlines()
total = 0
Map  = ["zero", "one","two","three","four","five","six","seven","eight","nine"]

for line in lines:
    number = []
    for i in range(len(line)):
        if line[i].isdigit():
            number.append(Map[int(line[i])])
            continue
        for ma in Map:
            if i+len(ma) < len(line) and line[i:i+len(ma)] == ma:
                number.append(ma)
    print(number)
    if len(number) > 0:
        total += int(str(Map.index(number[0])) + str(Map.index(number[-1])))
        # print(int(str(Map.index(number[0])) + str(Map.index(number[-1]))))
print(total)
