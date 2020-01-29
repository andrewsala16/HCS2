# Andrew Sala
# RPS
import random

running = False

#used for spacing
def line():
   print('\n-------------------\n')

#Class to generate cpu move
class Cpu:
   rps = ['Rock', 'Paper', 'Scissors']
   def __init__(self):
       self.rps = Cpu.rps[random.randint(0, len(Cpu.rps)-1)]
       self.flop = Cpu.flop(self)
    #function to represent Cpu's move as a number
   def flop(self):
       if self.rps == 'Rock':
           return 1
       elif self.rps == 'Paper':
           return 2
       elif self.rps == 'Scissors':
           return 3

#Function if you choose rock
def rock(num):
   if num == 1:
       print('\nDraw! The CPU chose Rock')
       playAgain()
   elif num == 2:
       print('\nYou Lost! The CPU chose Paper')
       playAgain()
   elif num == 3:
       print('\nYou Won! The CPU chose Scissors')
       playAgain()

#Function if you choose paper
def paper(num):
   if num == 2:
       print('\nDraw! The CPU chose Paper')
       playAgain()
   elif num == 3:
       print('\nYou Lost! The CPU chose Scissors')
       playAgain()
   elif num == 2:
       print('\nYou Won! The CPU chose Rock')
       playAgain()

#Function if you choose scissors
def scissors(num):
   if num == 3:
       print('\nDraw! The CPU chose Scissors')
       playAgain()
   elif num == 1:
       print('\nYou Lost! The CPU chose Rock')
       playAgain()
   elif num == 2:
       print('\nYou Won! The CPU chose Paper')
       playAgain()

#Function for user to choose to play again
def playAgain():
   global running
   pa = input('Would you like to play again? (yes/no)')
   if(pa == 'yes'):
       line()
       Start()
       return
   elif(pa == 'no'):
       running = False
   else:
       print("\nInvalid input, please state 'yes' or 'no'")
       playAgain()
       return

#Function to initiate the program
def Start():
   global running, cpuMove
   running = True
   userMove = input('Choose Rock, Paper, or Scissors\n')
   while running == True:
       cpuMove = Cpu()
       if userMove.lower() == 'rock':
           rock(cpuMove.flop)
           return
       elif userMove.lower() == 'paper':
           paper(cpuMove.flop)
       elif userMove == 'scissors':
           scissors(cpuMove.flop)
           return
       else:
           print('\nInvalid input, please type Rock, Paper, or Scissors')
           Start()
           return

print('Welcome to Rock Paper Scissors!')
Start()
