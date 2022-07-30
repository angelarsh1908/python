from unicodedata import name


class Student:
    def all_student(self):
         student_list=[ ]
         status=True
         while status:
            name=input("Enter student name")
            student_list.append(name)
            choice=input("Do you want add  more item press'y' for yes and press 'n' for no")
            if choice=='n' or choice=='no':
                status=False
s_obj=Student()
s_obj.all_student()

