class Student:
    def __init__(self, first_name, last_name, age, height, gender, field, national_number, student_number, overall_average):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.gender = gender
        self.field = field
        self.national_number = national_number
        self.student_number = student_number
        self.overall_average = overall_average
        
    def get_first_name(self):
        return ("The first_name: "+ self.first_name)
    def get_age(self):
        return("the"+self.first_name + 's age is ' + str(self.age))
    
student_1 = Student('Amir', 'Rahimi', 23, 175,'Men', 'Control Engineering', 3589432259,9212040709013, 17.33)
student_2 = Student('Ali', 'Bahrami', 24, 165,'Men', 'Civil Engineering', 2197569276,9113345643442, 19.00)
student_3 = Student('Reza', 'Rasooli', 21, 180,'Men', 'Electronic Engineering', 5864503280,24113540709055, 15.86)

print(student_1.get_first_name())
print(student_1.get_age())
print(student_2.get_first_name())
print(student_2.get_age())
print(student_3.get_first_name())
print(student_3.get_age())