def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Define a Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test the function with a list of Student objects
if __name__ == "__main__":
    students = [
        Student("Alice", "A001", 3.8),
        Student("Bob", "A002", 3.6),
        Student("Charlie", "A003", 3.9),
        Student("David", "A004", 3.7)
    ]

    sorted_students = sort_students(students)

    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
