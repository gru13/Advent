# file = open(r"2022\2\input_sample.txt", "r")
file = open(r"2022\2\input.txt", "r")

wdl = {
    "A": {"X": 3, "Y": 4, "Z": 8},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 2, "Y": 6, "Z": 7},
}

count = 0
for a in file:
    count += wdl[a[0]][a[2]]
print(count)
