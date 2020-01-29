# Andrew Sala
# Class1.py

def line():
    print('\n----------------------\n')
import datetime
now = datetime.datetime.now()
class Student:
    def __init__(self, name, age, favSubject,):
        self.name = name
        self.age = age
        self.fav = favSubject
    def greeting(self):
        print('Hello my name is {}, I am {} years old, and my favorite subject is {}'.format(self.name, self.age, self.fav))
    def birthday(self):
        self.age += 1
        print('Happy Birthday! {} is now {} years old.'.format(self.name, self.age))
    def birthYear(self):
        print('{} was born in {}'.format(self.name, now.year - self.age))

student_1 = Student('Zach', 11, 'Lunch',)
student_2 = Student('Murph', 15, 'Computer Science',)
student_3 = Student('Max', 15, 'Spanish',)

student_1.greeting()
student_2.greeting()
student_3.greeting()
line()
student_1.birthday()
student_2.birthday()
student_3.birthday()
line()
student_1.birthYear()
student_2.birthYear()
student_3.birthYear()
