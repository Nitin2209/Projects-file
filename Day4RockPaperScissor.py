import random
Rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     '''
Paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|     '''
Scissor ='''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
'''

game_images = ["Rock", "Paper", "Scissor"]

userinput = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissor.\n"))
if userinput >= 0 and userinput <=2:
 print (game_images[userinput])
computer = random.randint(0, 2)
print("Computer chose")
print(game_images[computer]) 

if userinput < 0 and userinput >=3:
 print("invalid choice")
elif userinput == computer:
 print("Drow or no one win or no one lose")
elif userinput == 0 and computer == 2:
 print("You Win!")
elif computer == 0 and userinput == 2:
 print("You lose!")
elif computer > userinput:
 print("You lose!")
elif userinput > computer:
 print("You Win!")

















