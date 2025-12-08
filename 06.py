import math

from lib import file

lines = file.readlines()

numgrid = [[num for num in line.split()] for line in lines]
numgrid = [*zip(*numgrid)]

answers = []
for problem in numgrid:
    numbers, operator = problem[:-1], problem[-1]
    numbers = [int(x) for x in numbers]

    if operator == '*':
        answers.append(math.prod(numbers))
    elif operator == '+':
        answers.append(sum(numbers))

print(sum(answers))
