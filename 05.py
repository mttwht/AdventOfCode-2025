from lib import file

lines = file.readlines()

empty_index = lines.index("")
fresh_ranges, ingrediants = lines[:empty_index], lines[empty_index + 1 :]

fresh_ranges = [tuple(int(n) for n in fr.split("-")) for fr in fresh_ranges]
ingrediants = [int(i) for i in ingrediants]

fresh_ingrediants = []

for ingrediant in ingrediants:
    for low, high in fresh_ranges:
        if low <= ingrediant <= high:
            fresh_ingrediants.append(ingrediant)
            break

print(len(fresh_ingrediants))
