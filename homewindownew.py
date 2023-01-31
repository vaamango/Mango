import tkinter as t
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
import os
import customtkinter as ck      
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style as sty
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
import datetime as dt




#DEFINE ALL THE FUNCNS AT THE END OF PROGRAM OR AT THE START OF THE PROGRAM
#use alt for multiple cursors. ctrl+shift+l- to select the same words
root3=ck.CTk()
height = 630
width = 1100
x = (root3.winfo_screenwidth()//2)-(width//2)+30   #we are not getting centre pos of window with normal valuesdue to customtkinter module
y = (root3.winfo_screenheight()//2)-(height//2)-30
root3.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root3.resizable(False,False)
ck.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ck.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
root3.title('MANGO')
root3.iconbitmap('images\\mangoicon.ico')#ICON
unamedf=pd.read_csv('user data\\username2.csv')
unamelst=unamedf.to_numpy().tolist()
uname=unamelst[0][0] + '-'
# print(unamelst,len(uname))
try:
    pd.read_csv('user data\\'+uname+'Inventory(2).csv')
    pd.read_csv('user data\\'+uname+'Stock_Entry.csv')
    pd.read_csv('user data\\'+uname+'Cost.csv')
    pd.read_csv('user data\\'+uname+'sales().csv')
    # print('try')
except:
    inventorydf1=pd.DataFrame(columns=['Item_Code','Item_Name','In_Stock'])
    stockdf2=pd.DataFrame(columns=['Item_Code','Item_Name','Quantity Bought','Date_SE','SE_no.'])
    costdf3=pd.DataFrame(columns=['Item_Code','Item_Name','Cost Price','Selling Price'])
    salesdf4=pd.DataFrame(columns=['Date','Item_Code','Item_Name','Quantity','Sales_no.','Profit'])
    inventorydf1.to_csv('user data\\'+uname+'Inventory(2).csv',index=False,header=True)
    stockdf2.to_csv('user data\\'+uname+'Stock_Entry.csv',index=False,header=True)
    costdf3.to_csv('user data\\'+uname+'Cost.csv',index=False,header=True)
    salesdf4.to_csv('user data\\'+uname+'sales().csv',index=False,header=True)
    # print('except')
#IMAGES----------------------------------------------------------------------------------------------------------------------------------
mangoimg=ck.CTkImage(dark_image=Image.open(r"images\\vmango2.png"),size=(45,45))
mangoimg2=ck.CTkImage(dark_image=Image.open(r"images\\vmango2.png"),size=(400,400))
accountimg=ck.CTkImage(dark_image=Image.open(r'images\\account.png'),size=(45,45))
stockimg=ck.CTkImage(dark_image=Image.open(r'images\\stock entry.png'),size=(50,50))
billimg=ck.CTkImage(dark_image=Image.open(r'images\\rupees-bill.png'),size=(50,50))
salesimg=ck.CTkImage(dark_image=Image.open(r'images\\sales.png'),size=(50,50))
inventoryimg=ck.CTkImage(dark_image=Image.open(r'images\\inventory.png'),size=(50,50))
notepadimg=ck.CTkImage(dark_image=Image.open(r'images\\notepad.png'),size=(60,60))
rupeeimg=ck.CTkImage(dark_image=Image.open(r'images\\rs.png'),size=(40,40))
rupeeimg2=ck.CTkImage(dark_image=Image.open(r'images\\rs.png'),size=(60,60))
backimg=ck.CTkImage(dark_image=Image.open(r'images\\back.png'),size=(40,40))
inventorynoteimg=ck.CTkImage(dark_image=Image.open(r'images\\inventorynote.png'),size=(60,60))
salesrsimg=ck.CTkImage(dark_image=Image.open(r'images\\salesrs.png'),size=(60,60))
billingimg=ck.CTkImage(dark_image=Image.open(r'images\\billing.png'),size=(60,60))
searchimg=ck.CTkImage(dark_image=Image.open(r'images\\search.png'),size=(40,40))
vijayimg=ck.CTkImage(dark_image=Image.open(r'images\\vijay png 2.png'),size=(230,230))
abhinavimg=ck.CTkImage(dark_image=Image.open(r'images\\abhinav png.png'),size=(230,230))
aniketimg=ck.CTkImage(dark_image=Image.open(r'images\\aniket png.png'),size=(230,230))
# FUNCNS ---------------------------------------------------------------------------------------------------------------------------------

def change_appearance_mode( new_appearance_mode):
        ck.set_appearance_mode(new_appearance_mode)
def btn_clicked():
    print('BUTTON CLICKED')

def exitt():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root3)
    if sure == True:
        root3.withdraw()
        root3.destroy()



#HOME-----------------------------------------------------------------------------------------------------------------------------------
def home():
    global root3
    frame1=ck.CTkFrame(master=root3,width=1100,height=55,corner_radius=0,fg_color='#282927')
    frame1.grid(row=0,column=0) #REMEMBER RELATIVITY
    frame2=ck.CTkFrame(master=root3,width=1100,height=575,corner_radius=0)
    frame2.grid(row=1,column=0)
    
    # rlbl=ck.CTkLabel(master=frame2,text='HOME PAGE')
    # rlbl.place(x=0,y=0)
    
    lbl1=ck.CTkLabel(frame1,image=mangoimg,text='')
    lbl1.place(x=10,y=5)
    lbl2=ck.CTkLabel(frame1,image=accountimg,text='')
    lbl2.place(x=1040,y=5)
#frame1=====================
    homelbl = ck.CTkLabel(master=frame1,text='HOME',height=55,width=80,corner_radius=10,fg_color='green',text_color='white')
    homelbl.place(x=60,y=0)

    managebutton=ck.CTkButton(master=frame1,text='MANAGE',height=55,width=80,corner_radius=10,command = manage,cursor='hand2',fg_color='#282927',text_color='white')
    managebutton.place(x=140,y=0)

    analysebutton=ck.CTkButton(master=frame1,text='ANALYSE',height=55,width=80,corner_radius=10,command = analyse,cursor='hand2',fg_color='#282927',text_color='white')
    analysebutton.place(x=220,y=0)

    #settingsbutton=ck.CTkButton(master=frame1,text='SETTINGS',height=55,width=80,corner_radius=10,command = settings,cursor='hand2',fg_color='#282927',text_color='white')
    #settingsbutton.place(x=300,y=0)

    aboutbutton=ck.CTkButton(master=frame1,text='ABOUT',height=55,width=80,corner_radius=10,command = about,cursor='hand2',fg_color='#282927',text_color='white')
    aboutbutton.place(x=300,y=0)

#frame2======================
    welcomelbl=ck.CTkLabel(master=frame2,text='Welcome To',font=('Times New Roman',70),text_color='silver')
    welcomelbl.place(x=300,y=30)
    mangolbl=ck.CTkLabel(master=frame2,text='Mango',font=('Times New Roman',70),text_color='yellow')
    mangolbl.place(x=680,y=30)
    homeimglbl=ck.CTkLabel(master=frame2,text='',image=mangoimg2)
    homeimglbl.place(x=70,y=100)
    inventorylbl=ck.CTkLabel(master=frame2,text='''Inventory Management
and
Data Analytics Software''',font=('Times New Roman',60),text_color='silver')
    inventorylbl.place(x=500,y=240)
#MANAGE------------------------------------------------------------------------------------------------------------------------------
def manage():
    inventory()
#ANALYSE-----------------------------------------------------------------------------------------------------------------------------
def analyse():
    global root3 ,itemname,fromanalyseentry1,toanalyseentry1,fromanalyseentry2,toanalyseentry2, analyseframe4
    frame1=ck.CTkFrame(master=root3,width=1100,height=55,corner_radius=0,fg_color='#282927')
    frame1.grid(row=0,column=0) #REMEMBER RELATIVITY
    frame2=ck.CTkFrame(master=root3,width=1100,height=575,corner_radius=0)
    frame2.grid(row=1,column=0)
    frame3=ck.CTkFrame(master=frame2,width=370,height=555,corner_radius=20) # agar corners rounded chahiye then use master= frame2
    frame3.place(x=10,y=15)
    analyseframe4=ck.CTkFrame(master=frame2, width=700,height=555,corner_radius=20)
    analyseframe4.place(x=390,y=15)


    
    # rlbl=ck.CTkLabel(master=frame2,text='ANALYSE PAGE')
    # rlbl.place(x=0,y=0)
    lbl1=ck.CTkLabel(frame1,image=mangoimg,text='')
    lbl1.place(x=10,y=5)
    lbl2=ck.CTkLabel(frame1,image=accountimg,text='')
    lbl2.place(x=1040,y=5)

#FRAME 1 BUTTONS==========================

    homebutton = ck.CTkButton(master=frame1,text='HOME',height=55,width=80,corner_radius=10,command = home,cursor='hand2',fg_color='#282927',text_color='white')
    homebutton.place(x=60,y=0)

    managebutton=ck.CTkButton(master=frame1,text='MANAGE',height=55,width=80,corner_radius=10,command = manage,cursor='hand2',fg_color='#282927',text_color='white')
    managebutton.place(x=140,y=0)

    analyselbl=ck.CTkLabel(master=frame1,text='ANALYSE',height=55,width=80,corner_radius=10,fg_color='green',text_color='white')
    analyselbl.place(x=220,y=0)

    #settingsbutton=ck.CTkButton(master=frame1,text='SETTINGS',height=55,width=80,corner_radius=10,command = settings,cursor='hand2',fg_color='#282927',text_color='white')
    #settingsbutton.place(x=300,y=0)

    aboutbutton=ck.CTkButton(master=frame1,text='ABOUT',height=55,width=80,corner_radius=10,command = about,cursor='hand2',fg_color='#282927',text_color='white')
    aboutbutton.place(x=300,y=0)

#frame3 GRAPH1==============
    graph1analyselbl=ck.CTkLabel(master=frame3,text='GRAPH 1',text_color='white',font=('roboto',20))
    graph1analyselbl.place(x=135,y=0) 

    # lnpanalysebutton=ck.CTkButton(master=frame3,text='LNP',command=btn_clicked,height=80,width=80,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    # lnpanalysebutton.place(x=140,y=465)

    graphlist = ['Product Vs Sales(Bar Graph)','Product Vs Sales(Pie Chart)', 'Product Vs Quantity Sold(Bar Graph)',"Product Vs Quantity Sold(Pie Chart)",'Sales Vs Time(Line Graph)','Sales Vs Time(Bar Graph)','Profit Made Vs Time(Bar Graph)','Profit Made Vs Time(Line Graph)']

    analysedropdown1= ck.CTkOptionMenu(master=frame3,values=graphlist,command=dropdown1,width=100,height=30)
    analysedropdown1.place(x=10,y=40)

    itemname = pd.read_csv('user data\\'+uname+'Inventory(2).csv', usecols= ['Item_Name'] ).to_numpy().tolist()
    itemnamedropdownlst=['All']
    for i in itemname:
        itemnamedropdownlst.append(i[0])

    # analysedropdown2= ck.CTkOptionMenu(master=frame3,values=itemnamedropdownlst,command=dropdown2,width=100,height=30)
    # analysedropdown2.place(x=230,y=85)

#entryboxes==================
    fromanalyselbl1=ck.CTkLabel(master=frame3,text='FROM',text_color='white',font=('roboto',15))
    fromanalyselbl1.place(x=90,y=90)  
    fromanalyseentry1=ck.CTkEntry(master=frame3,placeholder_text='YYYY-MM-DD',width=210,height=30,corner_radius=20)
    fromanalyseentry1.place(x=70,y=120)

    toanalyselbl1=ck.CTkLabel(master=frame3,text='TO',text_color='white',font=('roboto',15))
    toanalyselbl1.place(x=90,y=160) 
    toanalyseentry1=ck.CTkEntry(master=frame3,placeholder_text='YYYY-MM-DD',width=210,height=31,corner_radius=20)
    toanalyseentry1.place(x=70,y=190)

    analysegraphitbutton1=ck.CTkButton(master=frame3,text='GRAPH IT',command=graphfunction1,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    analysegraphitbutton1.place(x=135,y=230)

 

    
#GRAPH 2==============================================

    graph2analyselbl=ck.CTkLabel(master=frame3,text='GRAPH 2',text_color='white',font=('roboto',20))
    graph2analyselbl.place(x=135,y=295) 


    graphlist2 = ['Quantity Vs Time(Line Graph)','Quantity Vs Time(Bar Graph)','Sales Vs Time(Line Graph)','Sales Vs Time(Bar Graph)']

    analysedropdown3= ck.CTkOptionMenu(master=frame3,values=graphlist2,command=dropdown3,width=100,height=30)
    analysedropdown3.place(x=10,y=335)

    itemname = pd.read_csv('user data\\'+uname+'Inventory(2).csv', usecols= ['Item_Name'] ).to_numpy().tolist()
    itemnamedropdownlst=[]
    for i in itemname:
        itemnamedropdownlst.append(i[0])

    analysedropdown4= ck.CTkOptionMenu(master=frame3,values=itemnamedropdownlst,command=dropdown4,width=100,height=30)
    analysedropdown4.place(x=230,y=380)
    
#entryboxes===============
    fromanalyselbl2=ck.CTkLabel(master=frame3,text='FROM',text_color='white',font=('roboto',15))
    fromanalyselbl2.place(x=90,y=385)  
    fromanalyseentry2=ck.CTkEntry(master=frame3,placeholder_text='YYYY-MM-DD',width=210,height=30,corner_radius=20)
    fromanalyseentry2.place(x=70,y=415)

    toanalyselbl2=ck.CTkLabel(master=frame3,text='TO',text_color='white',font=('roboto',15))
    toanalyselbl2.place(x=90,y=445) 
    toanalyseentry2=ck.CTkEntry(master=frame3,placeholder_text='YYYY-MM-DD',width=210,height=31,corner_radius=20)
    toanalyseentry2.place(x=70,y=475)

    analysegraphitbutton2=ck.CTkButton(master=frame3,text='GRAPH IT',command=graphfunction2,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    analysegraphitbutton2.place(x=135,y=515)


#ABOUT------------------------------------------------------------------------------------------------------------------------------
def about():
    global root3
    frame1=ck.CTkFrame(master=root3,width=1100,height=55,corner_radius=0,fg_color='#282927')
    frame1.grid(row=0,column=0) #REMEMBER RELATIVITY
    frame2=ck.CTkFrame(master=root3,width=1100,height=575,corner_radius=0)
    frame2.grid(row=1,column=0)
    
    # rlbl=ck.CTkLabel(master=frame2,text='ABOUT PAGE')
    # rlbl.place(x=0,y=0)
    lbl1=ck.CTkLabel(frame1,image=mangoimg,text='')
    lbl1.place(x=10,y=5)
    lbl2=ck.CTkLabel(frame1,image=accountimg,text='')
    lbl2.place(x=1040,y=5)
#frame1==============
    homebutton = ck.CTkButton(master=frame1,text='HOME',height=55,width=80,corner_radius=10,command = home,cursor='hand2',fg_color='#282927',text_color='white')
    homebutton.place(x=60,y=0)

    managebutton=ck.CTkButton(master=frame1,text='MANAGE',height=55,width=80,corner_radius=10,command = manage,cursor='hand2',fg_color='#282927',text_color='white')
    managebutton.place(x=140,y=0)

    analysebutton=ck.CTkButton(master=frame1,text='ANALYSE',height=55,width=80,corner_radius=10,command = analyse,cursor='hand2',fg_color='#282927',text_color='white')
    analysebutton.place(x=220,y=0)

    #settingsbutton=ck.CTkButton(master=frame1,text='SETTINGS',height=55,width=80,corner_radius=10,command = settings,cursor='hand2',fg_color='#282927',text_color='white')
    #settingsbutton.place(x=300,y=0)

    aboutlbl=ck.CTkLabel(master=frame1,text='ABOUT',height=55,width=80,corner_radius=10,fg_color='green',text_color='white')
    aboutlbl.place(x=300,y=0)

#frame2===============
    aboutuslbl=ck.CTkLabel(master=frame2,text='ABOUT US',height=55,width=80,corner_radius=10,text_color='silver',font=('Times New Roman',70))
    aboutuslbl.place(x=400,y=5)

    vaalbl=ck.CTkLabel(master=frame2,text="We are 'VAA': Versatile, Awesome, Adept",height=55,width=80,corner_radius=10,text_color='silver',font=('Times New Roman',27))
    vaalbl.place(x=350,y=90)

    learnerlbl=ck.CTkLabel(master=frame2,text="We are Learners, Hustlers, Problem Solvers and also students",height=55,width=80,corner_radius=10,text_color='silver',font=('Times New Roman',27))
    learnerlbl.place(x=250,y=130)

    vijaylbl=ck.CTkLabel(master=frame2,text="Vijaysubramanian",height=55,width=80,corner_radius=10,text_color='silver',font=('Times New Roman',30))
    vijaylbl.place(x=90,y=415)
    vijayimglbl=ck.CTkLabel(frame2,image=vijayimg,text='')
    vijayimglbl.place(x=90,y=190)

    abhinavlbl=ck.CTkLabel(master=frame2,text="Abhinav",height=55,width=80,corner_radius=10,text_color='silver',font=('Times New Roman',30))
    abhinavlbl.place(x=500,y=415)
    abhinavimglbl=ck.CTkLabel(frame2,image=abhinavimg,text='')
    abhinavimglbl.place(x=450,y=190)

    aniketlbl=ck.CTkLabel(master=frame2,text="Aniket",height=55,width=80,corner_radius=10,text_color='silver',font=('Times New Roman',30))
    aniketlbl.place(x=890,y=415)
    aniketimglbl=ck.CTkLabel(frame2,image=aniketimg,text='')
    aniketimglbl.place(x=820,y=190)

    contactlbl=ck.CTkLabel(master=frame2,text="Contact Us: Gmail: vaamango3@gmail.com",height=55,width=80,corner_radius=10,text_color='silver',font=('Times New Roman',20))
    contactlbl.place(x=30,y=500)
    

    # rimg=ck.CTkLabel(master=frame2,text='',image=bgimg,corner_radius=100)
    # rimg.place(x=110,y=200)

    instructionsbutton=ck.CTkButton(master=frame2,text='INSTRUCTIONS',command=instructionpg,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    instructionsbutton.place(x=490,y=525)

def instructionpg():
    global root3
    frame1=ck.CTkFrame(master=root3,width=1100,height=55,corner_radius=0,fg_color='#282927')
    frame1.grid(row=0,column=0) #REMEMBER RELATIVITY
    frame2=ck.CTkFrame(master=root3,width=1100,height=575,corner_radius=0)
    frame2.grid(row=1,column=0)
    
    # rlbl=ck.CTkLabel(master=frame2,text='ABOUT PAGE')
    # rlbl.place(x=0,y=0)
    lbl1=ck.CTkLabel(frame1,image=mangoimg,text='')
    lbl1.place(x=10,y=5)
    lbl2=ck.CTkLabel(frame1,image=accountimg,text='')
    lbl2.place(x=1040,y=5)
#frame1==============
    homebutton = ck.CTkButton(master=frame1,text='HOME',height=55,width=80,corner_radius=10,command = home,cursor='hand2',fg_color='#282927',text_color='white')
    homebutton.place(x=60,y=0)

    managebutton=ck.CTkButton(master=frame1,text='MANAGE',height=55,width=80,corner_radius=10,command = manage,cursor='hand2',fg_color='#282927',text_color='white')
    managebutton.place(x=140,y=0)

    analysebutton=ck.CTkButton(master=frame1,text='ANALYSE',height=55,width=80,corner_radius=10,command = analyse,cursor='hand2',fg_color='#282927',text_color='white')
    analysebutton.place(x=220,y=0)

    #settingsbutton=ck.CTkButton(master=frame1,text='SETTINGS',height=55,width=80,corner_radius=10,command = settings,cursor='hand2',fg_color='#282927',text_color='white')
    #settingsbutton.place(x=300,y=0)

    aboutlbl=ck.CTkLabel(master=frame1,text='ABOUT',height=55,width=80,corner_radius=10,fg_color='green',text_color='white')
    aboutlbl.place(x=300,y=0)

#frame2===================
    instructionheadinglbl=ck.CTkLabel(master=frame2,text='INSTRUCTIONS',height=55,width=80,corner_radius=10,text_color='silver',font=('Times New Roman',50))
    instructionheadinglbl.place(x=320,y=5)
    
    instruction_text=ck.CTkTextbox(master=frame2,width=1060,height=430,font=('Times New Roman',20) )

    instructions="1. To search an item either enter its itemname or itemcode or both. Wherever there is an option between itemname and itemcode try to use itemcode.\n2. In sales page to search for a bill enter its sales no. (bill no.).\n3. Always enter date in YYYY-MM-DD format.\n4. The tables may show date in either YYYY-MM-DD format or DD-MM-YY format.\n5. To update itemcode or itemname of an item use Cost Table. NOTE: You can't update itemcode and itemname of an item simultaneously.\n6. To delete a record select that record on the table.\n7. Don't Click on bill text box in bill page.\n8. In stock page you can only update the quantity bought column.\n9. To search a bill write its Sales no. in the sales no. entry box and don't write anything in the other entryboxes.\n10. In stock page SE stands for stock entry."
    
    instruction_text.insert('insert',instructions)
    
    instruction_text.configure(state='disabled')
    instruction_text.place(x=20,y=80) 

    backbutton=ck.CTkButton(master=frame2,text='BACK',command=about,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    backbutton.place(x=490,y=525)

#STOCK-----------------------------------------------------------------------------------------------------------------------------------
def stock(): 
    def clear_stock():
        global itemcodeentrystock,itemnameentrystock,quantityentrystock,itemcodestringvarstock,itemnamestringvarstock,quantitystringvarstock
        itemcodestringvarstock=t.StringVar()
        itemcodeentrystock=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=itemcodestringvarstock)
        itemcodeentrystock.place(x=39,y=125)

        itemnamestringvarstock=t.StringVar()
        itemnameentrystock=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=itemnamestringvarstock)
        itemnameentrystock.place(x=39,y=195)

        quantitystringvarstock=t.StringVar()
        quantityentrystock=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=quantitystringvarstock)
        quantityentrystock.place(x=39,y=265) 

    def stock_treeview(a):
        global stock_tree
        #treeview-----------------------------------------------------------------------------------------------------------------------------
        style=ttk.Style()
        # Add some style

        style.theme_use("clam")
        style.configure('Treeview',background='#5e6273',foreground='white',rowheight=65,fieldbackground='#5e6273',font=('Times New Roman',24))
        style.configure('Treeview.Heading',background='#5e6273',foreground='white',rowheight=50,fieldbackground='##5e6273',font=('Times New Roman',22))
        # Change selected color
        style.map('Treeview', 
        background=[('selected', '#34eb80')])
        
        #textbox
        

        #scrolllll bar
        stocktree_scroll = ck.CTkScrollbar(master=frame4,width=20,height=467,hover=True,fg_color='#504F4F') #504F4F
        stocktree_scroll.place(x=610,y=40)
        
        # setting treeview
        stock_tree = ttk.Treeview(frame4,yscrollcommand=stocktree_scroll.set,selectmode='browse')
        stockdf= pd.read_csv('user data\\'+uname+'Stock_Entry.csv')

        stocktree_scroll.configure(command=stock_tree.yview)
        
            # Set up new treeview
        stock_list=list(stockdf.columns)
        stock_tree["column"] = stock_list
        # print(stock_list)
        stock_tree["show"] = "headings"
        stock_tree.column(stock_list[0],width=180,stretch=False,minwidth=180)
        stock_tree.column(stock_list[1],width=180,stretch=False,minwidth=180)
        stock_tree.column(stock_list[2],width=210,stretch=False,minwidth=210)
        stock_tree.column(stock_list[3],width=180,stretch=False,minwidth=180)
        stock_tree.column(stock_list[4],width=150,stretch=False,minwidth=150)
        
        # Loop thru column list for headers
        for column in stock_tree["column"]:
            stock_tree.heading(column, text=column)

        # Put data in treeview
        stockdf_rows = stockdf.to_numpy().tolist()
        for row in stockdf_rows:
            stock_tree.insert("", "end", values=row)
        
        # Pack the treeview finally
        stock_tree.place(x=10,y=60)
        stock_tree.bind("<ButtonRelease-1>", stock_info)
    
    def search_stock():
        global stock_tree ,itemcodeentrystock,itemnameentrystock
        style=ttk.Style()
        # Add some style

        style.theme_use("clam")
        style.configure('Treeview',background='#5e6273',foreground='white',rowheight=65,fieldbackground='#5e6273',font=('Times New Roman',24))
        style.configure('Treeview.Heading',background='#5e6273',foreground='white',rowheight=50,fieldbackground='#5e6273',font=('Times New Roman',24))
        # Change selected color
        style.map('Treeview', 
        background=[('selected', '#34eb80')])
        
        #textbox
        

        #scrolllll bar
        stocktree_scroll = ck.CTkScrollbar(master=frame4,width=20,height=467,hover=True,fg_color='#504F4F') #504F4F
        stocktree_scroll.place(x=610,y=40)
        
        # setting treeview
        stock_tree = ttk.Treeview(frame4,yscrollcommand=stocktree_scroll.set,selectmode='browse')
        stockdf= pd.read_csv('user data\\'+uname+'Stock_Entry.csv')

        if itemnameentrystock.get():
            stockdf=stockdf[stockdf['Item_Name']==itemnameentrystock.get()]
        elif itemcodeentrystock.get():
            stockdf=stockdf[stockdf['Item_Code']==int(itemcodeentrystock.get())]

        stocktree_scroll.configure(command=stock_tree.yview)
        
            # Set up new treeview
        stock_list=list(stockdf.columns)
        stock_tree["column"] = stock_list
        # print(stock_list)
        stock_tree["show"] = "headings"
        stock_tree.column(stock_list[0],width=200,stretch=False,minwidth=200)
        stock_tree.column(stock_list[1],width=200,stretch=False,minwidth=200)
        stock_tree.column(stock_list[2],width=300,stretch=False,minwidth=300)
        stock_tree.column(stock_list[3],width=200,stretch=False,minwidth=200)
        
        # Loop thru column list for headers
        for column in stock_tree["column"]:
            stock_tree.heading(column, text=column)

        # Put data in treeview
        stockdf_rows = stockdf.to_numpy().tolist()
        for row in stockdf_rows:
            stock_tree.insert("", "end", values=row)
        
        # Pack the treeview finally
        stock_tree.place(x=10,y=60)
        stock_tree.bind("<ButtonRelease-1>", stock_info)

    global root3,stock_tree
    frame1=ck.CTkFrame(master=root3,width=1100,height=55,corner_radius=0,fg_color='#282927')
    frame1.grid(row=0,column=0) #REMEMBER RELATIVITY
    frame2=ck.CTkFrame(master=root3,width=1100,height=575,corner_radius=0)
    frame2.grid(row=1,column=0)
    frame3=ck.CTkFrame(master=frame2,width=288,height=555,corner_radius=20) # agar corners rounded chahiye then use master= frame2
    frame3.place(x=10,y=15)
    frame4=ck.CTkFrame(master=frame2, width=645,height=555,corner_radius=20)
    frame4.place(x=326,y=15)

    lbl1=ck.CTkLabel(frame1,image=mangoimg,text='')
    lbl1.place(x=10,y=5)
    lbl2=ck.CTkLabel(frame1,image=accountimg,text='')
    lbl2.place(x=1040,y=5)
    
#frame1 buttons----------------------------------------------------------------------------------------------------------------------

    homebutton = ck.CTkButton(master=frame1,text='HOME',height=55,width=80,corner_radius=10,command = home,cursor='hand2',fg_color='#282927',text_color='white')
    homebutton.place(x=60,y=0)

    managelbl=ck.CTkLabel(master=frame1,text='MANAGE',height=55,width=80,corner_radius=10,fg_color='green',text_color='white')
    managelbl.place(x=140,y=0)

    analysebutton=ck.CTkButton(master=frame1,text='ANALYSE',height=55,width=80,corner_radius=10,command = analyse,cursor='hand2',fg_color='#282927',text_color='white')
    analysebutton.place(x=220,y=0)

    #settingsbutton=ck.CTkButton(master=frame1,text='SETTINGS',height=55,width=80,corner_radius=10,command = settings,cursor='hand2',fg_color='#282927',text_color='white')
    #settingsbutton.place(x=300,y=0)

    aboutbutton=ck.CTkButton(master=frame1,text='ABOUT',height=55,width=80,corner_radius=10,command = about,cursor='hand2',fg_color='#282927',text_color='white')
    aboutbutton.place(x=300,y=0)

#right side buttons----------------------------------------------------------------------------------------------------------------

    inventorybutton=ck.CTkButton(master=frame2,text='INVENTORY',command=inventory,image=inventoryimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom', font=('roboto',10))
    inventorybutton.place(x=995,y=43)

    stocklbl=ck.CTkLabel(master=frame2,text='STOCK',image=stockimg,height=100,width=100,corner_radius=20,fg_color='green',text_color='white',compound='bottom')
    stocklbl.place(x=995,y=178)

    billbutton=ck.CTkButton(master=frame2,text='BILL',command=bill,image=billimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    billbutton.place(x=995,y=313)

    salesbutton=ck.CTkButton(master=frame2,text='SALES',command=sales,image=salesimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    salesbutton.place(x=995,y=448)

#frame3---------------------------------------------------------------------------------------------------------------------------

    managestocklbl=ck.CTkLabel(master=frame3,text='MANAGE STOCKS',text_color='white',font=('roboto',20))
    managestocklbl.place(x=50,y=0)

    notepadlbl=ck.CTkLabel(master=frame3,image=notepadimg,text='')
    notepadlbl.place(x=110,y=30)

#Entry boxes======================#date entry is not required
    itemcodelbl1=ck.CTkLabel(master=frame3,text='ITEM CODE(NUMBER)',text_color='white',font=('roboto',12))
    itemcodelbl1.place(x=55,y=95)  
    
    # itemcodeentrystock=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # itemcodeentrystock.place(x=39,y=125)

    itemnamelbl1=ck.CTkLabel(master=frame3,text='ITEM NAME',text_color='white',font=('roboto',12))
    itemnamelbl1.place(x=55,y=165) #ydifference of 70
    
    # itemnameentrystock=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # itemnameentrystock.place(x=39,y=195)

    #date entry is not required
    """ datelbl=ck.CTkLabel(master=frame3,text='DATE',text_color='white',font=('roboto',12))
    datelbl.place(x=3,y=235)
    dateentry=ck.CTkEntry(master=frame3,placeholder_text='YYYY-MM-DD',width=210,height=31,corner_radius=20)
    dateentry.place(x=39,y=265) """

    quantitylbl1=ck.CTkLabel(master=frame3,text='QUANTITY',text_color='white',font=('roboto',12))
    quantitylbl1.place(x=55,y=235)

   
    
    # quantityentrystock=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # quantityentrystock.place(x=39,y=265)

#clear_stock funcn==============
    clear_stock()

#BUTTONS================

    addbutton=ck.CTkButton(master=frame3,text='ADD',command=Stock_Entry,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    addbutton.place(x=27,y=380)
    addbutton.bind("<ButtonRelease-1>", stock_treeview)

    deletebutton=ck.CTkButton(master=frame3,text='DELETE',command=delete_stock,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    deletebutton.place(x=165,y=380)
    deletebutton.bind("<ButtonRelease-1>", stock_treeview)


    updatebutton=ck.CTkButton(master=frame3,text='UPDATE',command=update_stock,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    updatebutton.place(x=27,y=430)
    updatebutton.bind("<ButtonRelease-1>", stock_treeview)

    clearbutton=ck.CTkButton(master=frame3,text='CLEAR',command=clear_stock,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    clearbutton.place(x=165,y=430)
    clearbutton.bind("<ButtonRelease-1>", stock_treeview)

    costbutton=ck.CTkButton(master=frame3,text='COST TABLE',command=stock_cost,image=rupeeimg,height=74,width=70,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    costbutton.place(x=160,y=475)

    searchcostbutton=ck.CTkButton(master=frame3,text='SEARCH',command=search_stock,image=searchimg,height=74,width=74,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    searchcostbutton.place(x=27,y=475)
    
#treeview=================
    stock_treeview(1)

def stock_cost():
    def clear_cost():
        global itemcodeentrystock_cost,costpriceentrystock_cost,sellingpriceentrystock_cost,itemnameentrystock_cost,itemcodestringvarcost,itemnamestringvarcost,costpricestringvarcost,sellingpricestringvarcost

        itemcodestringvarcost=t.StringVar()
        itemcodeentrystock_cost=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=itemcodestringvarcost)
        itemcodeentrystock_cost.place(x=39,y=125)

        itemnamestringvarcost=t.StringVar()
        itemnameentrystock_cost=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=itemnamestringvarcost)
        itemnameentrystock_cost.place(x=39,y=195)

        costpricestringvarcost=t.StringVar()
        costpriceentrystock_cost=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=costpricestringvarcost)
        costpriceentrystock_cost.place(x=39,y=265)

        sellingpricestringvarcost=t.StringVar()
        sellingpriceentrystock_cost=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=sellingpricestringvarcost)
        sellingpriceentrystock_cost.place(x=39,y=335) 

    def cost_treeview(a):
        global cost_tree,Costdf
        #treeview-----------------------------------------------------------------------------------------------------------------------------
        style=ttk.Style()
        # Add some style

        style.theme_use("clam")
        style.configure('Treeview',
        background='#5e6273',foreground='white',rowheight=50,fieldbackground='#5e6273',font=('Times New Roman',27))
        style.configure('Treeview.Heading',background='#5e6273',foreground='white',rowheight=50,fieldbackground='#5e6273',font=('Times New Roman',30))
        # Change selected color
        style.map('Treeview', 
        background=[('selected', '#34eb80')])

        #scrollbar
        costtree_scroll = ck.CTkScrollbar(master=frame4,width=20,height=373,hover=True,fg_color='#504F4F') #504F4F
        costtree_scroll.place(x=695,y=67)
        
        # setting treeview
        cost_tree = ttk.Treeview(frame4,selectmode='browse',yscrollcommand=costtree_scroll.set)
        Costdf= pd.read_csv('user data\\'+uname+'Cost.csv')
        
        costtree_scroll.configure(command=cost_tree.yview)

            # Set up new treeview
        cost_list=list(Costdf.columns)
        cost_tree["column"] = cost_list
        cost_tree["show"] = "headings"
        cost_tree.column(cost_list[0],width=250,stretch=False,minwidth=250)
        cost_tree.column(cost_list[1],width=250,stretch=False,minwidth=250)
        cost_tree.column(cost_list[2],width=250,stretch=False,minwidth=250)
        cost_tree.column(cost_list[3],width=250,stretch=False,minwidth=250)
        # Loop thru column list for headers
        for column in cost_tree["column"]:
            cost_tree.heading(column, text=column)

        # Put data in treeview
        Costdf_rows = Costdf.to_numpy().tolist()
        for row in Costdf_rows:
            cost_tree.insert("", "end", values=row)
        
        
        # Pack the treeview finally
        cost_tree.place(x=40,y=100)
        cost_tree.bind("<ButtonRelease-1>", cost_info)

    def search_cost():
        global cost_tree,itemcodeentrystock_cost,itemnameentrystock_cost
        #treeview-----------------------------------------------------------------------------------------------------------------------------
        style=ttk.Style()
        # Add some style

        style.theme_use("clam")
        style.configure('Treeview',
        background='#5e6273',foreground='white',rowheight=50,fieldbackground='#5e6273',font=('Times New Roman',27))
        style.configure('Treeview.Heading',background='#5e6273',foreground='white',rowheight=50,fieldbackground='#5e6273',font=('Times New Roman',30))
        # Change selected color
        style.map('Treeview', 
        background=[('selected', '#34eb80')])

        #scrollbar
        costtree_scroll = ck.CTkScrollbar(master=frame4,width=20,height=373,hover=True,fg_color='#504F4F') #504F4F
        costtree_scroll.place(x=695,y=67)
        
        # setting treeview
        cost_tree = ttk.Treeview(frame4,selectmode='browse',yscrollcommand=costtree_scroll.set)
        Costdf= pd.read_csv('user data\\'+uname+'Cost.csv')
        if itemnameentrystock_cost.get():
            Costdf=Costdf[Costdf['Item_Name']==itemnameentrystock_cost.get()]
        elif itemcodeentrystock_cost.get():
            Costdf=Costdf[Costdf['Item_Code']==int(itemcodeentrystock_cost.get())]
        
        costtree_scroll.configure(command=cost_tree.yview)

            # Set up new treeview
        cost_list=list(Costdf.columns)
        cost_tree["column"] = cost_list
        cost_tree["show"] = "headings"
        cost_tree.column(cost_list[0],width=250,stretch=False,minwidth=250)
        cost_tree.column(cost_list[1],width=250,stretch=False,minwidth=250)
        cost_tree.column(cost_list[2],width=250,stretch=False,minwidth=250)
        cost_tree.column(cost_list[3],width=250,stretch=False,minwidth=250)
        # Loop thru column list for headers
        for column in cost_tree["column"]:
            cost_tree.heading(column, text=column)

        # Put data in treeview
        Costdf_rows = Costdf.to_numpy().tolist()
        for row in Costdf_rows:
            cost_tree.insert("", "end", values=row)
        
        
        # Pack the treeview finally
        cost_tree.place(x=40,y=100)
        cost_tree.bind("<ButtonRelease-1>", cost_info)
        

    global root3,Costdf,cost_tree
    frame1=ck.CTkFrame(master=root3,width=1100,height=55,corner_radius=0,fg_color='#282927')
    frame1.grid(row=0,column=0) #REMEMBER RELATIVITY
    frame2=ck.CTkFrame(master=root3,width=1100,height=575,corner_radius=0)
    frame2.grid(row=1,column=0)
    frame3=ck.CTkFrame(master=frame2,width=288,height=555,corner_radius=20) # agar corners rounded chahiye then use master= frame2
    frame3.place(x=10,y=15)
    frame4=ck.CTkFrame(master=frame2, width=750,height=555,corner_radius=20)
    frame4.place(x=326,y=15)

    lbl1=ck.CTkLabel(frame1,image=mangoimg,text='')
    lbl1.place(x=10,y=5)
    lbl2=ck.CTkLabel(frame1,image=accountimg,text='')
    lbl2.place(x=1040,y=5)

#frame1 buttons----------------------------------------------------------------------------------------------------------------------

    homebutton = ck.CTkButton(master=frame1,text='HOME',height=55,width=80,corner_radius=10,command = home,cursor='hand2',fg_color='#282927',text_color='white')
    homebutton.place(x=60,y=0)

    

    managelbl=ck.CTkLabel(master=frame1,text='MANAGE',height=55,width=80,corner_radius=10,fg_color='green',text_color='white')
    managelbl.place(x=140,y=0)

    analysebutton=ck.CTkButton(master=frame1,text='ANALYSE',height=55,width=80,corner_radius=10,command = analyse,cursor='hand2',fg_color='#282927',text_color='white')
    analysebutton.place(x=220,y=0)

    #settingsbutton=ck.CTkButton(master=frame1,text='SETTINGS',height=55,width=80,corner_radius=10,command = settings,cursor='hand2',fg_color='#282927',text_color='white')
    #settingsbutton.place(x=300,y=0)

    aboutbutton=ck.CTkButton(master=frame1,text='ABOUT',height=55,width=80,corner_radius=10,command = about,cursor='hand2',fg_color='#282927',text_color='white')
    aboutbutton.place(x=300,y=0)

#frame3----------------------------------------------------------------------------------------------------------------------------

    costtablelbl=ck.CTkLabel(master=frame3,text='COST TABLE',text_color='white',font=('roboto',20))
    costtablelbl.place(x=75,y=0)

    rupeelbl=ck.CTkLabel(master=frame3,image=rupeeimg2,text='')
    rupeelbl.place(x=110,y=30)

#Entryboxes=======================

    itemcodelbl2=ck.CTkLabel(master=frame3,text='ITEM CODE(NUMBER)',text_color='white',font=('roboto',12))
    itemcodelbl2.place(x=55,y=95)
    # itemcodeentrystock_cost=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # itemcodeentrystock_cost.place(x=39,y=125)

    itemnamelblcost=ck.CTkLabel(master=frame3,text='ITEM NAME',text_color='white',font=('roboto',12))
    itemnamelblcost.place(x=55,y=165)

    costpricelbl1=ck.CTkLabel(master=frame3,text='COST PRICE',text_color='white',font=('roboto',12))
    costpricelbl1.place(x=55,y=235)
    # costpriceentrystock_cost=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # costpriceentrystock_cost.place(x=39,y=195)

    sellingprice1=ck.CTkLabel(master=frame3,text='SELLING PRICE',text_color='white',font=('roboto',12))
    sellingprice1.place(x=55,y=305)         
    # sellingpriceentrystock_cost=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # sellingpriceentrystock_cost.place(x=39,y=265) 

#clear_cost() funcn==============
    clear_cost()

#buttons=======================    

    addbutton=ck.CTkButton(master=frame3,text='ADD',command=Cost,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    addbutton.place(x=27,y=380)
    addbutton.bind("<ButtonRelease-1>", cost_treeview)

    deletebutton=ck.CTkButton(master=frame3,text='DELETE',command=delete_cost,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    deletebutton.place(x=165,y=380)
    deletebutton.bind("<ButtonRelease-1>", cost_treeview)

    updatebutton=ck.CTkButton(master=frame3,text='UPDATE',command=update_cost,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    updatebutton.place(x=27,y=430)
    updatebutton.bind("<ButtonRelease-1>", cost_treeview)

    clearbutton=ck.CTkButton(master=frame3,text='CLEAR',command=clear_cost,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    clearbutton.place(x=165,y=430)
    clearbutton.bind("<ButtonRelease-1>", cost_treeview)

    backbutton=ck.CTkButton(master=frame3,text='BACK',command=stock,image=backimg,height=74,width=80,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    backbutton.place(x=165,y=475)

    searchcostbutton=ck.CTkButton(master=frame3,text='SEARCH',command=search_cost,image=searchimg,height=74,width=74,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    searchcostbutton.place(x=27,y=475)

#treeview==============
    cost_treeview(1)


#inventory-----------------------------------------------------------------------------------------------------------------------------

def inventory():
    def clear_inventory():
        global itemnameentryinventory,itemcodeentryinventory,instockinventoryentry,itemcodestringvarinventory,itemnamestringvarinventory,instockstringvarinventory
        itemcodestringvarinventory=t.StringVar()
        itemcodeentryinventory=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=itemcodestringvarinventory)
        itemcodeentryinventory.place(x=39,y=125)

        itemnamestringvarinventory=t.StringVar()
        itemnameentryinventory=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=itemnamestringvarinventory)
        itemnameentryinventory.place(x=39,y=195)

        instockstringvarinventory=t.StringVar()
        instockinventoryentry=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=instockstringvarinventory)
        instockinventoryentry.place(x=39,y=265)

    def inventory_treeview(a):
        global inventory_tree
        style=ttk.Style()
        # Add some style

        style.theme_use("clam")
        style.configure('Treeview',background='#5e6273',foreground='white',rowheight=60,fieldbackground='#5e6273',font=('Times New Roman',27)) #373535
        style.configure('Treeview.Heading',background='#5e6273',foreground='white',rowheight=50,fieldbackground='#5e6273',font=('Times New Roman',24)) #5A5A5A
        # Change selected color
        style.map('Treeview', background=[('selected', '#34eb80')]) #34eb80

        #scrollbar
        inventorytree_scroll = ck.CTkScrollbar(master=frame4,width=20,height=435,hover=True,fg_color='#504F4F') #504F4F
        inventorytree_scroll.place(x=602,y=65)
        
        # setting treeview
        inventory_tree = ttk.Treeview(frame4,selectmode='browse',yscrollcommand=inventorytree_scroll.set)
        inventorydf= pd.read_csv('user data\\'+uname+'Inventory(2).csv')
        
        inventorytree_scroll.configure(command=inventory_tree.yview)
            # Set up new treeview
        inventory_list=list(inventorydf.columns)
        inventory_tree["column"] = inventory_list

        inventory_tree["show"] = "headings"
        inventory_tree.column(inventory_list[0],width=280,stretch=False,minwidth=280)
        inventory_tree.column(inventory_list[1],width=300,stretch=False,minwidth=300)
        inventory_tree.column(inventory_list[2],width=280,stretch=False,minwidth=280)

        
        # Loop thru column list for headers
        for column in inventory_tree["column"]:
            inventory_tree.heading(column, text=column)

        # Put data in treeview
        inventorydf_rows = inventorydf.to_numpy().tolist()
        for row in inventorydf_rows:
            inventory_tree.insert("", "end", values=row)
        
        
        # Pack the treeview finally
        inventory_tree.place(x=40,y=100)
        inventory_tree.bind("<ButtonRelease-1>", inventory_info)
        
    
    def search_inventory():
        global inventory_tree,itemcodeentryinventory,itemnameentryinventory
        style=ttk.Style()
        # Add some style

        style.theme_use("clam")
        style.configure('Treeview',background='#5e6273',foreground='white',rowheight=60,fieldbackground='#5e6273',font=('Times New Roman',27))
        style.configure('Treeview.Heading',background='#5e6273',foreground='white',rowheight=50,fieldbackground='#5e6273',font=('Times New Roman',24))
        # Change selected color
        style.map('Treeview', background=[('selected', '#34eb80')])

        #scrollbar
        inventorytree_scroll = ck.CTkScrollbar(master=frame4,width=20,height=435,hover=True,fg_color='#504F4F') #504F4F
        inventorytree_scroll.place(x=602,y=65)
        
        # setting treeview
        inventory_tree = ttk.Treeview(frame4,selectmode='browse',yscrollcommand=inventorytree_scroll.set)
        inventorydf= pd.read_csv('user data\\'+uname+'Inventory(2).csv')
        
        I_Cinventory=itemcodeentryinventory.get()
        I_Ninventory=itemnameentryinventory.get()
        if I_Ninventory:
            inventorydf=inventorydf[inventorydf['Item_Name']==I_Ninventory]

        elif I_Cinventory:
            I_Cinventoryint=int(I_Cinventory)
            inventorydf=inventorydf[inventorydf['Item_Code']==I_Cinventoryint]
        
        inventorytree_scroll.configure(command=inventory_tree.yview)
            # Set up new treeview
        inventory_list=list(inventorydf.columns)
        inventory_tree["column"] = inventory_list

        inventory_tree["show"] = "headings"
        inventory_tree.column(inventory_list[0],width=280,stretch=False,minwidth=280)
        inventory_tree.column(inventory_list[1],width=300,stretch=False,minwidth=300)
        inventory_tree.column(inventory_list[2],width=280,stretch=False,minwidth=280)

        
        # Loop thru column list for headers
        for column in inventory_tree["column"]:
            inventory_tree.heading(column, text=column)

        # Put data in treeview
        inventorydf_rows = inventorydf.to_numpy().tolist()
        for row in inventorydf_rows:
            inventory_tree.insert("", "end", values=row)
        
        
        # Pack the treeview finally
        inventory_tree.place(x=40,y=100)
        inventory_tree.bind("<ButtonRelease-1>", inventory_info)
        

    global root3,inventory_tree
    frame1=ck.CTkFrame(master=root3,width=1100,height=55,corner_radius=0,fg_color='#282927')
    frame1.grid(row=0,column=0) #REMEMBER RELATIVITY
    frame2=ck.CTkFrame(master=root3,width=1100,height=575,corner_radius=0)
    frame2.grid(row=1,column=0)
    frame3=ck.CTkFrame(master=frame2,width=280,height=370,corner_radius=20) # agar corners rounded chahiye then use master= frame2
    frame3.place(x=10,y=15)
    frame4=ck.CTkFrame(master=frame2, width=645,height=555,corner_radius=20)
    frame4.place(x=326,y=15)

    lbl1=ck.CTkLabel(frame1,image=mangoimg,text='')
    lbl1.place(x=10,y=5)
    lbl2=ck.CTkLabel(frame1,image=accountimg,text='')
    lbl2.place(x=1040,y=5)
    
#frame1 buttons----------------------------------------------------------------------------------------------------------------------

    homebutton = ck.CTkButton(master=frame1,text='HOME',height=55,width=80,corner_radius=10,command = home,cursor='hand2',fg_color='#282927',text_color='white')
    homebutton.place(x=60,y=0)

    managelbl=ck.CTkLabel(master=frame1,text='MANAGE',height=55,width=80,corner_radius=10,fg_color='green',text_color='white')
    managelbl.place(x=140,y=0)

    analysebutton=ck.CTkButton(master=frame1,text='ANALYSE',height=55,width=80,corner_radius=10,command = analyse,cursor='hand2',fg_color='#282927',text_color='white')
    analysebutton.place(x=220,y=0)

    #settingsbutton=ck.CTkButton(master=frame1,text='SETTINGS',height=55,width=80,corner_radius=10,command = settings,cursor='hand2',fg_color='#282927',text_color='white')
    #settingsbutton.place(x=300,y=0)

    aboutbutton=ck.CTkButton(master=frame1,text='ABOUT',height=55,width=80,corner_radius=10,command = about,cursor='hand2',fg_color='#282927',text_color='white')
    aboutbutton.place(x=300,y=0)

#right side buttons----------------------------------------------------------------------------------------------------------------

    inventorylbl=ck.CTkLabel(master=frame2,text='INVENTORY',image=inventoryimg,height=100,width=100,corner_radius=20,fg_color='green',text_color='white',compound='bottom', font=('roboto',10))
    inventorylbl.place(x=995,y=43)

    stockbutton=ck.CTkButton(master=frame2,text='STOCK',command=stock,image=stockimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    stockbutton.place(x=995,y=178)

    billbutton=ck.CTkButton(master=frame2,text='BILL',command=bill,image=billimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    billbutton.place(x=995,y=313)

    salesbutton=ck.CTkButton(master=frame2,text='SALES',command=sales,image=salesimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    salesbutton.place(x=995,y=448)

#frame3-------------------------------------------------------------------------------------------------------------------------------

    inventorylbl2=ck.CTkLabel(master=frame3,text='INVENTORY',text_color='white',font=('roboto',20))
    inventorylbl2.place(x=85,y=0)

    inventoryylbl=ck.CTkLabel(master=frame3,image=inventorynoteimg,text='')
    inventoryylbl.place(x=110,y=35)

    #frame3 buttons
    itemcodelbl3=ck.CTkLabel(master=frame3,text='ITEM CODE(NUMBER)',text_color='white',font=('roboto',12))
    itemcodelbl3.place(x=55,y=95)
    # itemcodeentryinventory=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # itemcodeentryinventory.place(x=39,y=125)

    itemnamelbl2=ck.CTkLabel(master=frame3,text='ITEM NAME',text_color='white',font=('roboto',12))
    itemnamelbl2.place(x=55,y=165)
    # itemnameentryinventory=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # itemnameentryinventory.place(x=39,y=195)

    instockinventorylbl=ck.CTkLabel(master=frame3,text='IN STOCK',text_color='white',font=('roboto',12))
    instockinventorylbl.place(x=55,y=235)
    # instockinventoryentry=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # instockinventoryentry.place(x=39,y=265)

    #clear_inventory

    clear_inventory()

    searchbutton=ck.CTkButton(master=frame3,text='SEARCH',command=search_inventory,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    searchbutton.place(x=20,y=320)

    clearbutton=ck.CTkButton(master=frame3,text='CLEAR',command=clear_inventory,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    clearbutton.place(x=160,y=320)

    clearbutton.bind("<ButtonRelease-1>", inventory_treeview)

#treeview-----------------------------------------------------------------------------------------------------------------------------
    inventory_treeview(1)

    


#bil------------------------------------------------------------------------------------------------------------------------------------
def bill():
    def clear_billentry():
        global itemcodeentrybill,quantityentrybill,itemcodestringvarbill,quantitystringvarbill
        # itemnameentrybill=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,)
        # itemnameentrybill.place(x=39,y=125)

        itemcodestringvarbill=t.StringVar()
        itemcodeentrybill=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=itemcodestringvarbill)
        itemcodeentrybill.place(x=39,y=195)

        quantitystringvarbill=t.StringVar()
        quantityentrybill=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=quantitystringvarbill)
        quantityentrybill.place(x=39,y=265)

        # bill()
    def instocklabel(i):
        global billdropdowndata,itemcodestringvarbill
        billdropdowndata=i

        inventorydf= pd.read_csv('user data\\'+uname+'Inventory(2).csv')
        instock = (inventorydf[inventorydf['Item_Name']== billdropdowndata]['In_Stock']).to_numpy().tolist()
        instocklbl = ck.CTkLabel(master=frame3,text= 'In Stock: '+str(instock[0])+'\t\t',text_color='yellow',font=('roboto',12))
        instocklbl.place(x=55,y=300)
        
        I_Cbill=inventorydf[inventorydf['Item_Name']== billdropdowndata]['Item_Code'].to_numpy().tolist()[0]
        itemcodestringvarbill.set(str(I_Cbill))
        

    global root3,billlst,bill_text
    frame1=ck.CTkFrame(master=root3,width=1100,height=55,corner_radius=0,fg_color='#282927')
    frame1.grid(row=0,column=0) #REMEMBER RELATIVITY
    frame2=ck.CTkFrame(master=root3,width=1100,height=575,corner_radius=0)
    frame2.grid(row=1,column=0)
    frame3=ck.CTkFrame(master=frame2,width=288,height=555,corner_radius=20) # agar corners rounded chahiye then use master= frame2
    frame3.place(x=10,y=15)
    frame4=ck.CTkFrame(master=frame2, width=645,height=555,corner_radius=20)
    frame4.place(x=326,y=15)

    lbl1=ck.CTkLabel(frame1,image=mangoimg,text='')
    lbl1.place(x=10,y=5)
    lbl2=ck.CTkLabel(frame1,image=accountimg,text='')
    lbl2.place(x=1040,y=5)
    
#frame1 buttons----------------------------------------------------------------------------------------------------------------------

    homebutton = ck.CTkButton(master=frame1,text='HOME',height=55,width=80,corner_radius=10,command = home,cursor='hand2',fg_color='#282927',text_color='white')
    homebutton.place(x=60,y=0)

    managelbl=ck.CTkLabel(master=frame1,text='MANAGE',height=55,width=80,corner_radius=10,fg_color='green',text_color='white')
    managelbl.place(x=140,y=0)

    analysebutton=ck.CTkButton(master=frame1,text='ANALYSE',height=55,width=80,corner_radius=10,command = analyse,cursor='hand2',fg_color='#282927',text_color='white')
    analysebutton.place(x=220,y=0)

    #settingsbutton=ck.CTkButton(master=frame1,text='SETTINGS',height=55,width=80,corner_radius=10,command = settings,cursor='hand2',fg_color='#282927',text_color='white')
    #settingsbutton.place(x=300,y=0)

    aboutbutton=ck.CTkButton(master=frame1,text='ABOUT',height=55,width=80,corner_radius=10,command = about,cursor='hand2',fg_color='#282927',text_color='white')
    aboutbutton.place(x=300,y=0)

#right side buttons----------------------------------------------------------------------------------------------------------------

    inventorybutton=ck.CTkButton(master=frame2,text='INVENTORY',command=inventory,image=inventoryimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom', font=('roboto',10))
    inventorybutton.place(x=995,y=43)

    stockbutton=ck.CTkButton(master=frame2,text='STOCK',command=stock,image=stockimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    stockbutton.place(x=995,y=178)

    billlbl=ck.CTkLabel(master=frame2,text='BILL',image=billimg,height=100,width=100,corner_radius=20,fg_color='green',text_color='white',compound='bottom')
    billlbl.place(x=995,y=313)

    salesbutton=ck.CTkButton(master=frame2,text='SALES',command=sales,image=salesimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    salesbutton.place(x=995,y=448)

#frame3------------------------------------------------------------------------------------------------------------------------------

    billinglbl=ck.CTkLabel(master=frame3,text='BILLING',text_color='white',font=('roboto',20))
    billinglbl.place(x=105,y=0)

    billingimglbl=ck.CTkLabel(master=frame3,image=billingimg,text='')
    billingimglbl.place(x=110,y=30)
    
    inventorydf= pd.read_csv('user data\\'+uname+'Inventory(2).csv', usecols=['Item_Name'])
    itemnamenamebilllst = inventorydf.to_numpy().tolist()
    
    lstbill=[]
    for i in itemnamenamebilllst:
        lstbill.append(i[0])

    
    # print(itemnamenamebilllst)
    itemnamedropdownbill=ck.CTkOptionMenu(master=frame3,values=lstbill,command=instocklabel)
    itemnamedropdownbill.place(x=50,y=125)

    itemnamelblbill=ck.CTkLabel(master=frame3,text='ITEM NAME',text_color='white',font=('roboto',12))
    itemnamelblbill.place(x=55,y=95)
    # itemnameentrybill=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,)
    # itemnameentrybill.place(x=39,y=125)

    itemcodelbl4=ck.CTkLabel(master=frame3,text='ITEM CODE(NUMBER)',text_color='white',font=('roboto',12))
    itemcodelbl4.place(x=55,y=165)
    # itemcodeentrybill=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # itemcodeentrybill.place(x=39,y=195)


    quantitylbl2=ck.CTkLabel(master=frame3,text='QUANTITY',text_color='white',font=('roboto',12))
    quantitylbl2.place(x=55,y=235)
    # quantityentrybill=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # quantityentrybill.place(x=39,y=265)

#clear bill funcn:===================================
    clear_billentry()

    addtobillbutton=ck.CTkButton(master=frame3,text='ADD TO BILL',command=addtobill,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    addtobillbutton.place(x=27,y=450)

    
    clearbutton=ck.CTkButton(master=frame3,text='CLEAR',command=clear_billentry,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    clearbutton.place(x=165,y=450)

    generatebill=ck.CTkButton(master=frame3,text='GENERATE BILL',command=Sales_generatebill,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',12))
    generatebill.place(x=27,y=500)
    # generatebill.bind("<ButtonRelease-1>",lambda: save_bill(bill_text.get('1.0', 'end')))

    savebillbutton=ck.CTkButton(master=frame3,text='SAVE BILL',command=lambda: save_bill(bill_text.get('1.0', 'end')),height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',12))
    savebillbutton.place(x=165,y=500)

#FRAME4-------------------------------------------------------------------------------------------------------------------------------

    removebutton=ck.CTkButton(master=frame4,text='REMOVE',command=remove,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    removebutton.place(x=27,y=500)

    clearbillbutton=ck.CTkButton(master=frame4,text='CLEAR BILL',command=clearbill,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    clearbillbutton.place(x=275,y=500)

    printbillbutton=ck.CTkButton(master=frame4,text='PRINT BILL',command=lambda: print_bill(bill_text.get('1.0', 'end')),height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    printbillbutton.place(x=510,y=500)

#bill textbox==-===-=-----====
    # billscroll = ck.CTkScrollbar(master=frame4,width=20,height=435,hover=True,fg_color='#504F4F') #504F4F
    # billscroll.place(x=602,y=65)
    bill_text=ck.CTkTextbox(master=frame4,width=600,height=450,font=('Times New Roman',20) )

    
    billlst=[]

    bill_text.insert('insert',"\t      Thank you for shopping from virtual bazaar\n ")

    bill_text.insert('insert',"\nItem Name\t ---- \tQuantity\t ---- \tRate(₹)\t ---- \tAmount(₹)\n")
    bill_text.insert('insert','--------------------------------------------------------------------------------------\n')
    


    bill_text.configure(state='disabled')
    bill_text.place(x=20,y=20) 

    

#SALES------------------------------------------------------------------------------------------------------------------------------------

def sales(a=None):
    def clear_sales():
        global salesnoentrysales,itemcodeentrysales,dateentrysales,itemnameentrysales,dateentrysales,datestringvarsales,itemcodestringvarsales,itemnamestringvarsales,quantitystringvarsales,salesnostringvarsales,profitsalesstringvar
        datestringvarsales=t.StringVar()
        dateentrysales=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=datestringvarsales)
        dateentrysales.place(x=39,y=125)

        itemcodestringvarsales=t.StringVar()
        itemcodeentrysales=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=itemcodestringvarsales)
        itemcodeentrysales.place(x=39,y=195)

        itemnamestringvarsales=t.StringVar()
        itemnameentrysales=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=itemnamestringvarsales)
        itemnameentrysales.place(x=39,y=265)

        quantitystringvarsales=t.StringVar()
        quantityentrysales=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=quantitystringvarsales)
        quantityentrysales.place(x=39,y=335)
        
        salesnostringvarsales=t.StringVar()
        salesnoentrysales=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,textvariable=salesnostringvarsales)
        salesnoentrysales.place(x=39,y=405)
        
        profitsalesstringvar=t.StringVar()
        profitsales=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20,
        textvariable=profitsalesstringvar)
        profitsales.place(x=39,y=475)

    def sales_treeview(a):
        global sales_tree,billdetails_text
        #treeview-----------------------------------------------------------------------------------------------------------------------------
        style=ttk.Style()
        # Add some style

        style.theme_use("clam")
        style.configure('Treeview',background='#5e6273',foreground='white',rowheight=40,fieldbackground='#5e6273',font=('Times New Roman',18))
        style.configure('Treeview.Heading',background='#5e6273',foreground='white',rowheight=45,fieldbackground='#5e6273',font=('Times New Roman',16))
        # Change selected color
        style.map('Treeview', 
        background=[('selected', '#34eb80')])
        #scrollbar
        salestree_scroll = ck.CTkScrollbar(master=frame4,width=15,height=291,hover=True,fg_color='#504F4F') #504F4F
        salestree_scroll.place(x=655,y=13)
        
        # setting treeview
        sales_tree = ttk.Treeview(frame4,selectmode='browse',yscrollcommand=salestree_scroll.set)
        salesdf= pd.read_csv('user data\\'+uname+'sales().csv')

        salestree_scroll.configure(command=sales_tree.yview)
            # Set up new treeview
        sales_list=list(salesdf.columns)
        sales_tree["column"] = sales_list
        # print(sales_list)
        sales_tree["show"] = "headings"
        sales_tree.column(sales_list[0],width=180,stretch=False,minwidth=150)
        sales_tree.column(sales_list[1],width=150,stretch=False,minwidth=150)
        sales_tree.column(sales_list[2],width=180,stretch=False,minwidth=150)
        sales_tree.column(sales_list[3],width=150,stretch=False,minwidth=150)
        sales_tree.column(sales_list[4],width=150,stretch=False,minwidth=150)
        sales_tree.column(sales_list[5],width=160,stretch=False,minwidth=150)
        # sales_tree.column(sales_list[6],width=150,stretch=False,minwidth=130)
        # Loop thru column list for headers
        for column in sales_tree["column"]:
            sales_tree.heading(column, text=column)

        # Put data in treeview
        salesdf_rows = salesdf.to_numpy().tolist()
        for row in salesdf_rows:
            sales_tree.insert("", "end", values=row)
        
        
        # Pack the treeview finally
        sales_tree.place(x=10,y=20)
        sales_tree.bind("<ButtonRelease-1>", sales_info)

        billdetails_text=ck.CTkTextbox(master=frame2,width=680,height=230,font=('Times New Roman',20) ,corner_radius=20)
        billdetails_text.configure(state='normal')
        billdetails_text.delete('1.0', 'end')

        billdetails_text.insert('insert','\t\t\tBill Details\n')
        billdetails_text.configure(state='disabled')
        billdetails_text.place(x=305,y=340)
        
    def search_sales():
        global sales_tree,itemcodeentrysales,itemnameentrysales,salesnoentrysales,S_Nsales
        #treeview-----------------------------------------------------------------------------------------------------------------------------
        style=ttk.Style()
        # Add some style

        style.theme_use("clam")
        style.configure('Treeview',
        background='#5e6273',foreground='white',rowheight=40,fieldbackground='#5e6273',font=('Times New Roman',18))
        style.configure('Treeview.Heading',background='#5e6273',foreground='white',rowheight=45,fieldbackground='#5e6273',font=('Times New Roman',16))
        # Change selected color
        style.map('Treeview', 
        background=[('selected', '#34eb80')])
        #scrollbar
        salestree_scroll = ck.CTkScrollbar(master=frame4,width=15,height=291,hover=True,fg_color='#504F4F') #504F4F
        salestree_scroll.place(x=655,y=13)
        
        # setting treeview
        sales_tree = ttk.Treeview(frame4,selectmode='browse',yscrollcommand=salestree_scroll.set)
        salesdf= pd.read_csv('user data\\'+uname+'sales().csv')
        I_Csales=itemcodeentrysales.get()
        I_Nsales=itemnameentrysales.get()
        S_Nsales=salesnoentrysales.get()
        if I_Nsales:
            salesdf=salesdf[salesdf['Item_Name']==I_Nsales]

        elif I_Csales:
            salesdf=salesdf[salesdf['Item_Code']==int(I_Csales)]

        elif S_Nsales:
            salesdf=salesdf[salesdf['Sales_no.']==int(S_Nsales)]
        
        salestree_scroll.configure(command=sales_tree.yview)
            # Set up new treeview
        sales_list=list(salesdf.columns)
        sales_tree["column"] = sales_list
        # print(sales_list)
        sales_tree["show"] = "headings"
        sales_tree.column(sales_list[0],width=180,stretch=False,minwidth=150)
        sales_tree.column(sales_list[1],width=150,stretch=False,minwidth=150)
        sales_tree.column(sales_list[2],width=180,stretch=False,minwidth=150)
        sales_tree.column(sales_list[3],width=150,stretch=False,minwidth=150)
        sales_tree.column(sales_list[4],width=150,stretch=False,minwidth=150)
        sales_tree.column(sales_list[5],width=160,stretch=False,minwidth=150)
        # sales_tree.column(sales_list[6],width=150,stretch=False,minwidth=130)
        # Loop thru column list for headers
        for column in sales_tree["column"]:
            sales_tree.heading(column, text=column)

        # Put data in treeview
        salesdf_rows = salesdf.to_numpy().tolist()
        for row in salesdf_rows:
            sales_tree.insert("", "end", values=row)
        
        
        # Pack the treeview finally
        sales_tree.place(x=10,y=20)
        sales_tree.bind("<ButtonRelease-1>", sales_info)
    
    def billdetails(a):
        global S_Nsales
        try:
            billdetails_text.configure(state='normal')
            billdetails_text.delete('1.0', 'end')
            billdetails_text.insert('insert','\t\t\tBill Details\n')
            fo=open('user data\\'+uname+'Bill no.'+S_Nsales+'.txt','r',encoding='utf-8')
            data=fo.read()
            billdetails_text.insert('insert',data)
            billdetails_text.configure(state='disabled')
            
        except FileNotFoundError:
            billdetails_text.configure(state='normal')
            billdetails_text.delete('1.0', 'end')
            billdetails_text.insert('insert','\t\t\tBill Details\n')
            billdetails_text.insert('insert','\t\tNO SUCH BILL FOUND IN SYSTEM\n')
            billdetails_text.configure(state='disabled')
            
    global root3,S_Nsales,billdetails_text
    frame1=ck.CTkFrame(master=root3,width=1100,height=55,corner_radius=0,fg_color='#282927')
    frame1.grid(row=0,column=0) #REMEMBER RELATIVITY
    frame2=ck.CTkFrame(master=root3,width=1100,height=575,corner_radius=0)
    frame2.grid(row=1,column=0)
    frame3=ck.CTkFrame(master=frame2,width=288,height=555,corner_radius=20) # agar corners rounded chahiye then use master= frame2
    frame3.place(x=10,y=15)
    frame4=ck.CTkFrame(master=frame2, width=680,height=320,corner_radius=20)
    frame4.place(x=305,y=15)

    lbl1=ck.CTkLabel(frame1,image=mangoimg,text='')
    lbl1.place(x=10,y=5)
    lbl2=ck.CTkLabel(frame1,image=accountimg,text='')
    lbl2.place(x=1040,y=5)
    
#frame1 buttons----------------------------------------------------------------------------------------------------------------------

    homebutton = ck.CTkButton(master=frame1,text='HOME',height=55,width=80,corner_radius=10,command = home,cursor='hand2',fg_color='#282927',text_color='white')
    homebutton.place(x=60,y=0)

    managelbl=ck.CTkLabel(master=frame1,text='MANAGE',height=55,width=80,corner_radius=10,fg_color='green',text_color='white')
    managelbl.place(x=140,y=0)

    analysebutton=ck.CTkButton(master=frame1,text='ANALYSE',height=55,width=80,corner_radius=10,command = analyse,cursor='hand2',fg_color='#282927',text_color='white')
    analysebutton.place(x=220,y=0)

    #settingsbutton=ck.CTkButton(master=frame1,text='SETTINGS',height=55,width=80,corner_radius=10,command = settings,cursor='hand2',fg_color='#282927',text_color='white')
    #settingsbutton.place(x=300,y=0)

    aboutbutton=ck.CTkButton(master=frame1,text='ABOUT',height=55,width=80,corner_radius=10,command = about,cursor='hand2',fg_color='#282927',text_color='white')
    aboutbutton.place(x=300,y=0)

#right side buttons----------------------------------------------------------------------------------------------------------------

    inventorybutton=ck.CTkButton(master=frame2,text='INVENTORY',command=inventory,image=inventoryimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom', font=('roboto',10))
    inventorybutton.place(x=995,y=43)

    stockbutton=ck.CTkButton(master=frame2,text='STOCK',command=stock,image=stockimg,height=100,width=100,corner_radius=20,cursor='hand2',fg_color='#5e6273',text_color='white',compound='bottom')
    stockbutton.place(x=995,y=178)

    billbutton=ck.CTkButton(master=frame2,text='BILL',command=bill,image=billimg,height=100,width=100,corner_radius=20,fg_color='#5e6273',cursor='hand2',text_color='white',compound='bottom')
    billbutton.place(x=995,y=313)

    saleslbl=ck.CTkLabel(master=frame2,text='SALES',image=salesimg,height=100,width=100,corner_radius=20,fg_color='green',text_color='white',compound='bottom')
    saleslbl.place(x=995,y=448)

#frame3------------------------------------------------------------------------------------------------------------------------------

    saleslbl=ck.CTkLabel(master=frame3,text='SALES',text_color='white',font=('roboto',20))
    saleslbl.place(x=110,y=0)

    salesrslbl=ck.CTkLabel(master=frame3,image=salesrsimg,text='')
    salesrslbl.place(x=110,y=30)

    datelblsales=ck.CTkLabel(master=frame3,text='DATE',text_color='white',font=('roboto',12))
    datelblsales.place(x=55,y=95)
    # salesnoentrysales=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # salesnoentrysales.place(x=39,y=125)

    itemcodelbl5=ck.CTkLabel(master=frame3,text='ITEM CODE(NUMBER)',text_color='white',font=('roboto',12))
    itemcodelbl5.place(x=55,y=165)
    # itemcodeentrysales=ck.CTkEntry(master=frame3,placeholder_text='Enter text here...',width=210,height=31,corner_radius=20)
    # itemcodeentrysales.place(x=39,y=195)


    itemnamelblsales=ck.CTkLabel(master=frame3,text='ITEM NAME',text_color='white',font=('roboto',12))
    itemnamelblsales.place(x=55,y=235)
    # itemnameentrysales=ck.CTkEntry(master=frame3,placeholder_text='YYYY-MM-DD',width=210,height=31,corner_radius=20)
    # itemnameentrysales.place(x=39,y=265)

    quantitylblsales=ck.CTkLabel(master=frame3,text='QUANTITY SOLD',text_color='white',font=('roboto',12))
    quantitylblsales.place(x=55,y=305)
    
    salesnolbl2=ck.CTkLabel(master=frame3,text='SALES NO.',text_color='white',font=('roboto',12))
    salesnolbl2.place(x=55,y=375)
    # dateentrysales=ck.CTkEntry(master=frame3,placeholder_text='YYYY-MM-DD',width=210,height=31,corner_radius=20)
    # dateentrysales.place(x=39,y=325)

    profitsaleslbl=ck.CTkLabel(master=frame3,text=' PROFIT',text_color='white',font=('roboto',12))
    profitsaleslbl.place(x=55,y=445)

    clear_sales()

    searchbutton=ck.CTkButton(master=frame3,text='SEARCH',command=search_sales,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    searchbutton.place(x=25,y=520)
    searchbutton.bind("<ButtonRelease-1>",billdetails)

    clearbutton=ck.CTkButton(master=frame3,text='CLEAR',command=clear_sales,height=33,width=100,corner_radius=20,cursor='hand2',text_color='black', font=('roboto',15))
    clearbutton.place(x=160,y=520)
    clearbutton.bind("<ButtonRelease-1>",sales_treeview)
#sales_treeview===========
    sales_treeview(1)

    


#bill_details===================
    billdetails_text=ck.CTkTextbox(master=frame2,width=680,height=230,font=('Times New Roman',20) ,corner_radius=20)
    billdetails_text.insert('insert','\t\t\tBill Details\n')
    billdetails_text.configure(state='disabled')
    billdetails_text.place(x=305,y=340)
    


def Stock_Entry(): ## when user clicks Add
# Valiables     : # - ItemName= I_N, - ItemCOde= I_C , - Quantity= Qu,  - Date= Date,
        global I_Cstock,I_Nstock,Qustock,todaydate
        I_Cstock=itemcodeentrystock.get()
        I_Nstock=itemnameentrystock.get()
        Qustock=int(quantityentrystock.get())
        todaydate= dt.date.today()
        stockdf=pd.read_csv('user data\\'+uname+'Stock_Entry.csv' , usecols=['SE_no.'])
        stock_lst=stockdf.to_numpy().tolist()
        # print(stock_lst)
        SE_no=stock_lst[-1][0] + 1

        SEdf= pd.DataFrame([[I_Cstock,I_Nstock,Qustock,todaydate,SE_no]])# Made a data frame of  Stock Entry(1 entry)
        # print(SEdf)
# append data frame to CSV file
        SEdf.to_csv('user data\\'+uname+'Stock_Entry.csv', mode='a', index=False, header=False)

        Inventory_Entry()

def Inventory_Entry():
    

    Item_Code= pd.read_csv('user data\\'+uname+'Inventory(2).csv', usecols= ['Item_Code']) 

    ItemCode= Item_Code.to_numpy() 

    # print(I_Cstock)
    
    

    for i in ItemCode:  #[44,66] # now to check if the item we are going to enter is already their or not
        
        """ Maybe if is not working """
        j=int(i[0])
        k=int(I_Cstock)
        # print(j,type(j))
        # print(k,type(k))
        if j == k: # Means the itemCode already exist so we ahve to just change the Quantity 
            df= pd.read_csv('user data\\'+uname+'Inventory(2).csv')
     
                    # **Replace values of columns by using DataFrame.loc[] property.
            # print(type(df.loc[df["Item_Code"] == I_Cstock, 'In_Stock'])) 
            # print(type(Qustock))
            # print(df.loc[df["Item_Code"] == I_Cstock, 'In_Stock'])
            df.loc[  df["Item_Code"] == k, "In_Stock"]= int(df[df['Item_Code']==k]['In_Stock']) + Qustock # **** VVVVVVV Important

            # df.loc[  df["Item_Code"] == k, "In_Stock"] +=  Qustock  ###Error in this line ** Do check if it works'+='
            df.to_csv('user data\\'+uname+'Inventory(2).csv', index = False)  ## * To write thed dataframe in the csv file   VVVVVVV Important

            break

    else: # ** Means the itemCode does not exist, So to append the data
    
            NE= pd.DataFrame([[I_Cstock,I_Nstock,Qustock]])
            NE.to_csv('user data\\'+uname+'Inventory(2).csv', mode='a', index=False, header=False)
            


def delete(): 

    SE=  pd.read_csv('user data\\'+uname+'Stock_Entry.csv') #user data/Stock_Entry (2).csv
    update_SE = SE.drop(SE[SE['Item_Code']== I_Cstock, SE['Item_Name']== I_Nstock, SE['Quantity']== Qustock])
    update_SE.to_csv('user data\\'+uname+'Stock_Entry.csv')
    


def Sales_generatebill():
    global bill_text,billlst,Sales_no
    totalbill=0
    salesdf2=pd.read_csv('user data\\'+uname+'sales().csv' , usecols=['Sales_no.'])   
    saleslst=salesdf2.to_numpy().tolist()
    Sales_no=saleslst[-1][0] + 1
    for i in billlst:  # i would be [todaydate,i_cbill,i_nbill,qubill,spbill,spbill*qubill] 
        totalbill+= i[5]
        Costdf = pd.read_csv('user data\\'+uname+'Cost.csv')
        cpbill=float(Costdf[Costdf['Item_Code']== i[1]]['Cost Price'] )
        profit_1unit= i[4] - cpbill
        grossprofit= profit_1unit * i[3]
        Salesdf= pd.DataFrame([i[0:4]+[Sales_no,grossprofit]]) 
        # print(Salesdf)

   # **append data frame to CSV file
        Salesdf.to_csv('user data\\'+uname+'sales().csv', mode='a', index=False, header=False)

        InventoryUpdate(i)    

   ## After sales table is updated the inventory should also be updated
    
    datentime=str(dt.datetime.today())
    datentimetuple=datentime.partition(' ')
    date=datentimetuple[0]
    timetuple=datentimetuple[2].partition('.')
    time=timetuple[0]
    bill_text.configure(state='normal')
    
    bill_text.insert('insert','Date: '+date + '\t\t\t\t\tTotal =  ₹ '+str(totalbill)+'\n' ) 
    bill_text.insert('insert','Time: '+time +'\n')
    bill_text.insert('insert','Bill no.(Sales no.): '+str(Sales_no)+'\n')
    bill_text.configure(state='disabled')

    
    

def save_bill(texts):
    global Sales_no
    file_name='user data\\'+uname+'Bill no.'+str(Sales_no)+'.txt' #for file path use \\ or raw string and don't use \\
    fo=open(file_name,'w+',encoding="utf-8")
    fo.write(texts)
    fo.close() 

def InventoryUpdate(a): # i = [I_N,I_C,Qu, Date]
    Item_Code= pd.read_csv('user data\\'+uname+'Inventory(2).csv', usecols= ['Item_Code']) 

    ItemCode= Item_Code.to_numpy()

    # for i in billlst:
    for j in ItemCode:
      if j == a[1]:  ##**change the Quantity 
        df= pd.read_csv('user data\\'+uname+'Inventory(2).csv')
        df.loc[df['Item_Code'] == int(a[1]) ,'In_Stock'] =int(df[df['Item_Code']==  int(a[1])]['In_Stock'])-a[3]   
        df.to_csv('user data\\'+uname+'Inventory(2).csv', index=False)


def Cost():
#variables ---## - ItemName= I_N, - ItemCOde= I_C , - CP=Cost Price, SP= Selling Price 
    I_Cstockcost=itemcodeentrystock_cost.get()
    I_Nstockcost=itemnameentrystock_cost.get()
    CPstockcost=float(costpriceentrystock_cost.get())
    SPstockcost=float(sellingpriceentrystock_cost.get())
    COdf= pd.DataFrame([[I_Cstockcost,I_Nstockcost,CPstockcost,SPstockcost]])
    COdf.to_csv('user data\\'+uname+'Cost.csv', mode='a', index=False, header=False)  # **append data frame to CSV file

def addtobill():
    global bill_text,billlst,billdropdowndata,todaydate

    Costdf = pd.read_csv('user data\\'+uname+'Cost.csv')
    bill_text.configure(state='normal')
    i_cbill=int(itemcodeentrybill.get())
    i_nbill=billdropdowndata
    qubill=int(quantityentrybill.get())
    spbill=float(Costdf[Costdf['Item_Code']== i_cbill]['Selling Price'] )
    #df.loc[  df["Item_Code"] == k, "In_Stock"]= int(df[df['Item_Code']==k]['In_Stock']) + Qustock
    # print(type(spbill))
    # print(spbill)
    todaydate=dt.date.today()
    record =[todaydate,i_cbill,i_nbill,qubill,spbill,spbill*qubill]   
    # print(record) 
    billlst.append(record)
    # print(billlst)
    bill_content="{}\t  -----  \t{}\t  -----  \t{}\t ---- \t{}\n".format(record[2],record[3],record[4],record[5])
    bill_text.insert('insert', bill_content)
    bill_text.insert('insert','-------------------------------------------------------------------------------------\n')
    bill_text.configure(state='disabled')

def clearbill():
    global billlst,bill_text
    bill_text.configure(state='normal')

    billlst=[]
    bill_text.delete('1.0', 'end')
    bill_text.insert('insert',"\t      Thank you for shopping from virtual bazaar\n ")

    bill_text.insert('insert',"\nItem Name\t ---- \tQuantity\t ---- \tRate(₹)\t ---- \tAmount(₹)\n")
    bill_text.insert('insert','--------------------------------------------------------------------------------------\n')
    bill_text.configure(state='disabled')

def remove():
    global billlst
    # print(billlst)
    if billlst!=[]:
        billlst.pop()
        bill_text.configure(state='normal')
        # print(billlst)
        bill_text.delete("end-2l","end-1l") 
        bill_text.delete("end-2l","end-1l")
        bill_text.configure(state='disabled')
        
    # print (billlst)  

def print_bill(txt):
    global Sales_no
    # print(txt,type(txt))
    file_name='user data\\'+uname+'Bill no.'+str(Sales_no)+'.txt' #for file path use \\ or raw string and don't use \\
    fo=open(file_name,'w+',encoding="utf-8")
    fo.write(txt)
    fo.close()
    os.startfile(file_name, 'print')
    
""" def save_bill(texts):
    global Sales_no
    # print(txt,type(txt))
    file_name='user data\\'+uname+'Bill no.'+str(Sales_no)+'.txt' #for file path use \\ or raw string and don't use \\
    fo=open(file_name,'w+',encoding="utf-8")
    fo.write(texts)
    fo.close()
 """
def dropdown1(i):
    global analysedropdown1 
    analysedropdown1=i

# def dropdown2(i):
#     global analysedropdown2 
#     analysedropdown2=i

def dropdown3(i):
    global analysedropdown3
    analysedropdown3=i

def dropdown4(i):
    global analysedropdown4
    analysedropdown4=i

# def dropdownbill(i):
#     global billdropdowndata
#     billdropdowndata=i


def graphfunction1():  #use only analysedropdown1
    global analysedropdown1,analysedropdown3,analysedropdown4, analyseframe4
    # print(analysedropdown1)
    
    FilterData= pd.read_csv('user data\\'+uname+'sales().csv').sort_values(by='Item_Name')
    # ff=pd.DataFrame(FilterData)
    # print(FilterData,type(FilterData),ff)
    FilterData['Date']= pd.to_datetime(FilterData['Date'])

# df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    # filterdf=  df.loc[(df['Date'] >= SD) and (df['Date'] < ED ')]

    df1= FilterData[["Quantity",'Item_Name']].groupby("Item_Name").sum()
    df3 = pd.read_csv('user data\\'+uname+'Cost.csv').sort_values(by='Item_Name')
    df4 =df3[['Selling Price','Item_Name']].groupby('Item_Name').sum()
    df2= FilterData[["Quantity",'Item_Name']].groupby("Item_Name").sum()
    check= pd.DataFrame(df2['Quantity']*df4['Selling Price'])
    df2=df2.join(check)
    dff= FilterData[["Quantity","Date"]].groupby("Date").sum()
    


    if fromanalyseentry1.get() and toanalyseentry1.get():
               # todaydate= dt.date.today()
        
        SD=fromanalyseentry1.get()
        ED=toanalyseentry1.get()
        
        # print(type(sd),type(npsd),a,type(b))
        

        # FilterData['date'] = pd.date_range('2017-1-1', periods=30, freq='D')
        # print(pd.date_range(SD,ED))
        FilterData = FilterData[FilterData["Date"].isin(pd.date_range(SD, ED))]
        # print(FilterData)
        df1= FilterData[["Quantity",'Item_Name']].groupby("Item_Name").sum()
        # FilterData = FilterData.loc[(f >= a) and (f <= b )]
    
    # else:
    #     pass
    

    if analysedropdown1 == 'Product Vs Quantity Sold(Bar Graph)':
        # print(FilterData)
        # plt.bar((FilterData["Item_Name"].unique()), df1['Quantity'] )
        # plt.show()

        fig = Figure(figsize=(9.5,7.5), dpi=100)    
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().bar((FilterData["Item_Name"].unique()), df1['Quantity'])    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)



        # Labelling Graohs 
        # plt.title('Product Vs Quantitiy Sold')
        # plt.xlabel('Product')
        # plt.ylabel('Quantity')

    elif analysedropdown1== 'Product Vs Quantity Sold(Pie Chart)':
        # df1.plot(kind='pie', y='Quantity' ,autopct='%1.0f%%') # Pie chart
        # plt.show()
        
        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().pie(df1['Quantity'], radius=1, labels=FilterData['Item_Name'].unique(),autopct='%0.2f%%', shadow=True,)    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)

    elif analysedropdown1 == 'Product Vs Sales(Bar Graph)':
        # plt.bar(FilterData['Item_Name'].unique(),check.dropna(axis=0)[0] )  # using dropna to remove if their is any NaN values 
        # plt.show()
        # Labeling


        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().bar(FilterData['Item_Name'].unique(),check.dropna(axis=0)[0] )    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)
        # plt.title('Product Vs Sales')
        # plt.xlabel('Product')
        # plt.ylabel('Sales')

    elif analysedropdown1 == 'Product Vs Sales(Pie Chart)':
        # df2.plot(kind='pie' , y= 0 , autopct='%1.0f%%')
        # plt.title('Product Contribution in Sales')
        # plt.show()

        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().pie(df2[0], radius=1, labels=FilterData['Item_Name'].unique(),autopct='%0.2f%%', shadow=True,)    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)
    
    elif analysedropdown1 == 'Sales Vs Time(Line Graph)':
        merged = pd.merge(FilterData[['Date','Item_Code','Quantity']],df3[["Selling Price", 'Cost Price','Item_Code']], on='Item_Code')
        merged['Sale']= merged['Quantity']*merged['Selling Price']


        mergedgroup =merged[['Date','Sale']].groupby(merged['Date']).sum()
        merged['Date'].unique()
        # plt.plot(FilterData['Date'].unique(), mergedgroup['Sale'], color='Red')
        # plt.bar(FilterData['Date'].unique(), mergedgroup['Sale'] , color='Black')
        # plt.show()
        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().plot(FilterData['Date'].unique(), mergedgroup['Sale'] , color='Black' )    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)



    elif analysedropdown1 == 'Sales Vs Time(Bar Graph)':
        merged = pd.merge(FilterData[['Date','Item_Code','Quantity']],df3[["Selling Price", 'Cost Price','Item_Code']], on='Item_Code')
        merged['Sale']= merged['Quantity']*merged['Selling Price']


        mergedgroup =merged[['Date','Sale']].groupby(merged['Date']).sum()
        merged['Date'].unique()
        # plt.plot(FilterData['Date'].unique(), mergedgroup['Sale'], color='Red')
        # plt.bar(FilterData['Date'].unique(), mergedgroup['Sale'] , color='Black')
        # plt.show()
        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().bar(FilterData['Date'].unique(), mergedgroup['Sale'] , color='Black' )    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)



    elif analysedropdown1 == 'Profit Made Vs Time(Bar Graph)':
        merged = pd.merge(FilterData[['Date','Item_Code','Quantity']],df3[["Selling Price", 'Cost Price','Item_Code']], on='Item_Code')
        merged['COST']= merged['Quantity']*merged['Cost Price']
        mergedgroup =merged[['Date','COST']].groupby(merged['Date']).sum()
        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().bar(FilterData['Date'].unique(), mergedgroup['COST'] , color='Black' )    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)

    elif analysedropdown1 == 'Profit Made Vs Time(Line Graph)':
        merged = pd.merge(FilterData[['Date','Item_Code','Quantity']],df3[["Selling Price", 'Cost Price','Item_Code']], on='Item_Code')
        merged['COST']= merged['Quantity']*merged['Cost Price']
        mergedgroup =merged[['Date','COST']].groupby(merged['Date']).sum()
        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().plot(FilterData['Date'].unique(), mergedgroup['COST'] , color='Black' )    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)


 
def graphfunction2(): #use analysedropdown3,analysedropdown4
    global analysedropdown3 , analysedropdown4
    FilterData= pd.read_csv('user data\\'+uname+'sales().csv').sort_values(by='Item_Name')
    FilterData['Date']= pd.to_datetime(FilterData['Date'])

    FilteredData2= FilterData[FilterData['Item_Name'] == analysedropdown4 ]
    Ds=FilteredData2[["Quantity","Date"]].groupby("Date").sum() ## ** Grouping data frame with date
    df3 = pd.read_csv('user data\\'+uname+'Cost.csv').sort_values(by='Item_Name')


    # **** Only for Products( Particular Products)
         # All together Function

    if fromanalyseentry2.get() and toanalyseentry2.get():
        SD=fromanalyseentry2.get()
        ED=toanalyseentry2.get()
        FilterData = FilterData[FilterData["Date"].isin(pd.date_range(SD, ED))]
        # print(FilterData)
        FilteredData2= FilterData[FilterData['Item_Name'] == analysedropdown4 ]
        Ds=FilteredData2[["Quantity","Date"]].groupby("Date").sum() ## ** Grouping data frame with date

        # FilteredData2 = FilteredData2.loc[(FilteredData2['Date'] >= SD) and (FilteredData2['Date'] <= ED )]
    
    else:
        pass

        
    if analysedropdown3 == 'Quantity Vs Time(Line Graph)': 

        # plt.plot(FilteredData2['Date'].unique(), Ds['Quantity'])
        # plt.title( analysedropdown4+' Quantity Sold Vs Time')
        # plt.xlabel('Date')
        # plt.ylabel('Sales')
        # plt.show()

        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().plot(FilteredData2['Date'].unique(), Ds['Quantity'] )    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)

    

    # **** Only for Products( Particular Products)
    if analysedropdown3 == 'Quantity Vs Time(Bar Graph)':  # ** Making data frame for soap(Particular Product) only
        
        # plt.bar(FilteredData2['Date'].unique(), Ds['Quantity'])
        # plt.title( analysedropdown4+' Quantity Sold Vs Time')
        # plt.xlabel('Date')
        # plt.ylabel('Sales')
        # plt.show()

        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().bar(FilteredData2['Date'].unique(), Ds['Quantity'])    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)


    # **** Only for Products( Particular Products)
    if analysedropdown3 == 'Sales Vs Time(Bar Graph)':

        s= (df3[df3['Item_Name']== str(analysedropdown4)]['Selling Price']).to_numpy()
    
        # plt.bar(FilteredData2['Date'].unique(), Ds['Quantity']*s)
        # plt.title(analysedropdown4 +' Sales Vs Time')
        # plt.xlabel('Date')
        # plt.ylabel('Sales')
        # plt.show()

        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().bar(FilteredData2['Date'].unique(), Ds['Quantity']*s)    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)


       # **** Only for Products( Particular Products)
    if analysedropdown3 == 'Sales Vs Time(Line Graph)':

        s= (df3[df3['Item_Name']== str(analysedropdown4) ]['Selling Price']).to_numpy()
    
        # plt.plot(FilteredData2['Date'].unique(), Ds['Quantity']*s)
        # plt.title(analysedropdown4 + ' Sales Vs Time')
        # plt.xlabel('Date')
        # plt.ylabel('Sales')
        # plt.show()

        fig = Figure(figsize=(9.5,7.5), dpi=100)
        canvas = FigureCanvasTkAgg( fig, master= analyseframe4)

        fig.add_subplot().plot(FilteredData2['Date'].unique(), Ds['Quantity']*s)    
        canvas.draw()
        canvas.get_tk_widget().place(x= 45 , y=50)


def inventory_info(a):
    global inventory_tree,itemcodestringvarinventory,itemnamestringvarinventory,instockstringvarinventory
    #getting selection------------
    
    selectioninventory=inventory_tree.focus()
    detailsinventory=inventory_tree.item(selectioninventory)
    itemcodestringvarinventory.set(detailsinventory['values'][0])
    # print(detailsinventory,a)
    itemnamestringvarinventory.set(detailsinventory['values'][1])
    instockstringvarinventory.set(detailsinventory['values'][2])


def stock_info(a):
    global stock_tree,itemcodestringvarstock,itemnamestringvarstock,quantitystringvarstock
    #getting selection------------
    
    selectionstock=stock_tree.focus()
    detailsstock=stock_tree.item(selectionstock)
    itemcodestringvarstock.set(detailsstock['values'][0])
    # print(detailsinventory,a)
    itemnamestringvarstock.set(detailsstock['values'][1])
    quantitystringvarstock.set(detailsstock['values'][2])

def cost_info(a):
    global stock_tree,itemcodestringvarcost,itemnamestringvarcost,costpricestringvarcost,sellingpricestringvarcost
    #getting selection------------
    
    selectioncost=cost_tree.focus()
    detailscost=cost_tree.item(selectioncost)
    itemcodestringvarcost.set(detailscost['values'][0])
    # print(detailsinventory,a)
    itemnamestringvarcost.set(detailscost['values'][1])
    costpricestringvarcost.set(detailscost['values'][2])
    sellingpricestringvarcost.set(detailscost['values'][3])

def sales_info(a):
    global sales_tree,datestringvarsales,itemcodestringvarsales,itemnamestringvarsales,quantitystringvarsales,salesnostringvarsales,profitsalesstringvar
    selectionsales=sales_tree.focus()
    detailssales=sales_tree.item(selectionsales)
    datestringvarsales.set(detailssales['values'][0])
    itemcodestringvarsales.set(detailssales['values'][1])
    itemnamestringvarsales.set(detailssales['values'][2])
    quantitystringvarsales.set(detailssales['values'][3])
    salesnostringvarsales.set(detailssales['values'][4])
    profitsalesstringvar.set(detailssales['values'][5])


def delete_cost():
    global itemcodeentrystock_cost,itemnameentrystock_cost
    I_Ccost=itemcodeentrystock_cost.get()
    I_Ncost=itemnameentrystock_cost.get()
    costdf=pd.read_csv('user data\\'+uname+'Cost.csv')
    # print(costdf)
    if I_Ncost:
        costdf.drop(costdf.index[(costdf["Item_Name"] == I_Ncost)],axis=0,inplace=True) #rewrite this dataframe to csv file
        costdf.to_csv('user data\\'+uname+'Cost.csv', mode='w', index=False, header=True)
    else:
        costdf.drop(costdf.index[(costdf["Item_Code"] == I_Ccost)],axis=0,inplace=True)
        costdf.to_csv('user data\\'+uname+'Cost.csv', mode='w', index=False, header=True)
    # print(costdf)

def update_cost():
    global itemcodeentrystock_cost,itemnameentrystock_cost,costpriceentrystock_cost,sellingpriceentrystock_cost
    I_Ccost=itemcodeentrystock_cost.get()
    I_Ncost=itemnameentrystock_cost.get()
    CPcost=costpriceentrystock_cost.get()
    SPcost=sellingpriceentrystock_cost.get()
    costdf=pd.read_csv('user data\\'+uname+'Cost.csv')
    stockdf=pd.read_csv('user data\\'+uname+'Stock_Entry.csv')
    inventorydf=pd.read_csv('user data\\'+uname+'Inventory(2).csv')
    # print(costdf)
    if I_Ncost and CPcost and SPcost:
        costdf.loc[costdf['Item_Name'] ==I_Ncost ,'Item_Code'] =int(I_Ccost)
        stockdf.loc[stockdf['Item_Name'] ==I_Ncost ,'Item_Code'] =int(I_Ccost)
        inventorydf.loc[inventorydf['Item_Name'] ==I_Ncost ,'Item_Code'] =int(I_Ccost)
        costdf.loc[costdf['Item_Name'] == I_Ncost,'Cost Price']=float(CPcost)
        costdf.loc[costdf['Item_Name'] == I_Ncost ,'Selling Price']=float(SPcost)

    if I_Ccost and CPcost and SPcost:
        costdf.loc[costdf['Item_Code'] == int(I_Ccost) ,'Item_Name'] =I_Ncost
        stockdf.loc[stockdf['Item_Code'] == int(I_Ccost) ,'Item_Name'] =I_Ncost
        inventorydf.loc[inventorydf['Item_Code'] == int(I_Ccost) ,'Item_Name'] =I_Ncost
        costdf.loc[costdf['Item_Code'] == int(I_Ccost) ,'Cost Price']=CPcost
        costdf.loc[costdf['Item_Code'] == int(I_Ccost) ,'Selling Price']=SPcost
    
    costdf.to_csv('user data\\'+uname+'Cost.csv', mode='w', index=False, header=True)
    stockdf.to_csv('user data\\'+uname+'Stock_Entry.csv',mode='w', index=False, header=True)
    inventorydf.to_csv('user data\\'+uname+'Inventory(2).csv',mode='w', index=False, header=True)

def delete_stock(): # create a unique stock entry no.
    global itemcodeentrystock,itemnameentrystock,stock_tree
    stockdf=pd.read_csv('user data\\'+uname+'Stock_Entry.csv')
    inventorydf=pd.read_csv('user data\\'+uname+'Inventory(2).csv')
    selectionstock=stock_tree.focus()
    detailsstock=stock_tree.item(selectionstock)
    se_no=detailsstock['values'][4]
    Qu= detailsstock['values'][2]
    I_C= detailsstock['values'][0]
    # print(se_no,type(se_no))
    



    stockdf.drop(stockdf.index[(stockdf["SE_no."] == se_no )],axis=0,inplace=True)
    # print(stockdf)

    inventorydf.loc[inventorydf['Item_Code'] == I_C ,'In_Stock'] =int(inventorydf[inventorydf['Item_Code']==I_C]['In_Stock'])-Qu 

    stockdf.to_csv('user data\\'+uname+'Stock_Entry.csv', mode='w', index=False, header=True)
    inventorydf.to_csv('user data\\'+uname+'Inventory(2).csv', mode='w', index=False, header=True)
        

    



def update_stock():
    global stock_tree,quantityentrystock
    Qu_entry=quantityentrystock.get()
    selectionstock=stock_tree.focus()
    detailsstock=stock_tree.item(selectionstock)
    se_no=detailsstock['values'][4]
    Qu_details= detailsstock['values'][2]
    I_C = detailsstock['values'][0]

    stockdf=pd.read_csv('user data\\'+uname+'Stock_Entry.csv')
    inventorydf=pd.read_csv('user data\\'+uname+'Inventory(2).csv')
    if Qu_entry :
        
        stockdf.loc[stockdf['SE_no.']== se_no, 'Quantity Bought'] = int(Qu_entry)
        Qu= int(Qu_entry)-Qu_details
        inventorydf.loc[inventorydf['Item_Code'] == I_C ,'In_Stock'] =int(inventorydf[inventorydf['Item_Code']==I_C]['In_Stock']) + Qu
        stockdf.to_csv('user data\\'+uname+'Stock_Entry.csv', mode = 'w' , index=False, header=True)
        inventorydf.to_csv('user data\\'+uname+'Inventory(2).csv', mode='w', index=False, header=True)



# optionmenu_1 = ck.CTkOptionMenu(master=root3,values=["Light", "Dark", "System"],command=change_appearance_mode)
# optionmenu_1.place(x=0,y=0)
manage()
root3.protocol("WM_DELETE_WINDOW", exitt)
root3.mainloop()
