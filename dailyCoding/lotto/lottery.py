# 로또 시뮬레이션

from random import randint

'''
generate_numbers
이 함수는 파라미터로 정수 n을 받습니다. 
무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고, 
그 번호들이 담긴 리스트를 리턴합니다.
'''
def generate_numbers(n):
    numbers = []
    i = 0
    while i < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
            i += 1
    return numbers

'''
draw_winning_numbers
일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다. 
일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.
'''
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    draw_num = sorted(winning_numbers[:6]) + winning_numbers[6:]
    return draw_num

'''
count_matching_numbers
파라미터로 리스트 list_1과 리스트 list_2를 받고,
두 리스트 사이에 겹치는 번호 개수를 리턴합니다.
'''
def count_matching_numbers(list_1, list_2):
    count = 0
    # for i in list_1:
    #     if i in list_2:
    #         count += 1
    count = len(set(list_1)&set(list_2))

    return count

'''
check
참가자의 당첨 금액을 리턴합니다. 
파라미터로 참가자가 뽑은 번호가 담긴 리스트 numbers와 
주최측에서 뽑은 번호가 담긴 리스트 winning_numbers를 받는데요.
numbers는 당연히 번호 여섯 개를 담고 있고,
winning_numbers는 보너스까지 해서 번호 7개를 담고 있다.
'''
'''
당첨금 규칙
참고로 당첨 액수는 아래 규칙에 따라 결정됩니다.

내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)
'''
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    money = 0
    if count == 5:
        for bonus_num in numbers:
            if bonus_num in winning_numbers[6:]:
                money = 500000000
                break
            else:
                money = 100000000
    elif count == 6: money = 1000000000
    elif count == 4: money = 50000
    elif count == 3: money = 5000

    return money

#
# # 테스트
# print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
# print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
#
#
#
# # 테스트
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))
#
#
#
# print(generate_numbers(6))
# print(draw_winning_numbers())
