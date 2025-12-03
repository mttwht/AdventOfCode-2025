import sys

from lib import file

if len(sys.argv) > 1 and sys.argv[1] == "test":
    lines = file.readlines("input/01-example.txt")
else:
    lines = file.readlines("input/01.txt")

pos = 50
password = 0

for line in lines:
    if line[0] == 'L':
        pos -= int(line[1:])
    elif line[0] == 'R':
        pos += int(line[1:])
    
    if pos % 100 == 0:
        password += 1
        
print(password)
