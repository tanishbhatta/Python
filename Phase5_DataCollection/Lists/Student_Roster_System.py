"""
Requirements:

Create a list of students.
Replace one student with another.
Replace multiple consecutive students at once.
Show the roster before and after changes.
Create a second variable that references the same list.
Mutate the original list again.
Observe what happens to the second variable.
"""
students = ['Aarush', 'Ronaldo', 'Messi', 'Neymar']
students[0] = 'Pele'
students[1:] = 'Messi', 'Aalu', 'Banda'

print(students)
mutation = students

students[1] = 'Aarush'
print(mutation)
