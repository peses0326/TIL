x = input()
x = int(x)
count = 0

def cycle(n, count):
    sum_n = n // 10 + n % 10
    if n < 10:
        n = n * 10
        sum_n = n // 10 + n % 10
        n = n // 10
    n = n % 10 * 10 + sum_n % 10
    count += 1

    if n == x:
        return count
    return cycle(n, count)

print(cycle(x, count))