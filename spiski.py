a = [int(i) for i in input().split()]
print(a)
#алгоритм поиска минимума
m = a[0]
for x in a:
    if m > x:
        m = x
        print(m)