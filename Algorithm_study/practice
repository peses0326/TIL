
## 알고리즘 연습

#### 1. Brute Force
#### 최대 합 구간을 구하는 함수

# (1)
```
def sublist_max(profits):
    start = 0
    max_profit = []

    for i in range(0, len(profits)):
        compare = []
        for j in range(i, len(profits)):
            compare.append(profits[j])
            # print(sum(compare))

            if sum(compare) > sum(max_profit):
                max_profit = compare.copy()
                print(max_profit)
                start = profits.index(max_profit[0])

    return sum(max_profit)

```
# (2)
```
def sublist_max(profits):
    max_profit = profits[0]  # 최대 수익

    for i in range(len(profits)):
        # 인덱스 i부터 j까지 수익의 합을 보관하는 변수
        total = 0

        for j in range(i, len(profits)):
            # i부터 j까지 수익의 합을 계산
            total += profits[j]

            # i부터 j까지 수익의 합이 최대 수익이라면, max_profit 업데이트
            max_profit = max(max_profit, total)

    return max_profit
```    
```
# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))

# 결과
# 15
# 8
# 27
```

#### 2. 거듭 제곱 계산 함수 (x ** y)
```
# (1) 시간 복잡도 O(y)
def power(x, y):
    total = 1

    # x를 y번 곱해 준다
    for i in range(y):
        total *= x

    return total
```
```
# (2) 시간 복잡도 O(y)

def power(x, y):
    if y == 1:
        return x
    elif y>1:
        x = x * power(x,y-1)
    return x
```

# (3) 시간 복잡도 O(lg y)
```
def power(x, y):
    if y == 0:
        return 1

    # 계산을 한 번만 하기 위해서 변수에 저장
    subresult = power(x, y // 2)

    # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
    if y % 2 == 0:
        return subresult * subresult
    else:
        return x * subresult * subresult
# y가 8인 경우 함수가 4번 호출되고, y가 32인 경우 6번 호출
# power(2, 8)
# power(2, 4)
# power(2, 2)
# power(2, 1)
```
```
# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))

# 결과 
# 243
# 15625
# 40353607
```

#### 3. 빠르게 산 오르기
#### 리스트 : 약수터 위치, 한번에 capacity 칸 이동 가능
#### 최소 들러야하는 약수터 리스트 출력
```
def select_stops(water_stops, capacity):
    # 약수터 위치 리스트
    stop_list = []

    # 마지막 들른 약수터 위치
    prev_stop = 0

    for i in range(len(water_stops)):
        # i 지점까지 갈 수 없으면, i - 1 지점 약수터를 들른다
        if water_stops[i] - prev_stop > capacity:
            stop_list.append(water_stops[i - 1])
            prev_stop = water_stops[i - 1]

    # 마지막 약수터는 무조건 간다
    stop_list.append(water_stops[-1])

    return stop_list

# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
```
```
# 결과
# [4, 7, 11, 13, 16, 20, 24, 26]
# [5, 8, 12, 17, 23, 28, 32, 38, 44, 47]
```
