f = open('./inputs/day1_part1', 'r')
elves = []

elf = 0
for line in f.readlines():
    if line == '\n':
        elves.append(elf)
        elf = 0
    else:
        elf += int(line)

print('part 1: ', max(elves))

elves.sort(reverse=True)
top3 = sum(elves[0:3])

print('part 2: ', top3)

f.close()