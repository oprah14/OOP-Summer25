class Student:
    def hello(self):
        print("Hello! I am a student.")
student_instance = Student()
student_instance.hello()

class Student:
    def _init_(self, name, index_number):
        self.name = name
        self.index_number = index_number

    def hello(self):
        print(f"Hello, I am {self.name}, my index number is {self.index_number}")


student1 = Student("Ibrahim Levent", "35389")
student1.hello()