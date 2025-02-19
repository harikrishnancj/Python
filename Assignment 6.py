class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display(self):
        print(f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}")


class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display(self):
        super().display()
        print(f"Required for Major: {'Yes' if self.required_for_major else 'No'}")


class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display(self):
        super().display()
        print(f"Elective Type: {self.elective_type}")



core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course = ElectiveCourse("ART200", "History of Art", 2, "Liberal Arts")


core_course.display()
elective_course.display()

