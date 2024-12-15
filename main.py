import tkinter as tk
from tkinter import messagebox
import csv

def submitform():
    # Collect user inputs
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    hobby = hobby_var.get()
    favorite_color = color_var.get()
    programming_languages = [lang for lang, var in languages_vars.items() if var.get()]
    bio = bio_text.get("1.0", tk.END).strip()
    import re
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    email = email_entry.get().strip()
    
    if not re.match(email_pattern, email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address")
        return
        
    try:
        age_num = int(age)
        if age_num < 13 or age_num > 120:
            messagebox.showerror("Invalid Age", "Please enter an age between 13 and 120")
            return
    except ValueError:
        messagebox.showerror("Invalid Age", "Age must be a number")
        return


    # Validate inputs
    if not name or not age or not email:
        messagebox.showerror("Input Error", "Please fill out Name, Age, and Email fields.")
        return

    # Save data to CSV
    try:
        with open("responses.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, email, hobby, favorite_color, ', '.join(programming_languages), bio])
    except Exception as e:
        messagebox.showerror("File Error", f"An error occurred while saving data: {e}")
        return

    # Create a summary of inputs
    summary = (
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Email: {email}\n"
        f"Favorite Hobby: {hobby}\n"
        f"Favorite Color: {favorite_color}\n"
        f"Programming Languages: {', '.join(programming_languages) if programming_languages else 'None'}\n"
        f"Bio: {bio}\n"
    )
    
    messagebox.showinfo("Summary", summary)

app = tk.Tk()
app.title("Information Form")
app.geometry("500x600")

tk.Label(app, text="User Information", font=("Arial", 14)).pack(pady=10)
tk.Label(app, text="Name:").pack(anchor="w")
name_entry = tk.Entry(app, width=40)
name_entry.pack()

tk.Label(app, text="Age:").pack(anchor="w")
age_entry = tk.Entry(app, width=40)
age_entry.pack()

tk.Label(app, text="Email:").pack(anchor="w")
email_entry = tk.Entry(app, width=40)
email_entry.pack()

tk.Label(app, text="\nGetting to Know You Quiz", font=("Arial", 14)).pack(pady=10)


tk.Label(app, text="What is your favorite hobby?").pack(anchor="w")
hobby_var = tk.StringVar(value="Reading")
tk.Radiobutton(app, text="Reading", variable=hobby_var, value="Reading").pack(anchor="w")
tk.Radiobutton(app, text="Traveling", variable=hobby_var, value="Traveling").pack(anchor="w")
tk.Radiobutton(app, text="Cooking", variable=hobby_var, value="Cooking").pack(anchor="w")
tk.Radiobutton(app, text="Gaming", variable=hobby_var, value="Gaming").pack(anchor="w")


tk.Label(app, text="What is your favorite color?").pack(anchor="w")
color_var = tk.StringVar(value="Select")
color_dropdown = tk.OptionMenu(app, color_var, "Red", "Blue", "Green", "Yellow", "Purple")
color_dropdown.pack(anchor="w")

tk.Label(app, text="Which programming languages do you know?").pack(anchor="w")
languages_vars = {
    "Python": tk.BooleanVar(),
    "JavaScript": tk.BooleanVar(),
    "C++": tk.BooleanVar(),
    "Java": tk.BooleanVar(),
    "Ruby": tk.BooleanVar()
}
for lang, var in languages_vars.items():
    tk.Checkbutton(app, text=lang, variable=var).pack(anchor="w")


tk.Label(app, text="Tell us a bit about yourself:").pack(anchor="w")
bio_text = tk.Text(app, width=50, height=5)
bio_text.pack()

tk.Button(app, text="Submit", command=submitform, bg="blue", fg="white").pack(pady=20)

try:
    with open("responses.csv", mode="x", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Email", "Hobby", "Favorite Color", "Programming Languages", "Bio"])
except FileExistsError:
    pass                  
app.mainloop()
