n = int(input())

def avg(students):
    total_students = students[0]
    avg_point = sum(students[1:]) / total_students
    top_students = 0

    for i in students[1:]:
        if i > avg_point:
            top_students +=1

    top_rate = top_students/total_students *100

    return top_rate

for i in range(n):
    students = list(map(int, input().split()))
    x = round(avg(students),3)
    print(f'{x:.3f}%')