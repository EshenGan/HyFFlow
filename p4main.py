from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import mankendall as mk1
from pandas import DataFrame
from matplotlib import pyplot as plt
import Export as ex
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import gridspec
import numpy as np
from statsmodels.formula.api import ols
import main as mn
import p2main as mn2
import p3main as mn3


df=DataFrame()
scancounter=0
scannum = 0
toggleCI = False

def package4(menuroot):
    menuroot.withdraw()
    root=Toplevel(menuroot)
    root.geometry("733x566")
    root.state('zoomed')
    def OpenFile():
        filename2 = filedialog.askopenfilename(initialdir="/",
                                          title="Select A ZIP",
                                          filetype=(("ZIP files", "*.zip"), ("RAR files","*.rar"),("all files", "*.*")))
        label2_file.configure(text=filename2)



    #code for uploading saved data file
    file_frame = LabelFrame(root, text="Open File")
    file_frame.place(height=800, width=310, x=0, y=0)

    label2_file =ttk.Label(file_frame, text="")
    label2_file.place(x=0, y=10)

    label3_file =ttk.Label(file_frame, text="")
    label3_file.place(x=0, y=50)
    #button for loading saved excel data
    button2 = Button(root, text="Load File", command=lambda:Load_excel_data())
    button2.place(x=100, y=0)
    
    #tabs
    my_notebook=ttk.Notebook(root)
    my_notebook.place(x=310,y=0, height=785, width=1230)
   
    #excel data frame 1
    frame1 = LabelFrame(my_notebook,bg='white')
    frame1.pack(fill="both", expand=1)

    my_notebook.add(frame1,text="Discharge")
    
    #hide tabs before importing 
    my_notebook.hide(0)

    # This is the Treeview Widget for frame 1
    tv1 = ttk.Treeview(frame1)  
    tv1.place(relheight=1,relwidth=1)

    treescrolly=Scrollbar(frame1,orient="vertical",command=tv1.yview)
    treescrollx=Scrollbar(frame1,orient="horizontal",command=tv1.xview)

    tv1.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")


    #function for loading excel data

    def  Load_excel_data():
    #if your file is valid this will load the file into the treeview
        file_path = label2_file["text"]
        global df 
        df=None
        try:
            
            #if filepath fpr discharge is not empty only load
            if file_path!="":
                excel_filename = r"{}".format(file_path)
                if excel_filename[-4:] == ".csv":
                    if scancounter==0:
                        df = pd.read_csv(excel_filename)
                else:
                    if scancounter==0:
                        df = pd.read_excel(excel_filename)


        except ValueError:
            messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            messagebox.showerror("Information", f"No such file as {file_path}")
            return None
        
        clear_data()

        #if Discharge is loaded
        if file_path !="":
            my_notebook.add(frame1,text="Discharge")
            my_notebook.select(0)
            tv1["column"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column) 

            df_rows = df.to_numpy().tolist() 
            for row in df_rows:
                tv1.insert("", "end", values=row) 
            
                         
    #################################################
    def clear_data():
        print("data")
        return None

    def ScanFile():

        file_path = label2_file["text"]
        global df
        global scannum
        global scancounter
        if scannum == 1:
            df = pd.read_excel(file_path)
            colname = df.columns[1]
            scancounter = 1

        NewWindow = Toplevel(root)
        NewWindow.title("HyFFlow")
        NewWindow.geometry("500x200")
        NewWindow.resizable(0, 0)

        if df.isnull().values.any():
            label_question = Label(NewWindow, text="Excel file contains NULL values, would you like to remove NULL values?")
            label_question.place(x=100, y=69)
            def RemoveNA():
                df[colname].replace('', np.nan, inplace = True)
                df.dropna(inplace = True)
                messagebox.showinfo("Information","NULL values removed, file is imported successfully")
                NewWindow.destroy()
            b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="white", font="bold", command=RemoveNA)
            b1.place(x=130, y=150)

            def NoRemove():
                messagebox.showinfo("Information","Please import another excel file without NULL values")
                NewWindow.destroy()
            b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="white", font="bold", command=NoRemove)
            b2.place(x=280, y=150)
        else:
            messagebox.showinfo("Information", "Excel file contains no error data, file imported successfully")
            NewWindow.destroy()


    def ImportDischarge():
        filename2=None
        filename2 = filedialog.askopenfilename(initialdir="/",
                                           title="Select A File",
                                           filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        label2_file.configure(text=filename2)
        if filename2!="":
            NewWindow = Toplevel(root)
            NewWindow.title("HyFFlow")
            NewWindow.geometry("500x200")
            NewWindow.resizable(0, 0)

            global scannum
            scannum = 1

            label_question = Label(NewWindow, text="Would you like to scan through the data in the Excel Sheet")
            label_question.place(x=100, y=69)

            b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="white", font="bold", command=ScanFile)
            b1.place(x=130, y=150)
            def Continue():
                messagebox.showinfo("Innformation","file is imported successfully ")
                NewWindow.destroy()
            b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="white", font="bold", command=Continue)
            b2.place(x=280, y=150)
    

    #function for switching package
    def function():
        print("Need to figure out function")

    #About
    def About():
        print(".......")

    # #Function for selecting visualization output
    # def Output():
    #     print("Need to figure out")
    # #Function for selecting
    # def All():
    #     print("Need to figure out")


    #Menu

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=filemenu)
    

    Importexcel_menu = Menu(filemenu, tearoff=0)
    Importexcel_menu.add_command(label="Discharge or Rainfall", command=ImportDischarge)

    filemenu.add_cascade(label="Select Excel", menu=Importexcel_menu)
    filemenu.add_command(label="Open Graph", command=OpenFile)
    #submenu for switching Menu
    Switchpackage_menu = Menu(filemenu, tearoff=0)
    Switchpackage_menu.add_command(label="Fundamentals of the Flow Regime", command=lambda:mn.package1(root))
    Switchpackage_menu.add_command(label="Flow Metrics", command=lambda:mn2.package2(root))
    Switchpackage_menu.add_command(label="Hyrograph Shape", command=lambda:mn3.package3(root))
    

    filemenu.add_cascade(label="Switch to other package", menu=Switchpackage_menu)


    filemenu.add_separator()
    def closepackage():
        root.destroy() 
        menuroot.deiconify()
    filemenu.add_command(label="Exit", command=closepackage)
    
    #Window Menu
    Windowmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Window", menu=Windowmenu)
    Windowmenu.add_command(label="About", command=About)


    #Analysis Menu
    Analysismenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Analysis", menu=Analysismenu)

    #SubMenu for selecting visualization
    Visualization_menu = Menu(Analysismenu, tearoff=0)

    Visualization_menu.add_checkbutton(label="Man-Kendall" , command=lambda:mk1.selectwinfunction(root,df))
    Analysismenu.add_cascade(label="Visualization", menu=Visualization_menu)






    #Help Menu
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About", command=About)

    def quit_me():
        root.destroy()
        menuroot.quit()
        
        

    root.protocol("WM_DELETE_WINDOW", quit_me)
