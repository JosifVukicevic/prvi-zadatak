arr = [-2,3,1,-5]

x = int(input('Unesite X: '))

sum = x

for x in arr:
    sum = sum + x
    if sum < 1:
        break
    print(sum)