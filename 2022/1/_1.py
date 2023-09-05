# file = open(r"2022\1\input_sample.txt", "r")
file = open(r"2022\1\input.txt", "r")
cur_cost = 0
i = 1
index_min = 1
prev_cost = 0
for a in file:
    if a == "\n":
        if cur_cost > prev_cost:
            prev_cost = cur_cost
            index_min = i
        cur_cost = 0
        i += 1
    else:
        cur_cost += int(a)
print(index_min,prev_cost)