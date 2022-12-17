f = open('./inputs/day4', 'r')
lines = f.readlines()
f.close()

part1 = 0
part2 = 0
for line in lines:
    pairs = list(map(lambda line: 
        list(map(lambda x: int(x), line.split('-'))),
        line.split(',')))
    largest_key = 0 if (pairs[0][1] - pairs[0][0]) >= (pairs[1][1] - pairs[1][0]) \
        else 1
    largest = pairs[largest_key]
    smallest = pairs[1 - largest_key]
    if smallest[0] >= largest[0] and smallest[1] <= largest[1]:
        part1 += 1

    if pairs[0][0] <= pairs[1][1] and pairs[1][0] <= pairs[0][1]:
        part2 += 1

print('part1', part1)
print('part2', part2)