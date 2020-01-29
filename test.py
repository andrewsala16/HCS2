
from Class2 import Car
def line():
    print('\n----------------------\n')
#student_1 = Student('Zach', 11, 'Lunch',)

#student_1.greeting()

car_1 = Car(2006, 'Honda', 'Fit',)
car_2 = Car(2020, 'Dodge', 'Charger',)
car_3 = Car(1999, 'Jeep', 'Wrangler',)

car_1.honk()
line()
car_1.registration()
car_2.registration()
car_3.registration()
line()
car_1.drive(55)
car_2.drive(93)
car_3.drive(666)
line()
car_1.gas()


