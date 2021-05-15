### B) Divide and Conquer

#### 1. 1부터 nn까지 더하는 예시
```

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
