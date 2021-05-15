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
