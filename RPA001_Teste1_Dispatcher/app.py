import tkinter
from tkinter import messagebox

# Hide the main Tkinter window
root = tkinter.Tk()
root.withdraw()

# Show an informational message box
messagebox.showinfo("Important Msg", "Hello from Python!")