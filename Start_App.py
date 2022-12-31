import tkinter as t
from tkinter.ttk import Progressbar
import customtkinter as ck
import sys
import os

root0 = t.Tk()
root0.resizable(0, 0)
image = t.PhotoImage(file='images\\mango2.png')

height = 430
width = 530
x = (root0.winfo_screenwidth()//2)-(width//2)
y = (root0.winfo_screenheight()//2)-(height//2)
root0.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root0.overrideredirect(1)
#root0.wm_attributes('-alpha', 0.9)
root0.wm_attributes('-topmost', True)
root0.config(background='#fd6a36') #,.,fd6a36- for orange color

welcome_label = t.Label(text='WELCOME TO  MANGO', bg='#fd6a36', font=("yu gothic ui", 15, "bold"), fg='black')
welcome_label.place(x=150, y=25)

bg_label = t.Label(root0, image=image, bg='#fd6a36')
bg_label.place(x=130, y=65)

progress_label = t.Label(root0, text="Loading...", font=('yu gothic ui', 13, 'bold'), fg='black', bg='#fd6a36')
progress_label.place(x=190, y=350)
progress = ck.CTkProgressBar(root0, orientation='HORIZONTAL', width=500, mode='determinate',corner_radius=20,height=15,progress_color='#07D8E9',fg_color='#fd6a36',bg_color='#fd6a36')
progress.place(x=15, y=390)

exit_btn = t.Button(text='x', bg='#fd6a36', command=lambda: exit_window(), bd=0, font=("yu gothic ui", 16, "bold"),
activebackground='#fd6a36', fg='black')
exit_btn.place(x=490, y=0)


def exit_window():
    sys.exit(root0.destroy())


def top():
    root0.withdraw()
    os.system("loginwindow.py") #initial code-python AccountSystem.py
    root0.destroy()


i = 0


def load():
    global i
    if i <= 10:
        txt = 'Loading...  ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000, load)
        progress.set(i/10)
        i += 1
    else:
        top()


load()


load()
root0.mainloop()
