x= input()
y= input()

x = int(x)
sum = 0

for i in range(len(y)):
    print(x * int(y[-1 - i]))
    sum += x * int(y[-1 - i]) * 10 ** i

print(sum)
