from lib import file

lines = file.readlines()

invalid_ids = []

for range in lines[0].split(','):
    start, end = range.split('-')
    istart, iend = int(start), int(end)
    ss = start[:len(start)//2] if len(start) > 1 else start

    while int(ss+ss) <= iend:
        if int(ss+ss) >= istart:
            invalid_ids.append(ss+ss)
        ss = str(int(ss)+1)
    
print(invalid_ids)

print(len(invalid_ids))
print(sum(int(s) for s in invalid_ids))
