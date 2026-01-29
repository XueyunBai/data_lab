"""Part 1: Lists as Tables
Each row is a list: [id, name, school, credits]
Schema is implicit — your code depends on correct indexes.
"""

students = [
    [1, "Alice", "GSAS", 32],
    [2, "Bob", "Tandon", 28],
    [3, "Carol", "GSAS", 40],
    [4, "Dan", "CAS", 18]
]
# columns: [id, name, school, credits]

# TODO 1: Print all student names (one per line)
for i in range (len(students)):
    print(students[i][1])
# TODO 2: Print only the students in GSAS (id and name)
for j in range(len(students)):
    if students[j][2]=="GSAS":
        print(students[j][0], students[j][1], sep=" ")
# TODO 3: Print students with credits > 30 (name and credits)
for z in range(len(students)):
    if students[z][3]>30:
        print(students[z][1], students[z][3], sep=" ")
# TODO 4: Insert a new student row for: id=5, name='Eve', school='CAS', credits=22
students.append([5, "Eve", "CAS", 22])
print(students)
# TODO 5: Update Bob’s credits to 30
for i in range(len(students)):
    if students[i][1]=="Bob":
        students[i][3]=30
print(students)
# Reflection (answer in a comment):
#list is fragil becaus eit use positional index, so if we add a new column, we have to change all existing positions
# TODO: What breaks if we insert a new column at position 2?
#the position 2 will no longer be school

