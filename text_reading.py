name = "file.txt"
with open(name) as fname:
    lines=fname.readlines()

# for line in lines:
#     print(line, end="")

# the same

for line in lines:
    print(line.rstrip())