from lib import file

lines = file.readlines()

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
