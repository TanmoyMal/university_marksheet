import tkinter as tk
from tkinter import messagebox

# ---------------------- GUI Setup ----------------------
root = tk.Tk()
root.title("Student Result Management System")
root.geometry("500x650")

subject_entries = []  # List to hold subject and marks entry widgets

# ---------------------- Add Subject Function ----------------------
def add_subject_row():
    frame = tk.Frame(subject_frame)
    frame.pack(pady=2)

    sub_entry = tk.Entry(frame, width=20)
    sub_entry.pack(side=tk.LEFT, padx=5)
    sub_entry.insert(0, f"Subject {len(subject_entries) + 1}")

    marks_entry = tk.Entry(frame, width=10)
    marks_entry.pack(side=tk.LEFT, padx=5)

    outof_entry = tk.Entry(frame, width=10)
    outof_entry.pack(side=tk.LEFT, padx=5)
    outof_entry.insert(0, "100")

    subject_entries.append((sub_entry, marks_entry, outof_entry))

# ---------------------- Calculate Result Function ----------------------
def calculate_result():
    name = name_entry.get().strip()
    roll = roll_entry.get().strip()

    if not name or not roll:
        messagebox.showerror("Input Error", "Please enter student name and roll number.")
        return

    subjects = {}
    total_obtained = 0
    total_possible = 0
    failed_subjects = []

    for sub_entry, marks_entry, outof_entry in subject_entries:
        subject = sub_entry.get().strip()
        marks = marks_entry.get().strip()
        outof = outof_entry.get().strip()

        if not subject or not marks or not outof:
            messagebox.showerror("Input Error", "Please fill all subject names, marks, and out-of values.")
            return

        try:
            marks = float(marks)
            outof = float(outof)
        except ValueError:
            messagebox.showerror("Input Error", f"Invalid marks or out-of for subject '{subject}'.")
            return

        subjects[subject] = (marks, outof)
        total_obtained += marks
        total_possible += outof

        if marks < (0.33 * outof):
            failed_subjects.append(subject)

    percentage = (total_obtained / total_possible) * 100
    overall_result = "FAIL" if failed_subjects else "PASS"

    # Display result
    output = f"Student Name: {name}\nRoll Number: {roll}\n"
    output += f"Total Subjects: {len(subjects)}\n"
    output += f"Total Marks: {total_obtained:.2f} / {total_possible}\n"
    output += f"Percentage: {percentage:.2f}%\n\n"
    output += "Subject-wise Result:\n"

    for sub, (mark, outof) in subjects.items():
        status = "PASS" if mark >= (0.33 * outof) else "FAIL"
        output += f"{sub}: {mark}/{outof} - {status}\n"

    output += f"\nOverall Result: {overall_result}"

    result_label.config(text=output)

# ---------------------- GUI Layout ----------------------
tk.Label(root, text="Student Name:").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Roll Number:").pack(pady=5)
roll_entry = tk.Entry(root, width=30)
roll_entry.pack(pady=5)

subject_frame = tk.Frame(root)
subject_frame.pack(pady=10)

header_frame = tk.Frame(subject_frame)
header_frame.pack()
tk.Label(header_frame, text="Subject", width=20).pack(side=tk.LEFT, padx=5)
tk.Label(header_frame, text="Marks", width=10).pack(side=tk.LEFT, padx=5)
tk.Label(header_frame, text="Out Of", width=10).pack(side=tk.LEFT, padx=5)

add_subject_row()  # Add first subject row by default

add_btn = tk.Button(root, text="+ Add Subject", command=add_subject_row)
add_btn.pack(pady=5)

calc_btn = tk.Button(root, text="Calculate Result", command=calculate_result)
calc_btn.pack(pady=10)

result_label = tk.Label(root, text="", justify="left", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
