import tkinter as tk
from tkinter import messagebox
import random


dance_moves = [
    "Moonwalk", "Salsa Step", "Robot", "Running Man", "Twist",
    "Cabbage Patch", "Macarena", "Electric Slide", "Charleston",
    "Breakdance", "Dougie", "Tango", "Hip Hop", "Cha Cha", "Waltz","bhangara","slowmotion"
]

user_moves = {}


def assign_dance_move():
    user_name = entry.get().strip()
    if not user_name:
        messagebox.showwarning("Input Error", "Please enter a user name.")
        return

    if user_name in user_moves:
        assigned_move = user_moves[user_name]
        messagebox.showinfo("Dance Move Assigned", f"{user_name} already has the dance move: {assigned_move}")
        return

    if len(user_moves) >= len(dance_moves):
        messagebox.showerror("No Moves Left", "No more dance moves available!")
        return

    available_moves = list(set(dance_moves) - set(user_moves.values()))
    assigned_move = random.choice(available_moves)

    user_moves[user_name] = assigned_move
    messagebox.showinfo("Dance Move Assigned", f"{user_name} has been assigned the dance move: {assigned_move}")


root = tk.Tk()
root.title("Random Dance Move Generator")


tk.Label(root, text="Enter User Name:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

assign_button = tk.Button(root, text="Assign Dance Move", command=assign_dance_move)
assign_button.pack(pady=20)


root.mainloop()
