Student1 = {
    "Maths": 98,
    "Sost": 99,
    "Science": 96,
    "student_name": "Tanmay"
}
Student2 = {
    "Maths": 99,
    "Sost": 98,
    "Science": 10,
    "student_name": "Dhiraj"
}
Student3 = {
    "Maths": 10,
    "Sost": 90,
    "Science": 93,
    "student_name": "Suraj"
}

studentsList = [Student1,Student2,Student3]
HighMathMarks = []
HighSostMarks = []
HighSciMarks = []
mname=''
soname=''
scname = ''
mscore = 0
Sost = 0
Science = 0
for student in studentsList:
        math_marks = student['Maths']
        Sost_marks = student['Sost']
        Science_marks = student['Science']
        if (math_marks > mscore):
            mscore =  math_marks
            mname = student['student_name']
            HighMathMarks.append(mscore)
        if Sost_marks > Sost:
            Sost = Sost_marks
            soname = student['student_name']
            HighSostMarks.append(Sost)
        if Science_marks > Science:
            Science = Science_marks
            scname = student['student_name']
            HighSciMarks.append(Science)
           # print(HighSostMarks)



print(f"Highest Maths Marks Obtained:",mname,max(HighMathMarks))
print(f"Highest Sost Marks Obtained:",soname,max(HighSostMarks))
print(f"Highest Science Marks Obtained:",scname,max(HighSciMarks))







