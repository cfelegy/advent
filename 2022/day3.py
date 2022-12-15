f = open('./inputs/day3', 'r')
lines = f.readlines()
f.close()

def priority(letter: str):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27

priority_sum = 0
for line in lines:
    middle = len(line)//2
    comp1 = line[0:middle]
    comp2 = line[middle:]
    match_priority = 0
    for char in comp2:
        if char not in comp1: continue
        match_priority = priority(char)
    priority_sum += match_priority

print('part1', priority_sum)

badge_priority_sum = 0
for group_num in range(len(lines)//3):
    group = lines[group_num*3:(group_num+1)*3]
    group_counter = dict()
    for sack in group:
        sack_counter = dict()
        for char in sack.strip():
            if sack in group_counter: continue
            else: sack_counter[char] = 1
        for k in sack_counter.keys():
            if k in group_counter: group_counter[k] += 1
            else: group_counter[k] = 1
    vals = list(group_counter.values())
    keys = list(group_counter.keys())
    badge = keys[vals.index(max(vals))]

    badge_priority_sum += priority(badge)

print('part2', badge_priority_sum)