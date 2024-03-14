import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.password_var = tk.StringVar()
        self.password_label = tk.Label(root, textvariable=self.password_var, font=('New Times Roman', 14), wraplength=300)
        self.password_label.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", font=('New Times Roman', 12), command=self.generate_password)
        self.generate_button.pack(pady=5)

        self.copy_button = tk.Button(root, text="Copy to Clipboard", font=('New Times Roman', 12), command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)

    def generate_password(self):
        length = 12  # Change the length of the generated password here
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_var.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
