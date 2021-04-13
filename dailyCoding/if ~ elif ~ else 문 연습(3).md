# if ~ elif ~ else 문 연습(3)
### 입력된 알파벳의 대소문자를 구별하기
### 대소문자를 구별하는 .isupper() / .islower() 사용
```
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

* 입력 : X
K 는 대문자 입니다.  
