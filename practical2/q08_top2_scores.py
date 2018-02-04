students = []
scores = []
another = "y"
def enter():
    student = str(input("enter name of student: "))
    score = int(input("enter score of student: "))
    another = input("add another student? (y/n) ")
    students.append(student)
    scores.append(score)
    if another == "y":
        enter()
enter()
sort = sorted(range(len(scores)), key=lambda i: scores[i])[-2:]
for i in sort:
    print (students[i])
