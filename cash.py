from cs50 import get_float


while True:
    x = get_float("Change owed: ")
    if x >= 0:
        break
x = round(x * 100)
count = 0

while x > 0:
    if x >= 25:
        x -= 25
        count += 1
    elif x >= 10:
        x -= 10
        count += 1
    elif x >= 5:
        x -= 5
        count += 1
    elif x >= 1:
        x -= 1
        count += 1

#print number of coins used
print(count)