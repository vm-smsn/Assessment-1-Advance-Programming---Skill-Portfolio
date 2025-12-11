'''
Vince Michael J. Samson
ID: 04-24-0147
10/6/2025 - Oct.7,2026
Advance Programming: Exercise 1 - Maths Quiz
'''

import tkinter as tk
from tkinter import messagebox
import random

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        self.root.geometry("400x500")
        
        self.score = 0
        self.question_num = 0
        self.total_questions = 10
        
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(main_frame, text="Math Quiz", font=("Arial", 24, "bold")).pack(pady=10)
        
        tk.Label(main_frame, text="Select Difficulty:", font=("Arial", 12)).pack(pady=10)
        
        self.difficulty_var = tk.IntVar(value=1)
        
        tk.Radiobutton(main_frame, text="Easy (1-digit)", variable=self.difficulty_var, value=1).pack()
        tk.Radiobutton(main_frame, text="Moderate (2-digit)", variable=self.difficulty_var, value=2).pack()
        tk.Radiobutton(main_frame, text="Advanced (4-digit)", variable=self.difficulty_var, value=3).pack()
        
        tk.Button(main_frame, text="Start Quiz", command=self.start_quiz, 
                 font=("Arial", 12), bg="lightblue").pack(pady=20)
        
        self.question_label = tk.Label(main_frame, text="", font=("Arial", 18, "bold"))
        self.question_label.pack(pady=20)
        
        tk.Label(main_frame, text="Your Answer:").pack()
        self.answer_entry = tk.Entry(main_frame, font=("Arial", 14), width=10)
        self.answer_entry.pack(pady=10)
        
        self.submit_btn = tk.Button(main_frame, text="Submit", command=self.check_answer,
                                   font=("Arial", 12), bg="lightgreen", state=tk.DISABLED)
        self.submit_btn.pack(pady=10)
        
        self.score_label = tk.Label(main_frame, text="Score: 0/100", font=("Arial", 12))
        self.score_label.pack(pady=10)
        
        self.next_btn = tk.Button(main_frame, text="Next Question", command=self.next_question,
                                 font=("Arial", 12), bg="lightyellow", state=tk.DISABLED)
        self.next_btn.pack(pady=10)
        
        tk.Button(main_frame, text="Restart", command=self.restart_quiz,
                 font=("Arial", 10)).pack(pady=20)
    
    def start_quiz(self):
        self.score = 0
        self.question_num = 0
        self.score_label.config(text="Score: 0/100")
        self.submit_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.NORMAL)
        self.generate_question()
    
    def generate_question(self):
        level = self.difficulty_var.get()
        ranges = {1: (0, 9), 2: (10, 99), 3: (1000, 9999)}
        
        a = random.randint(*ranges[level])
        b = random.randint(*ranges[level])
        op = random.choice(['+', '-'])
        
        if op == '-' and a < b:
            a, b = b, a
        
        self.current_correct = a + b if op == '+' else a - b
        self.question_label.config(text=f"{a} {op} {b} = ?")
        self.answer_entry.delete(0, tk.END)
        self.question_num += 1
    
    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.current_correct:
                self.score += 10
                messagebox.showinfo("Correct!", "Ang Galing?!!!")
            else:
                messagebox.showinfo("Wrong", f"Correct answer: {self.current_correct}")
            
            self.score_label.config(text=f"Score: {self.score}/100")
            
            if self.question_num >= self.total_questions:
                self.end_quiz()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
    
    def next_question(self):
        if self.question_num < self.total_questions:
            self.generate_question()
        else:
            self.end_quiz()
    
    def end_quiz(self):
        if self.score >= 90: grade = "A+"
        elif self.score >= 80: grade = "A"
        elif self.score >= 70: grade = "B"
        elif self.score >= 60: grade = "C"
        elif self.score >= 50: grade = "D"
        else: grade = "F"
        
        messagebox.showinfo("Quiz Complete!", 
                          f"Final Score: {self.score}/100\nGrade: {grade}")
        
        self.submit_btn.config(state=tk.DISABLED)
        self.next_btn.config(state=tk.DISABLED)
    
    def restart_quiz(self):
        self.start_quiz()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()

