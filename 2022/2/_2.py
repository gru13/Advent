file = open(r"2022\2\input.txt", "r")
wdl = {
    "A": {"X": 4, "Y": 8, "Z": 3},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 7, "Y": 2, "Z": 6},
}
count = 0
for a in file:
    count += wdl[a[0]][a[2]]
print(count)