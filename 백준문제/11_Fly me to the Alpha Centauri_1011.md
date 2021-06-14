#### 문제는 이해가 되었고 내 머릿속에 다 그렸는데 코드로 어떻게 짜야할지 고민하다가 시간을 많이 쓴 문제..
#### 결국 해났다,,!
#### 다풀고 구글에 다른 사람들 어떻게 풀었나 봤는데 from math import sqrt 해서 제곱근으로 뭐 계산해서 풀던데
#### 이해는 대강 갔지만 저렇게 어렵게 풀어야하나.. 저건 읽고도 설명 못할듯 ,,
#### 아래 내 코드의 핵심은 distance가 0부터 음수인 구간은 이동 횟수가 일정하고 양수로 전환될 때 횟수가 1늘어난다는 규칙을 이용했다!
## 뿌듯해 ><
##
#### 코드가 2개인데 맨 밑 함수를 써서 먼저 짰는데 아래 풀이랑 코드도 똑같고 출력도 같지만 백준이 자꾸 오답이라 했다,, 왜인지,,,ㅠㅠ
#### 함수 안쓰고 반복문 안에 반복문 넣으니까 되는데,,
###### 백준은 알다가도 모르겠다
##
##
* 풀이
```
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    distance = y - x
    count = 0
    move = 1
    if distance < 4:
        print(distance)
        continue

    while distance > 0:
        distance -= move
        count += 1
        if count % 2 == 0:
            move += 1

    print(count)
# 입력
3
0 3
1 5
45 50
# 출력
3
3
4

```
<br>
<br>

#### 원래 풀었던 것.. 오답이래ㅠ  왜지.. 출력 맞는데.. 심지어 위에 코드랑 같음..
```
n = int(input())
def space_move(x, y):
    distance = y - x
    count = 0
    move = 1
    if distance < 4:
        return distance

    while True:
        distance -= move
        count += 1
        if count % 2 == 0:
            move += 1
        if distance < 0:
            break
    return count


for i in range(n):
    x, y = map(int, (input().split()))
    result = space_move(x, y)
    print(result)
    
# 입력
3
0 3
1 5
45 50
# 출력
3
3
4
    
```
