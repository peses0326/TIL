# 함수 연습


## 1. 단어를 거꾸로 출력하기
```
text = list(map(str, str(input())))

rev = []
for i in range(len(text) - 1, -1, -1):
    rev.append(text[i])
    if i == 0:
        if ''.join(rev) == ''.join(text):
            print(''.join(rev))
            print('입력하신 단어는 회문(Palindrome)입니다.')
        else:
            print(''.join(rev))
```

## 2. 가위바위보 게임
```
def game(Man1, Man2):
    list = [Man1, Man2]
    list.sort()
    Man1 = list[0]
    Man2 = list[1]

    if Man1 == Man2:
        print('비겼다!')
    elif Man1 == '가위' and Man2 == '바위':
        print('바위가 이겼습니다!')
    elif Man1 == '가위' and Man2 == '보':
        print('가위가 이겼습니다!')
    elif Man1 == '바위' and Man2 == '보':
        print('보가 이겼습니다.')
    else:
        print('다시 시도하렴')


name1 = input()
name2 = input()
Man1 = input()
Man2 = input()

game(Man1, Man2)
```

## 3. 정수가 소수인지 판단하는 함수 만들기
```
def prime(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    if count == 2:
        print('소수입니다.')
    else:
        print('소수가 아닙니다.')

x = int(input())
prime(x)
```

## 4. 피보나치 수열 출력함수
```
def Fibonacci(x):
    fibo = []
    for a in range(x):
        if a < 2:
            fibo.append(1)
        else:
            fibo.append(fibo[a - 2] + fibo[a - 1])

    print(fibo)


x = int(input())
Fibonacci(x)
```

## 5. 리스트의 중복값 제거함수
```
def a(A):
    print(A)
    list = []
    for x in A:
        if x not in list:
            list.append(x)
    print(list)

A = [1, 2, 3, 4, 3, 2, 1]
a(A)
```

## 6. 리스트에 값이 들어있는지 확인하는 함수
```
def findFator(A):
    a = 5
    b = 10
    if a in A:
        print(f'{a} => True')
    else:
        print(f'{a} => False')
    if b in A:
        print(f'{b} => True')
    else:
        print(f'{b} => False')

A = [2, 4, 6, 8, 10]
print(A)
findFator(A)

```

## 7. 팩토리얼 함수
```
def fac(x):
    fac = 0
    if x > 0:
        fac = 1
        for i in range(1, x + 1):
            fac *= i
    return fac


x = int(input())
print(fac(x))

```

## 8. 다중입력 값의 제곱을 구하는 함수
```
def square(x):
    x = x * x
    return x


a, b = map(int, input().split(','))
result_a = square(a)
result_b = square(b)

print(f'square({a}) => {result_a}')
print(f'square({b}) => {result_b}')

```

## 9. 더 긴 값을 골라내기
```
def longer(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        return a
    else:
        return b


a, b = map(str, input().split(', '))
result = longer(a, b)
print(result)

```

## 10. 카운트 다운하는 함수
```
def countdown(x):
    if x == 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    else:
        for a in range(10, 0, -1):
            print(a)


countdown(0)
countdown(10)
```
