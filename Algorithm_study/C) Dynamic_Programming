### C) Dynamic Programming
#### 최적 부분 구조(optimal substructure), 중복되는 부분 문제(Overlapping Subproblems)

#### 1. Memoiztion 방식의 피보나치 함수
```
def fib_memo(n, cache):
    if n < 3:
        return 1
    if n in cache:
        return cache[n]

    cache[n] = fib_memo(n - 1,cache) + fib_memo(n - 2,cache)
    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)

# 테스트
print(fib(10))
print(fib(50))
print(fib(100))

# 결과
# 55
# 12586269025
# 354224848179261915075
```

#### 2. tubulation 방식의 피보나치 함수
```
def fib_tab(n):
    # 이미 계산된 피보나치 수를 담는 리스트
    fib_table = [0, 1, 1]

    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    # 피보나치 n번째 수를 리턴한다
    return fib_table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
```

#### 3. 공간복잡도가 O(1)인 피보나치 함수
```
def fib_optimized(n):
    current = 1
    previous = 0

    # 반복적으로 위 변수들을 업데이트한다.
    for i in range(1, n):
        current, previous = current + previous, current

    # n번재 피보나치 수를 리턴한다.
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))

# 결과 
# 987
# 53316291173
# 146178119651438213260386312206974243796773058
```

#### 4. 장사 분석, 최대 수익 출력 함수

# (1)
```
def max_profit_memo(price_list, count, cache):
    # Base Case: 0개 혹은 1개면 부분 문제로 나눌 필요가 없기 때문에 가격을 바로 리턴한다
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    # 이미 계산한 값이면 cache에 저장된 값을 리턴한다
    if count in cache:
        return cache[count]

    # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
    # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
    # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache) 
                 + max_profit_memo(price_list, count - i, cache))

    # 계산된 최대 수익을 cache에 저장
    cache[count] = profit

    return profit

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)
```

# (2)
```
def max_profit_memo(price_list, count, cache):
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    if count in cache:
        return cache[count]

    maximum = 0

    for i in range(1, len(price_list)):
        if count < i:
            break
        if maximum < price_list[i] + max_profit_memo(price_list, count - i, cache):
            maximum = price_list[i] + max_profit_memo(price_list, count - i, cache)

    cache[count] = maximum
    return cache[count]


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)
```
```
# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))

# 결과 1200 2500 2400
```

##### 5. Tabulation 방식의 새꼼달꼼 장사 최대 수익 함수

#### 1) 일반 풀이
```
def max_profit(price_list, count):
    if count <2:
        return price_list[count]

    profit = 0

    if count < len(price_list):
        profit = price_list[count]

    for i in range(1,len(price_list)-1):
        if count < i:
            break
        if profit < price_list[i] + max_profit(price_list,count - i):
            profit = price_list[i] + max_profit(price_list,count - i)
            
    return profit
```
