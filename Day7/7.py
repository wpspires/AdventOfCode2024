from operator import add, mul

def concat(x,y): return int(str(x)+str(y))

operations = (add, mul, concat)

def run_operation(entries, local_goal):
    if len(entries) == 1:
        return entries[0] == local_goal

    x,y,*z = entries

    for operation in operations:
        if run_operation([operation(x, y), *z], local_goal):
            return local_goal
    return 0


equations = open('input.txt').read().split('\n')

calibration_result = 0
for equation in equations:
    goal, *operands = map(int, equation.replace(':','').split())
    calibration_result += run_operation(operands, goal)

print(calibration_result)
