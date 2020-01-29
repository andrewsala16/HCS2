#Andrew Sala
#class2
def line():
    print('\n----------------------\n')

class Car:
    def __init__(self, year, make, model,):
        self.year = year
        self.make = make
        self.model = model
        self.odo_miles = 0
        self.gas_miles = 500
    def honk(self):
        print("Beeeeeep")
    def registration(self):
        print('{} {} {} with {} miles.'.format(self.year, self.make, self.model, self.odo_miles))
    def drive(self, milesDriven):
        if (milesDriven > -1):
            if (self.gas_miles == 0):
                print('The {} {} has no gas! Fill it up'.format(self.make, self.model))
            elif (self.gas_miles > milesDriven and milesDriven <= 500):
                self.odo_miles += milesDriven
                self.gas_miles -= milesDriven
                print('The {} {} has driven {} miles'.format(self.make, self.model, milesDriven))
                print('The {} {} now has {} gas miles\n'.format(self.make, self.model, self.gas_miles))
            else:
                self.odo_miles += self.gas_miles
                print('The {} {} drove {} miles, but ran out of gas! Fill it up'.format(self.make, self.model, self.gas_miles))
        else:
            print('Sorry! We cannot drive backwards')
    def gas(self):
        self.gas_miles = 500
        print('The {} {} is back to {} gas miles'.format(self.make, self.model, self.gas_miles))

