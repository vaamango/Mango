import tkinter as t
# import PIL as p
import os
# import sys
import customtkinter as ck
import pandas as pd
import numpy as np

#def btn_clicked():
#    print("Button Clicked")

def signupwindow():
    root1.withdraw()
    os.system('signupwindow.py')
    root1.destroy()

def login(event=None):
    global entry0,entry1,root1,uname,pswd
    uname=entry0.get()
    pswd=entry1.get() 
    logindf=pd.read_csv('user data\\username.csv')
    logindf2=logindf[logindf['Username']==uname] 
    # logindf3=logindf2[logindf2['Password']==pswd] 
    loginlst=logindf2.to_numpy().tolist()
    # print(logindf)
    # print(logindf2)
    # print(loginlst)
    
    # use this to count no. of rows-logindf.count().to_numpy().tolist()

    if  len(loginlst) !=0:
        if str(loginlst[0][1]) == pswd:
            correctdata=t.Label(root1,text='\t\t\t\t\t',fg='red',bg='white',font=('',9))
            correctdata.place(x=89,y=320)
            with open ('user data\\username2.csv','w') as fo:
                pass
            logindf2.to_csv('user data\\username2.csv', mode='w', index=False, header=['Last Username','Last Password'])
            root1.withdraw()
            os.system('homewindownew.py')
            root1.destroy()
            return (uname,pswd)
        else:
            wrongdata=t.Label(root1,text='Incorrect Username or Password',fg='red',bg='white',font=('',9))
            wrongdata.place(x=89,y=320)
    else:
        
        wrongdata=t.Label(root1,text='Incorrect Username or Password',fg='red',bg='white',font=('',9))
        wrongdata.place(x=89,y=320)


root1 = t.Tk()
root1.resizable(False,False)
root1.title('MANGO')
root1.iconbitmap('images\\mangoicon.ico')#ICON
# get the screen dimension
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - 800/ 2)
center_y = int(screen_height/2 -  500/ 2)-40

# set the position of the root1 to the center of the screen
root1.geometry(f'800x500+{center_x}+{center_y}')

#root1.geometry("800x500")
root1.configure(bg = "#ffffff")
canvas = t.Canvas(root1,bg = "#ffffff",height = 500,width = 800,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = t.PhotoImage(file = "images\\loginbackground.png")
background = canvas.create_image(407.0, 250.0,image=background_img)
#entry0 - username , entry1- password
entry0_img = t.PhotoImage(file = "images\\img_textBox0.png")
entry0_bg = canvas.create_image(214.5, 206.0,image = entry0_img)

entry0 = t.Entry(bd = 0,bg = "#ebe9e9",highlightthickness = 0 ,font=('',12))
entry0.bind('<Return>',login)
entry0.place(x = 97.0, y = 186,width = 235.0,height = 38)
hide_image=t.PhotoImage(file='images\\hide.png')
show_image=t.PhotoImage(file='images\\show.png')

def show():
    hide_button=t.Button(root1,image=hide_image,command=hide,activebackground='white',bd=0,background='white',cursor='hand2')
    hide_button.place(x=355,y=279)
    entry1.config(show='')

def hide():
    show_button=t.Button(root1,image=show_image,command=show,activebackground='white',bd=0,background='white',cursor='hand2')
    show_button.place(x=355,y=279)
    entry1.config(show='*')

show_button=t.Button(root1,image=show_image,command=show,activebackground='white',bd=0,background='white',cursor='hand2')
show_button.place(x=355,y=279)

entry1_img =t.PhotoImage(file = "images\\img_textBox1.png")
entry1_bg = canvas.create_image(214.5, 299.0,image = entry1_img)
entry1 = t.Entry(bd = 0,bg = "#ebe9e9",highlightthickness = 0,show="*",font=('',12))
entry1.bind('<Return>',login) #can also use lambda event: login()
entry1.place(x = 97.0, y = 279,width = 235.0,height = 38)

img0 = t.PhotoImage(file = "images\\submitbutton.png")
submitbutton = t.Button(image = img0,borderwidth = 0,highlightthickness = 0,command = login,relief = "flat",cursor='hand2')
submitbutton.place(x = 124, y = 340,width = 167,height = 61)

img1 = t.PhotoImage(file = "images\\signupbutton.png")
signupbutton = t.Button(image = img1,borderwidth = 0,highlightthickness = 0,command = signupwindow,relief = "flat",cursor='hand2')

signupbutton.place(x = 250, y = 418,width = 102,height = 50)
root1.resizable(False, False)
root1.mainloop() 
