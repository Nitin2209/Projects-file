# import random
# word_list = ["aardvark", "baboon", "camel"]

# lives = 6

# chosen_word = random.choice(word_list)
# print(chosen_word)


# placeholder = ""
# word_lanth = len(chosen_word)
# for space in range(word_lanth):
#   placeholder += "_"
# print(placeholder)

# game_over = False
# correct_letter = []

# while not game_over:
  
#     guess = input("Guess a letter: ").lower()

#     display = ""
#     for letter in chosen_word:

#        if letter == guess:
#           display += letter
#           correct_letter.append(guess)
#        elif letter in correct_letter:
#           display += letter
            
#        else:
#           display += "_"

#     print(display)  

#     if guess not in chosen_word:
#        lives -= 1
#        if lives == 0 :
#          game_over = True
#          print ("You Loose!")
      
      
#     if "_" not in display:
#      game_over = True
#      print("You Win!")
   
import tkinter as tk
import random

# Word list
word_list = ["aardvark", "baboon", "camel"]

# Hangman stages (ASCII as text in GUI)
stages = [
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """
]

# Initialize game
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_"] * word_length
lives = len(stages) - 1
correct_letters = []

# Functions
def guess_letter():
    global lives
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if not guess or len(guess) != 1 or not guess.isalpha():
        result_label.config(text="Enter a single letter!")
        return

    new_display = ""
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
        new_display = "".join(display)

    word_label.config(text=" ".join(display))

    if guess not in chosen_word:
        lives -= 1
        result_label.config(text=f"Wrong! {lives} lives left")
        hangman_label.config(text=stages[lives])

        if lives == 0:
            result_label.config(text=f"You lose! Word was '{chosen_word}'")
            entry.config(state="disabled")
            button.config(state="disabled")
    else:
        result_label.config(text="Good guess!")

    if "_" not in display:
        result_label.config(text=" You Win!")
        entry.config(state="disabled")
        button.config(state="disabled")


# Tkinter window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("500x500")

word_label = tk.Label(root, text=" ".join(display), font=("Arial", 24))
word_label.pack(pady=20)

hangman_label = tk.Label(root, text=stages[lives], font=("Courier", 14))
hangman_label.pack()

entry = tk.Entry(root, font=("Arial", 18), width=5, justify="center")
entry.pack(pady=10)

button = tk.Button(root, text="Guess", font=("Arial", 16), command=guess_letter)
button.pack()

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=20)

root.mainloop()

