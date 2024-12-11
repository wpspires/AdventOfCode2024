data = open('input.txt').read().split('\n')

print(data)
rows = len(data)
cols = len(data[0])
print(rows, cols)
trailhead_score = 0
trailhead_ratings = 0

def walk_uphill(x, y, visited):
    val = int(data[x][y])
    if val == 9:
        if visited is not None:
            if (x,y) not in visited:
                visited.add((x,y))
                global trailhead_score
                trailhead_score += 1
        else:
            global trailhead_ratings
            trailhead_ratings += 1
        return

    # check left
    if y > 0 and int(data[x][y - 1]) == val + 1:
        walk_uphill(x, y - 1, visited)

    #check right
    if y < cols - 1 and int(data[x][y + 1]) == val + 1:
        walk_uphill(x, y + 1, visited)

    #check up
    if x > 0 and int(data[x - 1][y]) == val + 1:
        walk_uphill(x - 1, y, visited)

    #check down
    if x < rows - 1 and int(data[x + 1][y]) == val + 1:
        walk_uphill(x + 1, y, visited)

#p1
for x in range(rows):
    for y in range(cols):
        if int(data[x][y]) == 0:
            walk_uphill(x,y, set())

print(trailhead_score)

#p2
for x in range(rows):
    for y in range(cols):
        if int(data[x][y]) == 0:
            walk_uphill(x,y, None)

print(trailhead_ratings)