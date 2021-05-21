
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

# ---------------------------------------------------------------------------

#### 4. 첫번째로 중복되는 항목 찾기 1
```
# 시간 복잡도 O(n)
def find_same_number(some_list):
    # 이미 나온 요소를 저장시켜줄 사전
    elements_seen_so_far = {}

    for element in some_list:
        # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴한다
        if element in elements_seen_so_far:
            return element

        # 해당 요소를 사전에 저장시킨다
        elements_seen_so_far[element] = True
        print(elements_seen_so_far)


print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

# 결과 5 3 3
```

#### 5. 투자의 귀재, 합 구간이 가장 큰 함수

Divide: 구간을 왼쪽 반과 오른쪽 반으로 나눈다.
Conquer: 왼쪽 반에서 가능한 최대 수익과 오른쪽 반에서 가능한 최대 수익을 각각 계산한다.
Combine: 왼쪽 반에서 가능한 최대 수익, 오른쪽 반에서 가능한 최대 수익, 중앙을 관통하면서 가능한 최대 수익을 비교해서 그 중 가장 큰 값을 고른다.


# 풀이 1) brute force (시간 복잡도 O(n^2))
```
def sublist_max(profits, start, end):
    maximum = 0
    for i in range(len(profits)):
        total = 0
        for j in range(i,len(profits)):
            total += profits[j]
            maximum = max(maximum, total)

    return maximum
```
# 풀이 2) brute force : 최대 합 구간 출력
```
def sublist_max(profits, start, end):
    max_list = []
    maximum = 0
    for i in range(len(profits)):
        total = 0
        temp = []
        for j in range(i,len(profits)):
            total += profits[j]
            temp.append(profits[j])
            if maximum < total:
                maximum = total
                max_list = temp.copy()
    print(sum(max_list))

    return max_list
```
# 풀이 3) Divide and Conquer : 시간복잡도 O(n lg n)

가운데를 포함한 수익
1. 가운데 왼쪽 profits[half] 을 포함한 최대수익
2. 가운데 오른쪽 profits[half+1] 을 포함한 최대수익
3. 두 리스트 합치기

```
def max_crossing_sum(profits, start, end):
    mid = (start + end) // 2      # 중간 인덱스

    '''
    왼쪽에서의 가장 큰 수익 계산
    인덱스 mid부터 인덱스 0까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    left_sum = 0                  # 왼쪽 누적 수익
    left_max = profits[mid]       # 왼쪽 최고 수익; 왼쪽 반 중 가장 오른쪽 값으로 초기화

    for i in range(mid, start - 1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)

    '''
    오른쪽에서의 가장 큰 수익 계산
    인덱스 mid+1부터 인덱스 end까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    right_sum = 0                 # 오른쪽 누적 수익
    right_max = profits[mid + 1]  # 오른쪽 최고 수익; 오른쪽 반 중 가장 왼쪽 값으로 초기화

    for i in range(mid + 1, end + 1):
        right_sum += profits[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


def sublist_max(profits, start, end):
    # 범위에 하나의 항목밖에 없으면, 그 항목을 리턴한다
    if start == end:
        return profits[start]

    # 중간 인덱스
    mid = (start + end) // 2

    # 상황별로 최대 수익을 구한다
    max_left = sublist_max(profits, start, mid)
    max_right = sublist_max(profits, mid + 1, end)
    max_cross = max_crossing_sum(profits, start, end)

    # 위 세 경우 중 가장 큰 결괏값을 리턴한다
    return max(max_left, max_right, max_cross)
```

```
# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))

# 결과
# 7
# 28
# 22
# 16
```


# 풀이 3-1) Divide and Conquer : 시간복잡도 O(n)
```
def sublist_max(profits):
    max_profit_so_far = profits[0]  # 반복문에서 현재까지의 부분 문제의 답
    max_check = profits[0]  # 가장 끝 요소를 포함하는 구간의 최대 합

    # 반복문을 통하여 각 요소까지의 최대 수익을 저장한다
    for i in range(1, len(profits)):
        # 새로운 요소를 포함하는 구간의 최대합을 비교를 통해 정한다
        max_check = max(max_check + profits[i], profits[i])

        # 최대 구간 합을 비교를 통해 정한다
        max_profit_so_far = max(max_profit_so_far, max_check)

    return max_profit_so_far

# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))

# 풀이 3-2) Divide and Conquer : 시간복잡도 O(n)

def sublist_max(profits):

    # 변수 정의
    profit_max = 0  # 최대 수익
    temp = 0  # 임시 최대 수익 저장 변수
    
    # 왼쪽 인덱스부터 시작해서, 만약 지금까지의 합(temp)이 0보다 크지 않으면,
    # 앞으로의 수익을 더해도 최대 수익이 증가하는 데에 도움이 되지 않기 때문에
    # 기존의 수익 구간을 전부 버리고, 새로운 인덱스 부터 반영하도록 조건문 설정
    for i in range(len(profits)):
        temp = temp + profits[i] if temp + profits[i] > 0 else 0
        profit_max = max(profit_max, temp)
    
    return profit_max


# 결과
8
7
```

#### 4. 주식 최대 수익 함수
#### 예) [5, 1, 3, 6] 1에 사서 6에 팔면 최대 수익이다

# 풀이 1) Brute Force (빅오 : O(n^2))
```
def max_profit(stock_list):
    # 현재까지의 최대 수익
    max_profit_so_far = stock_list[1] - stock_list[0]

    # 한 번 사고 파는 모든 조합을 본다
    for i in range(len(stock_list) - 1):
        for j in range(i + 1, len(stock_list)):
            # i에서 사고 j에 파는 것이 현재까지의 최대 수익이라면 max_so_far을 바꾼다
            max_profit_so_far = max(max_profit_so_far, stock_list[j] - stock_list[i])

    return max_profit_so_far
```

# 풀이 2) 시간복잡도 O(n)
```
def max_profit(stock_list):
    # 현재까지의 최대 수익
    max_profit_so_far = stock_list[1] - stock_list[0]

    # 현재까지의 최소 주식 가격
    min_so_far = min(stock_list[0], stock_list[1])

    # 주식 가격을 하나씩 확인한다
    for i in range(2, len(stock_list)):
        # 현재 파는 것이 좋은지 확인한다
        max_profit_so_far = max(max_profit_so_far, stock_list[i] - min_so_far)

        # 현재 주식 가격이 최솟값인지 확인한다
        min_so_far = min(min_so_far, stock_list[i])

    return max_profit_so_far
```
```
# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))

#결과
5
-1
11
18
```


#### 5. 계단오르는 경우의 수 구하기

# 풀이 1)
```
fib_cache={}
def staircase(n):
    if n<2:
        return 1
    if n in fib_cache:
        return fib_cache[n]
    else:
        temp=staircase(n-1) + staircase(n-2)
        fib_cache[n] = temp
        return temp

```

# 풀이 2)
```
def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a
```
```
# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))

# 결과
1
13
987
121393
267914296
```
