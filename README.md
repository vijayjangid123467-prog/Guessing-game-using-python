Number Guessing Game 🎮

A simple Python-based Number Guessing Game where the computer randomly selects a number between 1 and 10, and the player tries to guess it.

📖 Description

This project is a beginner-friendly Python game that demonstrates the use of:

Random number generation
User input
Conditional statements (if, elif, else)
Basic game logic

The program generates a random number between 1 and 10 and asks the user to guess it. Based on the user's input, it provides feedback indicating whether the guess is too high, too low, or correct.

🚀 Features
Generates a random number between 1 and 10
Accepts user input
Provides feedback on the guess
Displays a winning message when the correct number is guessed
🛠️ Technologies Used
Python 3
Random Module
📂 Code
Python
import random
 
number = random.randint(1, 10)
 
print("Welcome to Number Guessing Game")
print("You have to guess the number which I selected")
 
n = int(input("Guess a number: "))
 
print("My number is", number)
 
if n < number:
print("Too low, try again")
elif n > number:
print("Too high, try again")
else:
print("Congratulations!! You won the game")
▶️ How to Run
Install Python 3.
Save the code in a file named guessing_game.py.
Open a terminal or command prompt.
Run the program:
Shell
python guessing_game.py
📸 Sample Output
Plain Text
Welcome to Number Guessing Game
You have to guess the number which I selected
Guess a number: 7
My number is 5
Too high, try again
🎯 Learning Outcomes

By building this project, you will learn:

How to import and use Python modules
How to take input from users
How conditional statements work
Basic game development concepts
