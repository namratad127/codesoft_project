import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x300") 
        
        self.user_score = 0
        self.computer_score = 0
        
        self.user_choice_label = tk.Label(root, text="Your Choice:", font=("Helvetica", 20))
        self.user_choice_label.pack()
        
        self.user_choice = tk.StringVar()
        self.user_choice.set("rock")
        
        
        self.user_choice_radio = tk.Radiobutton(root, text="Rock", variable=self.user_choice, value="rock", font=("Helvetica", 16))
        self.user_choice_radio.pack()
        self.user_choice_radio = tk.Radiobutton(root, text="Paper", variable=self.user_choice, value="paper", font=("Helvetica", 16))
        self.user_choice_radio.pack()
        self.user_choice_radio = tk.Radiobutton(root, text="Scissors", variable=self.user_choice, value="scissors", font=("Helvetica", 16))
        self.user_choice_radio.pack()
        
        self.play_button = tk.Button(root, text="Play", command=self.play, font=("Helvetica", 16))
        self.play_button.pack()
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))  
        self.result_label.pack()
        
        self.score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Helvetica", 16))
        self.score_label.pack()
        
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset, font=("Helvetica", 16))
        self.play_again_button.pack()
        self.play_again_button.config(state=tk.DISABLED)
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!", "blue"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            self.user_score += 1
            return "You win!", "green"
        else:
            self.computer_score += 1
            return "Computer wins!", "red"
    
    def play(self):
        user_choice = self.user_choice.get()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        result, color = self.determine_winner(user_choice, computer_choice)
        
        self.result_label.config(text=result, fg=color) 
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")
        self.play_again_button.config(state=tk.NORMAL)
    
    def reset(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Your Score: 0 | Computer Score: 0", font=("Helvetica", 16))
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
