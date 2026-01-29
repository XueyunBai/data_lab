"""Part 3: Tuples as Records
A tuple is immutable. In databases, 'tuple' can also mean a row/record.
"""

students = [
    (1, "Alice", "GSAS", 32),
    (2, "Bob", "Tandon", 28),
    (3, "Carol", "GSAS", 40)
]
# columns: (id, name, school, credits)

# TODO 1: Print the name for each record
for row in students:
    print (row[1])
# TODO 2: Try to change Bob’s credits directly (observe the error)
#students[1][3]=30
# TODO 3: Create a new tuple for Bob with credits=30 and replace the old record in the list
for i in range(len(students)):
    if students[i][1]=="Bob":
        students[i]=(students[i][0], students[i][1], students[i][2], 30)
print(students)
# Reflection (answer in a comment):
# TODO: Why might immutability be good for data integrity?
#since the data cannot be changed accidently
