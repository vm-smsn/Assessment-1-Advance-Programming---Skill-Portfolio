'''
Vince Michael J. Samson
ID: 04-24-0147
10/6/2025 - Oct.7,2026
Advance Programming: Excercise 2 - Alexa Tell Me A Joke
'''

import tkinter as tk
import random

class JokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Joke Bot")
        self.root.geometry("500x300")
        
        self.jokes = []
        self.load_jokes()
        self.create_widgets()
        self.show_joke()
    
    def load_jokes(self):
        try:
            with open("randomJokes.txt", "r") as file:
                for line in file:
                    if '?' in line:
                        parts = line.split('?', 1)
                        question = parts[0] + '?'
                        answer = parts[1].strip()
                        self.jokes.append((question, answer))
        except:
            pass
    
    def create_widgets(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(main_frame, text="Joke Bot", font=("Arial", 16, "bold")).pack(pady=10)
        
        joke_frame = tk.Frame(main_frame)
        joke_frame.pack(fill=tk.BOTH, expand=True, pady=15)
        
        self.setup_text = tk.Label(joke_frame, text="", wraplength=450, font=("Arial", 11))
        self.setup_text.pack(pady=5)
        
        self.punchline_text = tk.Label(joke_frame, text="", wraplength=450, font=("Arial", 11, "bold"))
        self.punchline_text.pack(pady=5)
        
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=15)
        
        tk.Button(button_frame, text="Next joke dawggggg", command=self.show_joke, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Quit", command=self.root.destroy, width=8).pack(side=tk.LEFT, padx=5)
    
    def show_joke(self):
        if self.jokes:
            setup, punchline = random.choice(self.jokes)
            self.setup_text.config(text=setup)
            self.punchline_text.config(text=punchline)
        else:
            self.setup_text.config(text="There aint no more jokes bruh")
            self.punchline_text.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = JokeApp(root)
    root.mainloop()
    
    
    
    