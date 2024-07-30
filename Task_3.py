import tkinter as tk
from random import randint

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("500x600")
        self.window.config(bg="#f0f0f0")  # Light gray background

        self.player_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="Rock Paper Scissors", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#00698f")  # Blue text
        self.label.pack(pady=20)

        self.player_label = tk.Label(self.window, text="Player", font=("Helvetica", 18), bg="#f0f0f0", fg="#33cc33")  # Green text
        self.player_label.pack(pady=10)

        self.computer_label = tk.Label(self.window, text="Computer", font=("Helvetica", 18), bg="#f0f0f0", fg="#ff9900")  # Orange text
        self.computer_label.pack(pady=10)

        self.result_label = tk.Label(self.window, text="", font=("Helvetica", 18), bg="#f0f0f0", fg="#00698f")  # Blue text
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.window, text="Score - You: 0, Computer: 0", font=("Helvetica", 18), bg="#f0f0f0", fg="#333")  # Dark gray text
        self.score_label.pack(pady=10)

        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.play("Rock"), bg="#ff69b4", fg="white")  # Pink button
        self.rock_button.pack(pady=10)

        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.play("Paper"), bg="#33cc33", fg="white")  # Green button
        self.paper_button.pack(pady=10)

        self.scissors_button = tk.Button(self.window, text="Scissors", command=lambda: self.play("Scissors"), bg="#00698f", fg="white")  # Blue button
        self.scissors_button.pack(pady=10)

        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset, bg="#ff9900", fg="white")  # Orange button
        self.reset_button.pack(pady=10)

    def play(self, player_choice):
        try:
            computer_choice = self.get_computer_choice()
            result = self.determine_winner(player_choice, computer_choice)
            self.update_labels(player_choice, computer_choice, result)
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_computer_choice(self):
        choices = ["Rock", "Paper", "Scissors"]
        return choices[randint(0, 2)]

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or (player_choice == "Paper" and computer_choice == "Rock") or (player_choice == "Scissors" and computer_choice == "Paper"):
            self.player_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def update_labels(self, player_choice, computer_choice, result):
        self.player_label.config(text=f"Player: {player_choice}")
        self.computer_label.config(text=f"Computer: {computer_choice}")
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score - You: {self.player_score}, Computer: {self.computer_score}")

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_label.config(text="Player")
        self.computer_label.config(text="Computer")
        self.result_label.config(text="")
        self.score_label.config(text="Score - You: 0, Computer: 0")

    def run(self):
        try:
            self.window.mainloop()
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
