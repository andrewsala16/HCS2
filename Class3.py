#Andrew Sala
#class3

def line():
    print('\n----------------------\n')

class Robot:
    population = 0
    robot_list = []
    def __init__(self, name):
        Robot.robot_list.append(name)
        self.name = name
        self.power = 100
        Robot.population += 1
        robot_num = Robot.population
        print('Robot {} number {}'.format(name, robot_num))
    def charge_robot(self):
        if (self.power == 100):
            print('Battery full')
        elif (self.power < 75):
            self.power += 25
        elif (self.power >= 75):
            self.power = 100
        print('{} now has {}% battery'.format(self.name, self.power))
    def is_robot_alive(self):
        if (self.power >= 75):
            print('Your robot {} has {}% battery.'.format(self.name, self.power))
        elif (self.power >= 25):
            print('Your robot {} has {}% battery, charge up soon!'.format(self.name, self.power))
        elif (self.power >= 1):
            print('Your robot {} has {}% battery, charge your robot!'.format(self.name, self.power))
        elif (self.power == 0):
            print('{} is dead! Charge up!'.format(self.name))
    def check_battery(self):
        print('{} has {}% battery'.format(self.name, self.power))
    def do_robot_things(self, action):
        print('{}:'.format(self.name, end=''))
        for i in range(1,11):
            print('{}'.format(action.upper()), end=' ')
        print()
        self.power -= 10
        self.is_robot_alive()
    def robot_roll_call(self):
        for i in range (len(Robot.robot_list)):
            if (i < len(Robot.robot_list)-1):
                print(Robot.robot_list[i], end=', ')
            else:
                print(Robot.robot_list[i])
robo1 = Robot('Mark Zuck')
robo2 = Robot('Patch')
robo3 = Robot('Yhandi')
robo4 = Robot('Will Smith')
robo5 = Robot('Cap')

robo1.do_robot_things('Talk')

