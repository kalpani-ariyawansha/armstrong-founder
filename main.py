print("Finding armstrong numbers")

x = 0
while x <= 100_000:
    p = str(x)
    num = 0
    for c in p:
        num += int(c) ** len(p)
    if num == x:
        print("Number is: ", x)
    x += 1
