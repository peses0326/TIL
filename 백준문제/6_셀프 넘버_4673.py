# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자.
# 예, d(75) = 75+7+5 = 87이다.
all_num = set(range(1, 10001))
not_self_num = set()
self_num = []

def d(n):
    sum = n
    for i in str(n):
        sum += int(i)
    not_self_num.add(sum)
    return


for i in range(1, 10001):
    d(i)

self_num = all_num - not_self_num
for i in sorted(self_num):
    print(i)
