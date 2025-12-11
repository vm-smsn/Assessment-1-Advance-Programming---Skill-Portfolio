'''
Vince Michael J. Samson
ID: 04-24-0147
10/6/2025 - Oct.11,2026
Advance Programming: Exercise 3 - Students Manager
'''

import tkinter as tk
from tkinter import ttk, messagebox

class StudentMarksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marks Manager")
        self.root.geometry("800x500")
        
        self.students = []
        self.load_students()
        
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(main_frame, text="Student Marks System", 
                font=("Arial", 20, "bold")).pack(pady=10)
        
        self.create_student_table(main_frame)
        
        details_frame = tk.Frame(main_frame)
        details_frame.pack(fill=tk.X, pady=10)
        
        self.details_label = tk.Label(details_frame, text="Select a student to view details",
                                     font=("Arial", 12), wraplength=600)
        self.details_label.pack()
        
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Show All Students", command=self.show_all,
                 width=20).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Show Highest Student", command=self.show_highest,
                 width=20).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Show Lowest Student", command=self.show_lowest,
                 width=20).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Exit", command=root.quit,
                 width=20, bg="lightcoral").pack(side=tk.LEFT, padx=5)
    
    def load_students(self):
        try:
            with open("studentMarks.txt", "r") as file:
                num_students = int(file.readline().strip())
                for i in range(num_students):
                    data = file.readline().strip().split(',')
                    student = {
                        'id': data[0],
                        'name': data[1],
                        'marks': [int(data[2]), int(data[3]), int(data[4])],
                        'exam': int(data[5])
                    }
                    self.students.append(student)
        except:
            messagebox.showerror("Error", "Could not load studentMarks.txt file")
    
    def calc_percentage(self, student):
        coursework_total = sum(student['marks'])
        total_marks = coursework_total + student['exam']
        return (total_marks / 160) * 100
    
    def get_grade(self, percentage):
        if percentage >= 70: return 'A'
        elif percentage >= 60: return 'B'
        elif percentage >= 50: return 'C'
        elif percentage >= 40: return 'D'
        else: return 'F'
    
    def create_student_table(self, parent):
        frame = tk.Frame(parent)
        frame.pack(fill=tk.BOTH, expand=True)
        
        v_scroll = tk.Scrollbar(frame)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        h_scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.tree = ttk.Treeview(frame, 
                                columns=("ID", "Name", "Coursework", "Exam", "Overall%", "Grade"),
                                show="headings",
                                yscrollcommand=v_scroll.set,
                                xscrollcommand=h_scroll.set)
        
        columns = [
            ("ID", 80),
            ("Name", 150),
            ("Coursework", 100),
            ("Exam", 80),
            ("Overall%", 100),
            ("Grade", 80)
        ]
        
        for col, width in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        v_scroll.config(command=self.tree.yview)
        h_scroll.config(command=self.tree.xview)
        
        self.tree.bind('<<TreeviewSelect>>', self.on_student_select)
        
        self.populate_table()
    
    def populate_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for student in self.students:
            percentage = self.calc_percentage(student)
            grade = self.get_grade(percentage)
            coursework = sum(student['marks'])
            
            self.tree.insert("", tk.END, values=(
                student['id'],
                student['name'],
                f"{coursework}/60",
                f"{student['exam']}/100",
                f"{percentage:.1f}%",
                grade
            ))
    
    def on_student_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            student_index = self.tree.index(item)
            self.show_student_details(student_index)
    
    def show_student_details(self, index):
        if 0 <= index < len(self.students):
            student = self.students[index]
            percentage = self.calc_percentage(student)
            grade = self.get_grade(percentage)
            coursework = sum(student['marks'])
            
            details = f"""
Name: {student['name']}
ID: {student['id']}
Coursework: {coursework}/60
Exam: {student['exam']}/100
Overall: {percentage:.1f}%
Grade: {grade}
            """
            self.details_label.config(text=details)
    
    def show_all(self):
        self.populate_table()
        messagebox.showinfo("Info", f"Showing all {len(self.students)} students")
    
    def show_highest(self):
        if not self.students:
            messagebox.showwarning("Warning", "No students loaded")
            return
        
        highest = self.students[0]
        for student in self.students:
            if self.calc_percentage(student) > self.calc_percentage(highest):
                highest = student
        
        percentage = self.calc_percentage(highest)
        messagebox.showinfo("Highest Student",
                          f"Name: {highest['name']}\n"
                          f"ID: {highest['id']}\n"
                          f"Overall: {percentage:.1f}%\n"
                          f"Grade: {self.get_grade(percentage)}")
    
    def show_lowest(self):
        if not self.students:
            messagebox.showwarning("Warning", "No students loaded")
            return
        
        lowest = self.students[0]
        for student in self.students:
            if self.calc_percentage(student) < self.calc_percentage(lowest):
                lowest = student
        
        percentage = self.calc_percentage(lowest)
        messagebox.showinfo("Lowest Student",
                          f"Name: {lowest['name']}\n"
                          f"ID: {lowest['id']}\n"
                          f"Overall: {percentage:.1f}%\n"
                          f"Grade: {self.get_grade(percentage)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentMarksApp(root)
    root.mainloop()
