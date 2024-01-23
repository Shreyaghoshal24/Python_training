from students_data import students_list, marks_list

num_students = len(students_list)
for i in range(num_students):
    student = students_list[i]
    print(f"\nStudent {i + 1}: {student['name']}")
    print("Subjects:", ", ".join(student['subjects']))
    
    total_marks = sum(marks_list[i]['marks'])
    print(f"Total Marks: {total_marks}\n")

print("Marks Calculated, Bye!")
    
  
        
