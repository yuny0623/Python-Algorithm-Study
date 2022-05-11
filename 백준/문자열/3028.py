# 1016
cup = [1, 0, 0]
for o in input():
    if o == 'A':
        cup[0], cup[1] = cup[1], cup[0]
    elif o == 'B':
        cup[1], cup[2] = cup[2], cup[1]
    elif o == 'C':
        cup[0], cup[2] = cup[2], cup[0]

print(cup.index(1) + 1)