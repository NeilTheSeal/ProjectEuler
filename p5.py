list1 = []
i = 20
result = False

while not result:
    j = 2
    while j <= 20:
        if i % j != 0:
            result = False
            j = 21
        else:
            result = True
            j += 1
    if result:
        list1.append(i)
    i += 20

print(list1)
