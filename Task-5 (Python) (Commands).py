import os
import tkinter as tk
from tkinter import messagebox, simpledialog

window = tk.Tk()
window.title("Linux and Networking Automation")
window.geometry("500x300")

label = tk.Label(window, text="LINUX AND NETWORKING AUTOMATION\n", font=("Arial", 12))
label.pack()

button_choices = [
    ("Run date", 1),
    ("Run cal", 2),
    ("Check current user", 3),
    ("Add user and set password", 4),
    ("To know about the memory available", 5), 
    ("To Know about CPU", 6), 
    ("To Check any program or service whether its installed or not", 7),
    ("To know Java version", 8), 
    ("To Python Version", 9), 
    ("To know about IPaddress", 10), 
    ("To know about current running Port numbers", 11), 
    ("To install tcpdump", 12), 
    ("To know who is pinging our System", 13), 
    ("To know process ID of any Program", 14), 
    ("To kill process", 15), 
    ("To know about available Hard Disk", 16), 
    ("To List Hard Disk and their Partitions", 17), 
    ("To install httpd service", 18), 
    ("To Start httpd service", 19), 
    ("To install xclip", 20), 
    ("To read data in clipboard", 21), 
    ("To know about repolist", 22), 
    ("To use Binary Calculator", 23), 
    ("To know IP address of a particular Domain", 24), 
    ("To check the applications running in backgroud", 25), 
    ("To run firefox", 26), 
    ("To Exit", 0) 
]

for text, choice in button_choices:
    button = tk.Button(window, text=text, command=lambda choice=choice: handle_click(choice))
    button.pack()

while True:
    X = input()
    if X == "A":
        window.mainloop()
    else:
        break
