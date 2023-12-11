student_scores = {
    "Harry": 81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

students_grades={}

for key in student_scores:
    marks =student_scores[key]
    if(marks > 90):
        students_grades[key]="Outstanding";
    elif(marks >80):
        students_grades[key]="Exceeda Expectations";
    elif(marks >70):
        students_grades[key]="Acceptable";
    else:
        students_grades[key]="Fail";


for key in students_grades:
    print(key+ " " + students_grades[key])


  
