class person:
    def show_person(self):
         print("this is a person")

class student(person):
     def show_student(self):
         print("this is a student")

class teacher(person):
     def show_teacher(self):
         print("this is a teacher")

class parttimestudent(student, teacher):
     def show_parttime(self):
         print("this is a part_time student")

obj=parttimestudent()
obj.show_person()
obj.show_student()
obj.show_teacher()
obj.show_parttime()