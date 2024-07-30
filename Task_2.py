import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(fg="green")  # Change text color to green

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Success", "Password copied to clipboard.")
    copy_button.config(bg="green", fg="white")  # Change button color to green
    root.after(1000, lambda: copy_button.config(bg="SystemButtonFace", fg="black"))  # Reset button color after 1 second

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter password length:", font=("Arial", 12, "bold"))
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=20, font=("Arial", 12))
length_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=lambda: generate_password(int(length_entry.get())), font=("Arial", 12, "bold"), bg="blue", fg="white")
generate_button.pack(pady=10)

password_entry = tk.Entry(root, width=40, font=("Arial", 12))
password_entry.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_password, font=("Arial", 12, "bold"), bg="SystemButtonFace", fg="black")
copy_button.pack(pady=10)

root.mainloop()
