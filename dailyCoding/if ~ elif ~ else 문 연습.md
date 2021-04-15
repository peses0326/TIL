# if ~ elif ~ else 문 연습
## 1. 입력받은 값의 모든 약수 구하기

```py
x = int(input())

for a in range(1, x+1):
    if x%a == 0:
        print (f'{a}(은)는 {x}의 약수입니다.')
```
### 결과
* 입력 9

 1(은)는 9의 약수입니다.  
 3(은)는 9의 약수입니다.  
 9(은)는 9의 약수입니다.

## 2. 입력받은 값의 모든 약수 구하고 약수가 2개인 소수를 표기하기
```py
x = int(input())
count=0
for a in range(1, x+1):
    if x%a == 0:
        print (f'{a}(은)는 {x}의 약수입니다.')
        count+=1
if count == 2:
    print (f'{x}(은)는 1과 {x}로만 나눌 수 있는 소수입니다.')
```

### 결과
* 입력 7
1(은)는 7의 약수입니다.   
7(은)는 7의 약수입니다.   
7(은)는 1과 7로만 나눌 수 있는 소수입니다.  

## 3. 입력된 알파벳의 대소문자를 구별하기
### 대소문자를 구별하는 `.isupper()` / `.islower()` 사용
```py
x = input()
if x.islower():
    print(f'{x} 는 소문자 입니다.')
elif x.isupper():
    print(f'{x} 는 대문자 입니다.')
else:
    print(f'{x} 는 알파벳이 아니거나 혼합형입니다.')
```
### 결과
* 입력 : f  
f 는 소문자 입니다.  

* 입력 : K  
K 는 대문자 입니다.    


## 4. 가위 바위 보 게임
### (1) random.choice 함수를 이용
```py
import random

all = ['가위','바위','보']
Man1 = random.choice(all)
Man2 = random.choice(all)

print('Man1 :',Man1,'Man2 :',Man2)

if Man1 == Man2:
    print('Result : Draw!')
elif Man1 == '가위' and Man2 == '보':
    print('Result : Man1 Win!')
elif Man1 == '바위' and Man2 == '가위':
    print('Result : Man1 Win!')
elif Man1 == '보' and Man2 == '바위':
    print('Result : Man1 Win!')
else :
    print('Result : Man2 Win!')
```

### (2) input() 을 받아 이용
```py
Man1 = input()
Man2 = input()

if Man1 == Man2:
    print('Result : Draw!')
elif Man1 == '가위' and Man2 == '보':
    print('Result : Man1 Win!')
elif Man1 == '바위' and Man2 == '가위':
    print('Result : Man1 Win!')
elif Man1 == '보' and Man2 == '바위':
    print('Result : Man1 Win!')
else :
    print('Result : Man2 Win!')
```    
    
    
    
    
    
