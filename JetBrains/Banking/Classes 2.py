class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = name[0] + last_name + birth_year


user_input_name = input()
user_input_last_name = input()
user_input_birth_year = input()

student = Student(user_input_name, user_input_last_name, user_input_birth_year)
print(student.student_id)
