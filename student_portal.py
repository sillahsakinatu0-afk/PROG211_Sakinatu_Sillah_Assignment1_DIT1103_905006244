"""
Student Learning Portal
PROG211 - Object-Oriented Programming 1
Domain: Education

Digital Public Goods (DPG) alignment:
- Open-source: intended to be published on GitHub.
- Inclusive: plain-text menu, clear messages, no special hardware needed.
- Privacy-respecting: stores only an auto-generated ID, a display name
  (nickname allowed) and a score. No phone, address or other sensitive data.
- Modular and reusable: each class has one job and can be reused alone.
"""

# Tuple (optional extra marks): fixed grade bands that never change.
GRADE_BANDS = (
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F"),
)


class Course:
    """Represents a course a student is enrolled in."""

    def __init__(self, code, title):
        self.code = code      # attribute
        self.title = title    # attribute

    def display_info(self):
        return f"{self.code} - {self.title}"


class Student:
    """Represents a student in the learning portal."""

    total_students = 0  # class attribute shared by all students

    def __init__(self, student_id, display_name, course, score=0):
        self.student_id = student_id        # unique ID (the dictionary key)
        self.display_name = display_name    # nickname allowed (privacy)
        self.course = course                # a Course object (interaction)
        self.score = score
        Student.total_students += 1

    # ---------- Instance methods ----------
    def update_score(self, new_score):
        """Update this student's score if it is valid."""
        if Student.is_valid_score(new_score):
            self.score = new_score
            return True
        return False

    def get_grade(self):
        """Return the letter grade using the GRADE_BANDS tuple."""
        for minimum, letter in GRADE_BANDS:
            if self.score >= minimum:
                return letter

    def display_info(self):
        print(f"ID     : {self.student_id}")
        print(f"Name   : {self.display_name}")
        print(f"Course : {self.course.display_info()}")
        print(f"Score  : {self.score}  (Grade {self.get_grade()})")
        print("-" * 40)

    # ---------- Class method ----------
    @classmethod
    def get_total_students(cls):
        """Return how many Student objects have been created."""
        return cls.total_students

    # ---------- Static method ----------
    @staticmethod
    def is_valid_score(score):
        """A score must be a number from 0 to 100."""
        return isinstance(score, (int, float)) and 0 <= score <= 100


class StudentPortal:
    """Stores students in ONE data structure: a dictionary (ID -> Student)."""

    def __init__(self):
        self.students = {}   # the single data structure used

    def add_student(self, student):
        """Add a student record. IDs must be unique."""
        if student.student_id in self.students:
            print("Error: that ID already exists.")
            return False
        self.students[student.student_id] = student
        print(f"Added: {student.display_name}")
        return True

    def display_students(self):
        """Display every record in the portal."""
        if not self.students:
            print("No records yet.")
            return
        print("\n===== STUDENT RECORDS =====")
        for student in self.students.values():
            student.display_info()

    def find_student(self, student_id):
        return self.students.get(student_id)


def read_score(prompt):
    """Ask for a score until a valid number is entered."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if Student.is_valid_score(value):
            return value
        print("Score must be between 0 and 100.")


def menu():
    portal = StudentPortal()
    next_id = 1  # IDs are generated, so no personal data is needed

    while True:
        print("\n--- STUDENT LEARNING PORTAL ---")
        print("1. Add student")
        print("2. Display all students")
        print("3. Update a student's score")
        print("4. Show total students")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Display name (nickname allowed): ").strip()
            code = input("Course code (e.g. PROG211): ").strip().upper()
            title = input("Course title: ").strip()
            score = read_score("Score (0-100): ")
            student = Student(f"STU{next_id:03d}", name, Course(code, title), score)
            if portal.add_student(student):
                next_id += 1
        elif choice == "2":
            portal.display_students()
        elif choice == "3":
            student = portal.find_student(input("Student ID (e.g. STU001): ").strip().upper())
            if student:
                student.update_score(read_score("New score (0-100): "))
                print("Score updated.")
            else:
                print("Student not found.")
        elif choice == "4":
            print("Total students:", Student.get_total_students())
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


def demo():
    """Sample run showing object creation and interaction."""
    portal = StudentPortal()
    prog = Course("PROG211", "Object-Oriented Programming 1")

    portal.add_student(Student("STU001", "Aminata", prog, 78))
    portal.add_student(Student("STU002", "Mohamed", prog, 64))

    portal.find_student("STU002").update_score(72)   # instance method
    portal.display_students()
    print("Total students:", Student.get_total_students())  # class method


if __name__ == "__main__":
    print("1. Run demo")
    print("2. Run interactive portal")
    if input("Choose (1/2): ").strip() == "1":
        demo()
    else:
        menu()
