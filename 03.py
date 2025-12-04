from lib import file

banks = file.readlines()

total = 0

for bank in (list(b) for b in banks):
    # ibank = [int(x) for x in bank]
    i1 = max(bank[:-1])
    i2 = max(bank[bank.index(i1)+1:])
    total += int(i1+i2)

print(total)
    