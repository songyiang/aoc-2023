from itertools import combinations
import re
import z3

### PART 1 ###

hailstones = []
with open('input.txt', 'r') as f:
    for line in f:
        l = re.split(', | @ ', line.strip())
        x, y, z, dx, dy, dz = [int(i) for i in l]
        hailstones.append((x, y, z, dx, dy, dz))

xTestStart, xTestEnd = 200000000000000, 400000000000000
yTestStart, yTestEnd = 200000000000000, 400000000000000

numIntersections = 0
for a, b in combinations(hailstones, 2):
    ax, ay, _, adx, ady, _ = a
    bx, by, _, bdx, bdy, _ = b

    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line_segment
    x1, y1, x2, y2 = ax, ay, ax + adx, ay + ady
    x3, y3, x4, y4 = bx, by, bx + bdx, by + bdy
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator != 0:
        t = float((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
        u = float((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / denominator
        if t >=0 and u >= 0 and xTestStart <= ax + t * adx <= xTestEnd and yTestStart <= ay + t * ady <= yTestEnd:
            numIntersections += 1
print(numIntersections)

### PART 2 ###

solver = z3.Solver()

ix, iy, iz, dix, diy, diz = z3.Ints('ix iy iz dix diy diz')
time = [z3.Int(f't{i}') for i in range(len(hailstones))]

for i, (x, y, z, dx, dy, dz) in enumerate(hailstones):
    solver.add(ix + time[i] * dix == x + time[i] * dx)
    solver.add(iy + time[i] * diy == y + time[i] * dy)
    solver.add(iz + time[i] * diz == z + time[i] * dz)
solver.check()
print(solver.model().evaluate(ix + iy + iz))
