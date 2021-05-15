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
