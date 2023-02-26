name = "file.txt"
# with open(name) as fname:
#     lines=fname.readlines()
# for line in lines:
#     print(line, end="")

# the same
#
# for line in lines:
#     print(line.rstrip())


# lst =[print(row.strip()) for row in lines]

# for l in lst:
#     print(l.strip())

with open(name) as fname:
    line=fname.readline()
#readline() czyta tylko jeden wiersz
for l in line:
    print(len(l.strip()))