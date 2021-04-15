
## 1. 점수 합격/불합격 출력
```
students = [88,30,61,55,95]
i = 1
# 1번 학생은 88점으로 합격입니다.
for student in students:
    if (student > 60):
        print(f'{i}번 학생은 {student}점으로 합격입니다.')
    else:
        print(f'{i}번 학생은 {student}점으로 불합격입니다.')
    i +=1
```

## 2. 숫자 출력하기

### (1) 범위 내 모든 숫자 출력
```
for a in range(1,101):
     print(a)
```
### (2) 짝수 출력하기
```
for a in range(1,101):
    if a % 2 ==0:
     print(a,end=' ')
```
### (3) 홀수 출력하기
```
x = []
for a in range(1,101):
    if a % 2 !=0:
        x.append(str(a))
print(', '.join(x))
```
### (4) 3배수의 합 구하기
```
x = 0
for a in range(1,101):
    if a % 3 ==0:
        x += a
print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {x}')
```
### (5) 혈액형 갯수 count하기
```
bloodtype = ['A','A','A','O','B','B','O','AB','AB','O']
student = {'A':0,'O':0,'B':0,'AB':0}
countA=0
countB=0
countO=0
countAB=0

for a in bloodtype:
    if a == 'A':
        countA += 1
        student['A']=countA
    elif a == 'B':
        countB += 1
        student['B']=countB
    elif a == 'O':
        countO += 1
        student['O']=countO
    elif a == 'AB':
        countAB += 1
        student['AB']=countAB

print (student)
```
### (6) 80점 이상인 점수의 합
### .pop(x) : x번째 요소를 꺼내고 그 요소는 삭제한다.
```
students =[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
students.sort()
i= 0
sum = 0
while i<len(students):
    if students[i] >= 80:
        sum +=students.pop(i)
        i-= 1
    i +=1
print(sum)
```
## 3. 별찍기
### (1)별찍기
```
*****
****
***
**
*
```
```
star = '*'
for i in range(5,0,-1):
    print(star * i)
```    
### (2)별찍기
```
******* 
 *****
  *** 
   * 
```
```
star = '*'
i , k = 4 ,0
while i > 0:
    print ('{0}{1}'.format(' ' * k, star * (2*i-1)))
    k+=1
    i-=1
```    
### (3)별찍기
```
    *
   **
  ***
 ****
*****
```
```
k = 4
star = '*'
for i in range(1,6):
    print('{0}{1}'.format(' '*k,star*i))
    k-= 1
```

## 4. 입력된 숫자의 갯수 세기
```
b=[]
num = list(map(int, str(input())))
for a in range(10):
    print(a, end=' ')
print()
for a in range(10):
    count = num.count(a)
    b.append(str(count))

print(' '.join(b))
```
