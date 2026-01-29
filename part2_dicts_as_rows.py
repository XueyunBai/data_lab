"""Part 2: Dictionaries as Rows
Each row is a dict: {"id": ..., "name": ..., ...}
Schema becomes explicit and safer to access.
"""

students = [
    {"id": 1, "name": "Alice", "school": "GSAS", "credits": 32},
    {"id": 2, "name": "Bob", "school": "Tandon", "credits": 28},
    {"id": 3, "name": "Carol", "school": "GSAS", "credits": 40},
    {"id": 4, "name": "Dan", "school": "CAS", "credits": 18}
]

# TODO 1: Print all student names

# TODO 2: Print only GSAS students (name + credits)

# TODO 3: Add a new field to each row:
#   status='full-time' if credits >= 30 else 'part-time'

# TODO 4: Update Bob’s credits to 30 AND ensure his status updates correctly

def get_students_by_school(rows, school):
    """Return a list of rows where row['school'] == school."""
    # TODO 5: implement
    return []

# TODO 6: Call get_students_by_school(students, "GSAS") and print results

# Reflection (answer in a comment):
# TODO: Why is dict-based code safer than index-based list code?
