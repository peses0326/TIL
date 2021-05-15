#### <1. 기본 >
##### 1. palindrome : 앞뒤가 같은 단어 찾기 (for문)
```
def is_palindrome(word):
    revword = list(reversed(word))
    for i in range(len(word)):
        if word[i] != revword[i]:
            return False
    return True
```

##### 2. 선형탐색
```
def linear_search(element, some_list):
    for i in some_list:
        if element == i:
            return some_list.index(i)
    return None
```

##### 3. 이진탐색 : 절반으로 잘라가며 요소 찾기
```
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
```

### <2. 재귀함수 >

##### 1. 연습
```
def countdown(n):
    if n > 0 :
        print(n)
        countdown(n-1)
#countdown(4)를 출력하면
#4 3 2 1

def countup(n):
    if n > 0 :
        countup(n-1)
        print(n)
#countup(4)를 출력하면
#1 2 3 4
```

##### 2. n번째 피보나치 수를 리턴
```
def fib(n):
    # 코드를 입력하세요.
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))
```


##### 3. 1부터 n까지의 합을 리턴
```
def triangle_number(n):
    # base case
    if n == 1:
        return 1

    return n + triangle_number(n - 1)


# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))
```

#### 4. 각 자릿수의 합 리턴
```
def sum_digits(n):
    # print(n)
    if n < 10:
        return n

    return n % 10 + sum_digits(n // 10)

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# 결과 14 15 16 11 20
```

#### 5. 파라미터 some_list를 거꾸로 뒤집는 함수
```
def flip(some_list):
    if len(some_list) == 1:
        return some_list
    return some_list[-1:] + flip(some_list[:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# 결과 [9, 8, 7, 6, 5, 4, 3, 2, 1]
```
#### 6. 리스트 내 요소 찾는 재귀함수
```
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    midpoint = (end_index + start_index) // 2
    if start_index > end_index:
        return None

    if element == some_list[midpoint]:
        return midpoint
    elif element < some_list[midpoint]:
        return binary_search(element, some_list, start_index, midpoint - 1)
    else:
        return binary_search(element, some_list, midpoint + 1, end_index)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

# 결과 : 0 None 2 1 4
```

#### 7. 하노이의 탑
```
def move_disk(disk_num, start_peg, end_peg):
    # print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))
    print('0')


def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg

        # 1. 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
        hanoi(num_disks - 1, start_peg, other_peg)

        # 2. 가장 큰 원판을 start_peg에서 end_peg로 이동
        move_disk(num_disks, start_peg, end_peg)

        # 3. 나머지 원판들을 other_peg에서 end_peg로 이동
        hanoi(num_disks - 1, other_peg, end_peg)


# 테스트 
hanoi(1, 1, 3)

# 결과 
1번 원판을 1번 기둥에서 3번 기둥으로 이동
2번 원판을 1번 기둥에서 2번 기둥으로 이동
1번 원판을 3번 기둥에서 2번 기둥으로 이동
3번 원판을 1번 기둥에서 3번 기둥으로 이동
1번 원판을 2번 기둥에서 1번 기둥으로 이동
2번 원판을 2번 기둥에서 3번 기둥으로 이동
1번 원판을 1번 기둥에서 3번 기둥으로 이동
```
#### 1. Brute Force
#### 두 카드 뭉치에서 1개씩 뽑아 가장 큰 곱을 구하기
```
def max_product(left_cards, right_cards):
    times = []
    for i in left_cards:
        for j in right_cards:
            times.append(i*j)
    max = times[0]
    for a in times:
        if a > max:
            max = a
    return max


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))

#결과 : 24 32 28
```
#### 2. 두 매장 사이가 가까운 곳 출력 함수
```
# 제곱근 사용을 위한 sqrt 함수
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    list_1, list_2 = [], []
    dis = distance(coordinates[0],coordinates[1])
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            if dis > distance(coordinates[i], coordinates[j]):
                dis = distance(coordinates[i], coordinates[j])
                list_1 = coordinates[i]
                list_2 = coordinates[j]

    return [list_1,list_2]


# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))

#결과 : [(2, 3), (3, 4)]
```

#### 3. 물이 담길수 있는 양 출력 함수
```
def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height



# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

#결과 : 10 6
```

# ---------------------------------------------------------------------------
### B) Divide and Conquer

#### 1. 11부터 nn까지 더하는 예시
```
def consecutive_sum(start, end):
    def consecutive_sum(start, end):
        # base case
        if end == start:
            return start

        # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다 (Divide)
        mid = (start + end) // 2

        # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine).
        return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))

# 결과 : 55 5050 32131 75466
```

#### 2. 합병 정렬 알고리즘 merge함수
```
'''
#(1)
def merge(list1, list2):
    new = []
    while 1:
        if list1 == [] or list2 == []:
            new += list1 + list2
            break
        elif list1[0] < list2[0]:
            new.append(list1.pop(0))
        elif list1[0] > list2[0]:
            new.append(list2.pop(0))

    return new
'''

'''
#(2)
def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list = merged_list + list1[i:] + list2[j:]
    
    return merged_list
'''


# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))

#결과 
# [1]
# [1]
# [1, 2]
# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 3, 4, 6, 7, 8, 9, 10]
```

