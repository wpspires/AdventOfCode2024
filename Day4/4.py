import re

text = open('input.txt').read()

#forwards and backwards. honestly maybe not worth doing this way (slower overall) since we iterate through the whole text anyway.
p1_count = len(re.findall("XMAS", text))
p1_count += len(re.findall("SAMX", text))

grid = text.split('\n')
rows = len(grid)
cols = len(grid[0])
p2_count = 0
for i in range(rows):
    for j in range(cols):
        #p1
        if grid[i][j] == "X":
            #check up
            if i > 2:
                if grid[i-1][j] == "M" and grid[i-2][j] == "A" and grid[i-3][j] == "S":
                    p1_count += 1
                # check up-right
                if j < cols - 3:
                    if grid[i - 1][j + 1] == "M" and grid[i - 2][j + 2] == "A" and grid[i - 3][j + 3] == "S":
                        p1_count += 1
                # check up-left
                if j > 2:
                    if grid[i - 1][j - 1] == "M" and grid[i - 2][j - 2] == "A" and grid[i - 3][j - 3] == "S":
                        p1_count += 1
            #check down
            if i < rows - 3:
                if grid[i+1][j] == "M" and grid[i+2][j] == "A" and grid[i+3][j] == "S":
                    p1_count += 1
                #check down-right
                if j < cols - 3:
                    if grid[i + 1][j + 1] == "M" and grid[i + 2][j + 2] == "A" and grid[i + 3][j + 3] == "S":
                        p1_count += 1
                #check down-left
                if j > 2:
                    if grid[i + 1][j - 1] == "M" and grid[i + 2][j - 2] == "A" and grid[i + 3][j - 3] == "S":
                        p1_count += 1
        #p2
        if 0 < i < rows - 1 and 0 < j < cols - 1 and grid[i][j] == "A":
            if (grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S") or (grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M"):
                if (grid[i - 1][j + 1] == "M" and grid[i + 1][j - 1] == "S") or (grid[i - 1][j + 1] == "S" and grid[i + 1][j - 1] == "M"):
                    p2_count += 1
print(p1_count)
print(p2_count)
