#### <1. 기본 >

##### 1. palindrome : 앞뒤가 같은 단어 찾기 (for문)

```
def is_palindrome(word):
    revword = list(reversed(word))
    for i in range(len(word)):
        if word[i] != revword[i]:
            return False
    return True
    
print(is_palindrome('sonos'))
print(is_palindrome('gamja'))
```

##### 2. 선형탐색

```
def linear_search(element, some_list):
    for i in some_list:
        if element == i:
            return some_list.index(i)
    return None
    
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
```

##### 3. 이진탐색 binary search : 절반으로 잘라가며 요소 찾기

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
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

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
hanoi(3, 1, 3)

# 결과 
1번 원판을 1번 기둥에서 3번 기둥으로 이동
2번 원판을 1번 기둥에서 2번 기둥으로 이동
1번 원판을 3번 기둥에서 2번 기둥으로 이동
3번 원판을 1번 기둥에서 3번 기둥으로 이동
1번 원판을 2번 기둥에서 1번 기둥으로 이동
2번 원판을 2번 기둥에서 3번 기둥으로 이동
1번 원판을 1번 기둥에서 3번 기둥으로 이동
```