#### 3. 합병 함수를 Divide and Conquer 방식으로 작성
```
def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list = merged_list + list1[i:] + list2[j:]

    return merged_list

# 합병 정렬
def merge_sort(my_list):
    if len(my_list)==1:
        return my_list
    mid = len(my_list)//2
    return merge(merge_sort(my_list[:mid]),merge_sort(my_list[mid:]))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

# 결과
# [1, 3, 5, 7, 9, 11, 11, 13]
# [1, 5, 7, 9, 13, 15, 28, 30, 48]
# [1, 1, 2, 2, 4, 4, 4, 5, 6, 6, 7, 7, 10, 11, 13, 15]
```

#### 4. 퀵정렬로 함수 정렬
```
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1],my_list[index2]=my_list[index2],my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    pivot = my_list[end]
    b = 0
    for i in range(start,end):
        if my_list[i] <= pivot:
            swap_elements(my_list,i,b)
            b += 1
    swap_elements(my_list,end,b)

    return b

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)

# 결과 
# [4, 3, 2, 1, 5, 6, 7]
# 4
# [1, 2, 3, 4, 6, 5, 6]
# 3
```


#### 5. Divide and Conquer 방식으로 퀵정렬을 해보자

# (1)두 요소의 위치를 바꿔주는 helper function
```
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i = start
    b = start
    pivot = my_list[end]

    # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
    while i < end:
        # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
        if my_list[i] <= pivot:
            swap_elements(my_list, i, b)
            b += 1
        i += 1
    swap_elements(my_list, end, b)

    return b


# 퀵 정렬
def quicksort(my_list, start, end):
    if end - start < 1:
        return
    mid = partition(my_list, start, end)
    quicksort(my_list, start, mid - 1)
    quicksort(my_list, mid + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)
```

# (2) 1번의 퀵 함수 가공
```
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i = start
    b = start
    pivot = my_list[end]

    # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
    while i < end:
        # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
        if my_list[i] <= pivot:
            swap_elements(my_list, i, b)
            b += 1
        i += 1
    swap_elements(my_list, end, b)

    return b


# 퀵 정렬
def quicksort(my_list, start =0, end=None):
    if end == None:
        end = len(my_list)-1
    if end - start < 1:
        return
    mid = partition(my_list, start, end)
    quicksort(my_list, start, mid - 1)
    quicksort(my_list, mid + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)
```

# ---------------------------------------------------------------------------
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
#### 2) Tabulation 방식
```
def max_profit(price_list, count):
    profit_table = [0]

    for i in range(1, count + 1):

        profit = 0

        if i < len(price_list):
            profit = price_list[i]

        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

        profit_table.append(profit)

    return profit_table[count]
```
```
# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))

# 결과 : 2000 2400 1800
```

# ---------------------------------------------------------------------------
## D) Greedy Algorithm
#### 1. 최소 동전으로 거슬러주기
```
def min_coin_count(value, coin_list):
    # 누적 동전 개수
    count = 0
    # coin_list의 값들을 큰 순서대로 본다
    for coin in sorted(coin_list, reverse=True):
        # 현재 동전으로 몇 개 거슬러 줄 수 있는지 확인한다
        count += (value // coin)

        # 잔액을 계산한다
        value %= coin
        
    return count


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))

#결과 : 10 5 49 70
```
#### 2. 세 사람의 카드게임에서 한장씩 뽑아 가장 큰 곱 출력 함수
```
def max_product(card_lists):
    max_result = 1

    for i in card_lists:
        max_result *= max(i)
    return max_result

# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))

# 결과 : 24 244944 10800 12600
```


#### 3. 최소 벌금 문제 : 리스트는 5명이 프린트 해야할 페이지 수(1장당 1분,분당 1$)

# (1)
```
def min_fee(pages_to_print):
    pages_to_print.sort()
    fee = 0
    total_fee = 0
    for i in pages_to_print:
        fee += i
        total_fee += fee
    return total_fee
```
# (2)
```
def min_fee(pages_to_print):
    # 인풋으로 받은 리스트를 정렬시켜 준다
    sorted_list = sorted(pages_to_print)

    # 총 벌금을 담을 변수
    total_fee = 0

    # 정렬된 리스트에서 총 벌금 계산
    for i in range(len(sorted_list)):
        total_fee += sorted_list[i] * (len(sorted_list) - i)

    return total_fee
```
```
# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))

# 결과
# 39
# 10
# 32
# 188
```

#### 4. 수업 겹치지 않게 수강하기

# (1)
```
def course_selection(course_list):
    course_list.sort()

    subject = [course_list[0]]

    for i in range(1, len(course_list)):
        if subject[0][1] > course_list[i][1]:
            subject = [course_list[i]]

    end = subject[0][1]

    for i in course_list[2:]:
        if end < i[0]:
            subject.append(i)
            end = subject[-1][1]

    return subject
```
# (2)
```
def course_selection(course_list):
    # 수업을 끝나는 순서로 정렬한다
    sorted_list = sorted(course_list, key=lambda x: x[1])

    # 가장 먼저 끝나는 수업은 무조건 듣는다
    my_selection = [sorted_list[0]]

    # 이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
    for course in sorted_list:
        # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹친다
        if course[0] > my_selection[-1][1]:
            my_selection.append(course)

    return my_selection
```
```
# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))

# 결과
# [(2, 3), (4, 5), (6, 8), (9, 10)]
# [(1, 2), (3, 4), (5, 7), (8, 9)]
# [(1, 3), (4, 7), (8, 10), (13, 16)]
```

# ---------------------------------------------------------------------------

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





