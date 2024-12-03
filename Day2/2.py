#p1
#def is_safe_row_ascending(local_row: list[int]) -> bool:
#    for x in range(1, len(local_row)):
#        diff = local_row[x] - local_row[x - 1]
#        if diff > 3 or diff < 1:
#            return False
#    return True

#def is_safe_row_descending(local_row: list[int]) -> bool:
#    for x in range(1, len(local_row)):
#        diff = local_row[x - 1] - local_row[x]
#        if diff > 3 or diff < 1:
#            return False
#    return True

#p2
def is_safe_row_ascending(local_row: list[int]) -> bool:
    faults = 0
    for x in range(1, len(local_row)):
        diff = local_row[x] - local_row[x - 1]
        if diff > 3 or diff < 1:
            return False
    return True

def is_safe_row_descending(local_row: list[int]) -> bool:
    faults = 0
    for x in range(1, len(local_row)):
        diff = local_row[x - 1] - local_row[x]
        if diff > 3 or diff < 1:
            return False
    return True

reports = open('input.txt').read().split('\n')
safe = 0
for report in reports:
    row = list(map(int, report.split()))

    if row[0] < row[1]:
        if is_safe_row_ascending(row):
            safe += 1
    elif row[0] > row[1]:
        if is_safe_row_descending(row):
            safe += 1

print(safe)


