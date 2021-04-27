import pandas as pd
import plots4p1_window as ty
import anova as an
import hydrograph_baseflow as hb
import numpy as np
import colwell4rainfall as c4r
import CI_window as C4d
import mkstationUI as Mk
import iha as iha
import PCA_AHC_UI as Pau
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from pandas import DataFrame
import usermanual as um
import ntpath

df = DataFrame()
df2 = DataFrame()
lg_df = DataFrame()
lg_df2 = DataFrame()
scannum = 0
scancounter1 = 0
scancounter2 = 0

filename2=""
filename1=""
def loadpackages(loadroot):
    loadroot.withdraw()
    root = Toplevel(loadroot)
    root.geometry("733x566")
    root.state('zoomed')

    # code for uploading saved data file
    file_frame = LabelFrame(root, text="")
    file_frame.place(height=800, width=310, x=0, y=0)

    label2_file = ttk.Label(file_frame, text="")
    label2_file.place(x=0, y=30)

    label3_file = ttk.Label(file_frame, text="")
    label3_file.place(x=0, y=60)
    



    # tabs
    my_notebook = ttk.Notebook(root)
    my_notebook.place(x=310, y=0, height=785, width=1230)
   
    # excel data frame 1
    frame1 = LabelFrame(my_notebook, bg='white')
    frame1.pack(fill="both", expand=1)
    
    # excel data frame 2`
    frame2 = LabelFrame(my_notebook, bg='white')
    frame2.pack(fill="both", expand=1)
    my_notebook.add(frame1, text="Discharge")
    my_notebook.add(frame2, text="Rainfall")

    # hide tabs before importing
    my_notebook.hide(0)
    my_notebook.hide(1)

    # This is the Treeview Widget for frame 1
    tv1 = ttk.Treeview(frame1)  
    tv1.place(relheight=1, relwidth=1)

    treescrolly = Scrollbar(frame1, orient="vertical", command=tv1.yview)
    treescrollx = Scrollbar(frame1, orient="horizontal", command=tv1.xview)
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom", fill="x")
    treescrolly.pack(side="right", fill="y")

    # This is the Treeview Widget for frame 2
    tv2 = ttk.Treeview(frame2)  
    tv2.place(relheight=1, relwidth=1)

    treescrolly = Scrollbar(frame2, orient="vertical", command=tv2.yview)
    treescrollx = Scrollbar(frame2, orient="horizontal", command=tv2.xview)

    tv2.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom", fill="x")
    treescrolly.pack(side="right", fill="y")

    # function for loading excel data

    def load_excel_data():
        # if your file is valid this will load the file into the treeview
        file_path = filename1
        file_path2 = filename2

        global df 
        global df2 
        global lg_df
        global lg_df2
        df = None
        df2 = None
        try:
            
            # if filepath for discharge is not empty only load
            if file_path != "":
                excel_filename = r"{}".format(file_path)
                
                if excel_filename[-4:] == ".csv":
                    if scancounter1 == 1:
                        df = data_discharge
                        lg_df = pd.read_csv(excel_filename)
                    elif scancounter1 == 0:
                        df = pd.read_csv(excel_filename)
                        lg_df = pd.read_csv(excel_filename)    
                else:
                    if scancounter1 == 1:
                        df = data_discharge
                        lg_df = pd.read_excel(excel_filename)
                    elif scancounter1 == 0:
                        df = pd.read_excel(excel_filename) 
                        lg_df = pd.read_excel(excel_filename)
            # if filepath for rainfall is not empty only load
            if file_path2 != "":
                excel_filename2 = r"{}".format(file_path2)
                
                if excel_filename2[-4:] == ".csv":
                    if scancounter2 == 2:
                        df2 = data_rainfall
                        lg_df2 = pd.read_csv(excel_filename2)
                    elif scancounter2 == 0:
                        df2 = pd.read_csv(excel_filename2)
                        lg_df2 = pd.read_csv(excel_filename2) 
                else:
                    if scancounter2 == 2:
                        df2 = data_rainfall
                        lg_df2 = pd.read_excel(excel_filename2)
                    elif scancounter2 == 0:
                        df2 = pd.read_excel(excel_filename2)
                        lg_df2 = pd.read_excel(excel_filename2)

        except ValueError:
            messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        # if only rainfall load
        if file_path2 != "":
            for i in tv2.get_children():
                tv2.delete(i)
            my_notebook.add(frame2, text="Rainfall")
            my_notebook.select(1)
            tv2["column"] = list(df2.columns)
            tv2["show"] = "headings"
            for column in tv2["columns"]:
                tv2.heading(column, text=column)

            df_rows = df2.to_numpy().tolist()
            for row in df_rows:
                tv2.insert("", "end", values=row)

        # if Discharge is loaded
        
        if file_path != "":
            for i in tv1.get_children():
                tv1.delete(i)
            my_notebook.add(frame1, text="Discharge")
            my_notebook.select(0)
            tv1["column"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column) 

            df_rows = df.to_numpy().tolist() 
            for row in df_rows:
                tv1.insert("", "end", values=row)

    def scanfile():

        file_path = filename1
        file_path2 = filename2

        global scannum
        global scancounter1
        global scancounter2
        global data_discharge
        global data_rainfall

        newwindow = Toplevel(root)
        newwindow.title("HyFFlow")
        newwindow.geometry("500x200")
        newwindow.resizable(0, 0)

        if scannum == 1:
            data_discharge = pd.read_excel(file_path)
            scancounter1 = 1
            if data_discharge.isnull().values.any():
                label_question = Label(newwindow,
                                       text="Excel file contains NULL values, would you like to remove NULL values?")
                label_question.place(x=100, y=69)

                def remove_na():
                    data_discharge[data_discharge.columns].replace('', np.nan, inplace=True)
                    data_discharge.dropna(inplace=True)
                    messagebox.showinfo("Information", "NULL values removed, file is imported successfully")
                    newwindow.destroy()
                    load_excel_data()

                b1 = Button(newwindow, text="Yes", height=1, width=7, bg="lightblue", fg="black", font="bold",
                            command=remove_na)
                b1.place(x=130, y=150)

                def no_remove():
                    messagebox.showinfo("Information", "File imported, NULL values in excel file ignored.")
                    newwindow.destroy()
                    load_excel_data()

                b2 = Button(newwindow, text="No", height=1, width=7, bg="lightblue", fg="black", font="bold",
                            command=no_remove)
                b2.place(x=280, y=150)
            else:
                messagebox.showinfo("Information", "Excel file contains no error data, file imported successfully")
                load_excel_data()
                newwindow.destroy()
        elif scannum == 2:
            data_rainfall = pd.read_excel(file_path2)
            scancounter2 = 2
            if data_rainfall.isnull().values.any():
                label_question = Label(newwindow,
                                       text="Excel file contains NULL values, would you like to remove NULL values?")
                label_question.place(x=100, y=69)

                def remove_na():
                    data_rainfall[data_rainfall.columns].replace('', np.nan, inplace=True)
                    data_rainfall.dropna(inplace=True)
                    messagebox.showinfo("Information", "NULL values removed, file is imported successfully")
                    newwindow.destroy()
                    load_excel_data()

                b1 = Button(newwindow, text="Yes", height=1, width=7, bg="lightblue", fg="black", font="bold",
                            command=remove_na)
                b1.place(x=130, y=150)

                def no_remove():
                    messagebox.showinfo("Information", "File imported, NULL values in excel file ignored.")
                    newwindow.destroy()
                    load_excel_data()

                b2 = Button(newwindow, text="No", height=1, width=7, bg="lightblue", fg="black", font="bold",
                            command=no_remove)
                b2.place(x=280, y=150)
            else:
                messagebox.showinfo("Information", "Excel file contains no error data, file imported successfully")
                load_excel_data()
                newwindow.destroy()

    # importing the rainfall data
    def import_rainfall():
        global filename2
        filename2=""
        filename2 = filedialog.askopenfilename(initialdir="/",
                                               title="Select A File",
                                               filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        label3_file.configure(text=ntpath.basename(filename2))
        if filename2 != "":
            newwindow = Toplevel(root)
            newwindow.title("HyFFlow")
            newwindow.geometry("500x200")
            newwindow.resizable(0, 0)

            label_question = Label(newwindow, text="Would you like to scan through the data in the Excel Sheet")
            label_question.place(x=100, y=69)

            global scannum
            scannum = 2

            def continue_scan_file():
                newwindow.destroy()
                scanfile()

            b1 = Button(newwindow, text="Yes", height=1, width=7, bg="lightblue", fg="black", font="bold",
                        command=continue_scan_file)
            b1.place(x=130, y=150)

            def _continue():
                messagebox.showinfo("Innformation", "file is imported successfully ")
                newwindow.destroy()
                load_excel_data()

            b2 = Button(newwindow, text="No", height=1, width=7, bg="lightblue", fg="black", font="bold",
                        command=_continue)

            b2.place(x=280, y=150)

    # importing the discharge data
    def import_discharge():
        global filename1
        filename1=""
        filename1 = filedialog.askopenfilename(initialdir="/",
                                               title="Select A File",
                                               filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        label2_file.configure(text=ntpath.basename(filename1))
        if filename1 != "":
            newwindow = Toplevel(root)
            newwindow.title("HyFFlow")
            newwindow.geometry("500x200")
            newwindow.resizable(0, 0)

            global scannum
            scannum = 1

            label_question = Label(newwindow, text="Would you like to scan through the data in the Excel Sheet")
            label_question.place(x=100, y=69)

            def continue_scan_file():
                newwindow.destroy()
                scanfile()

            b1 = Button(newwindow, text="Yes", height=1, width=7, bg="lightblue", fg="black", font="bold",
                        command=continue_scan_file)
            b1.place(x=130, y=150)

            def _continue():
                messagebox.showinfo("Innformation", "file is imported successfully ")
                newwindow.destroy()
                load_excel_data()

            b2 = Button(newwindow, text="No", height=1, width=7, bg="lightblue", fg="black", font="bold",
                        command=_continue)
            b2.place(x=280, y=150)

    # Toolbar menu
    menu = Menu(root)
    root.config(menu=menu)

    def closepackage():
        root.destroy()
        loadroot.deiconify()
    # 'File'
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=filemenu)
    importexcel_menu = Menu(filemenu, tearoff=0)
    importexcel_menu.add_command(label="Discharge", command=import_discharge)
    importexcel_menu.add_command(label="Rainfall", command=import_rainfall)
    filemenu.add_cascade(label="Select Excel", menu=importexcel_menu)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=closepackage)

    # 'Package 1'
    p1_analysis = Menu(menu, tearoff=0)
    menu.add_cascade(label="Package 1", menu=p1_analysis)
    
    # submenu for analysis p1
    p1menu = Menu(p1_analysis, tearoff=0)
    p1_analysis.add_cascade(label="Fundamentals of the Flow Regime", menu=p1menu)

    # drop down list of analyses p1
    p1menu.add_checkbutton(label="Hydrograph and hyetrograph", command=lambda: ty.hydro_graph(root, df, df2))
    p1menu.add_checkbutton(label="Flow duration ", command=lambda: ty.flow_curve(root, df))
    p1menu.add_checkbutton(label="Flood frequency",  command=lambda: ty.flood_curve(root, df))
    p1menu.add_checkbutton(label="Median Discharge",  command=lambda: ty.medianDischarge(root, df))
    p1menu.add_checkbutton(label="Median RainFall",  command=lambda: ty.median_Rain(root, df2))
    p1menu.add_checkbutton(label="Anova",  command=lambda: an.anovaa(df2, root))
    p1menu.add_checkbutton(label="Anova Post Hoc",  command=lambda: an.posthoc(df2, root))
    p1menu.add_checkbutton(label="Rainfallstations Mean Chart",  command=lambda: an.barchart(df2, root))
    p1menu.add_checkbutton(label="Baseflow diagram", command=lambda: hb.baseflowdiagram(df, root))
    p1menu.add_checkbutton(label="Hydrograph with Baseflow", command=lambda: hb.hydrograph_baseflow(df, root))
    p1menu.add_checkbutton(label="Rainfall-runoff relations", command=lambda: hb.linear_regression(lg_df, lg_df2, root))

    # 'Package 2'
    p2_analysis = Menu(menu, tearoff=0)
    menu.add_cascade(label="Package 2", menu=p2_analysis)

    # submenu for analyses p2
    p2menu = Menu(p2_analysis, tearoff=0)
    p2_analysis.add_cascade(label="Flow Metrics", menu=p2menu)

    # drop down list of analyses p2
    p2menu.add_checkbutton(label="Colwell's Indices(Rainfall)", command=lambda: c4r.selectwinfunction(df2, root,1))
    p2menu.add_checkbutton(label="Colwell's Indices(Discharge) ", command=lambda: C4d.ci_window(df, root,2))
    p2menu.add_checkbutton(label="IHA", command=lambda: iha.openiha())

    # 'Package 3'
    p3_analysis = Menu(menu, tearoff=0)
    menu.add_cascade(label="Package 3", menu=p3_analysis)

    # submenu for analysis p3
    p3menu = Menu(p3_analysis, tearoff=0)
    p3_analysis.add_cascade(label="Hydrograph Shape", menu=p3menu)

    # Drop down list for analyses p3
    p3menu.add_checkbutton(label="PCA & AHC", command=lambda: Pau.pca_ahc_ui(root, df))

    # 'Package 4'
    p4_analysis = Menu(menu, tearoff=0)
    menu.add_cascade(label="Package 4", menu=p4_analysis)

    # submenu for analysis p4
    p4menu = Menu(p4_analysis, tearoff=0)
    p4_analysis.add_cascade(label="Long-term Trends on Flow and Rainfall Regimes", menu=p4menu)

    # Dropdown list for analyses p4
    p4menu.add_checkbutton(label="Classic man-kendall Test", command=lambda: Mk.choosestation(root, df2))

    # Help Menu
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="User Manual/User Guide", command=lambda: um.openguide(loadroot))

    def quit_me():
        root.destroy()
        loadroot.quit()

    root.protocol("WM_DELETE_WINDOW", quit_me)
