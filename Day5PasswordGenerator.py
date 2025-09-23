import random
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letter = int(input("How many letters Would you like in your passwor\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_number = int(input("How many numbers would you like?\n"))

password_list = []
for char in range(0, nr_letter):
  password_list.append(random.choice(letter))

for char in range(0, nr_symbols):
  password_list.append(random.choice(symbols))
  
for char in range(0, nr_number):
  password_list.append(random.choice(number))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = " "
for char in password_list:
  password += char

  print(f"Your password is: {password}")