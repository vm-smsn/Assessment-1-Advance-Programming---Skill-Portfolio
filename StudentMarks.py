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
        '''
        The program starts with metadata and importation of Tkinter modules that are needed to develop a graphical user interface including ttk module used to develop Treeview widgets and the messagebox module used to handle dialogs. The StudentMarksApp class instance is launched into an 800x500 window part, whereby it builds a student list, loads the relevant data and builds the GUI layout entailing a titling element, a tabular display area, a delineated details section and a mix of interactive controls such as an option to list all entries, unveil the highest score, present the lowest score and an exit button that is red in color and located conspicuously.
        '''
        
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
        '''
        The load-students procedure will open the file studentMarks.txt and the first line will be used to identify the number of students as a result of the first line, then all the other lines will be processed individually read and a structured dictionary will be formed in the form of the student identifier, name, three course work assessments with a final examination score. In case the necessary file is not available, the implementation initiates an error notification.
        '''
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
        '''
        The process of populating the table is done via the populate_table() function and computes percentages and grades of each row and assigns the scores in relation to their maximums (e.g. 30/60). The table has an interactive element which triggers selection events when rows are selected.
        '''
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
        '''
        As a row is clicked on a table, onstudentselect only captures. 
        the event, is what decides the index of the chosen student, and calls showstudentdetails. 
        to provide formatted information.
        '''
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            student_index = self.tree.index(item)
            self.show_student_details(student_index)
    
    def show_student_details(self, index):
        '''
        The system provides the structured student data, in the form of names, ID, coursework total, exam score, percentage and grade in a special label below the table thus making individual and personal analysis of the students easy.
        '''
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
    '''
    The standard conditional statement provided above: if __name__ == "__main|: is the cause of the prompting of the instantiation of the Tkinter root window,  
    the creation of the StudentMarksApp object, and the main event loop is launched.  
    Subsequently, this block enables one to have extensive student administration system,  
    a synergistical combination of data processing, graphing and analytical appraisal on a single user interface.
    '''
    root = tk.Tk()
    app = StudentMarksApp(root)
    root.mainloop()

