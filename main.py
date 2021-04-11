from tkinter import *
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import plots4p1_window as ty
import anova as an
import hydrograph_baseflow as hb
from pandas import DataFrame
from matplotlib import pyplot as plt
import Export as ex
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import gridspec
import plots4p1 as pf
import numpy as np
import colwell4rainfall as c4r
import CI_window as c4d
import mkstationUI as mk
import iha as iha
import monthPca as mP


df=DataFrame()
df2=DataFrame()
scannum=0
scancounter1=0
scancounter2=0
togglehydro = False
toggleMD = False
toggleMR = False
toggleflood = False
toggleflow = False
toggleanovaa = False
toggleposthoc = False
togglebarchart = False
togglehydrographbf = False
toggleHB = False
toggleLR = False
toggleCIr = False
toggleCId = False
def loadpackages(loadroot):
    loadroot.withdraw()
    root=Toplevel(loadroot)
    root.geometry("733x566")
    root.iconbitmap('iconlogo.ico')
    root.state('zoomed')

    #code for uploading saved data file
    file_frame = LabelFrame(root, text="")
    file_frame.place(height=800, width=310, x=0, y=0)

    label2_file =ttk.Label(file_frame, text="")
    label2_file.place(x=0, y=30)

    label3_file =ttk.Label(file_frame, text="")
    label3_file.place(x=0, y=60)
    #button for loading saved excel data
    button2 = Button(root, text="Load File",bg="lightblue", fg="black",command=lambda: Load_excel_data())
    button2.place(x=100, y=0)
    
    #tabs
    my_notebook=ttk.Notebook(root)
    my_notebook.place(x=310,y=0, height=785, width=1230)
   
    #excel data frame 1
    frame1 = LabelFrame(my_notebook,bg='white')
    frame1.pack(fill="both", expand=1)
    
    #excel data frame 2`
    frame2 = LabelFrame(my_notebook,bg='white')
    frame2.pack(fill="both",expand=1)

    
    my_notebook.add(frame1,text="Discharge")
    my_notebook.add(frame2,text="Rainfall")
    
    
    #hide tabs before importing 
    my_notebook.hide(0)
    my_notebook.hide(1)
    

    # This is the Treeview Widget for frame 1
    tv1 = ttk.Treeview(frame1)  
    tv1.place(relheight=1,relwidth=1)

    treescrolly=Scrollbar(frame1,orient="vertical",command=tv1.yview)
    treescrollx=Scrollbar(frame1,orient="horizontal",command=tv1.xview)

    tv1.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")


    # This is the Treeview Widget for frame 2
    tv2 = ttk.Treeview(frame2)  
    tv2.place(relheight=1,relwidth=1)

    treescrolly=Scrollbar(frame2,orient="vertical",command=tv2.yview)
    treescrollx=Scrollbar(frame2,orient="horizontal",command=tv2.xview)

    tv2.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")

    #function for loading excel data

    def  Load_excel_data():
    #if your file is valid this will load the file into the treeview
        file_path = label2_file["text"]
        file_path2 = label3_file["text"]
        global df 
        global df2 
        global lg_df
        global lg_df2
        df=None
        df2=None
        try:
            
            #if filepath for discharge is not empty only load
            if file_path!="":
                excel_filename = r"{}".format(file_path)
                
                if excel_filename[-4:] == ".csv":
                    if scancounter1==1:
                        df = data_discharge
                        lg_df = pd.read_csv(excel_filename)
                    elif scancounter1==0:
                        df = pd.read_csv(excel_filename)
                        lg_df = pd.read_csv(excel_filename)    
                else:
                    if scancounter1==1:
                        df = data_discharge
                        lg_df = pd.read_excel(excel_filename)
                    elif scancounter1==0:
                        df = pd.read_excel(excel_filename) 
                        lg_df = pd.read_excel(excel_filename)
            #if filepath for rainfall is not empty only load
            if file_path2 !="":
                excel_filename2 = r"{}".format(file_path2)
                
                if excel_filename2[-4:] == ".csv":
                    if scancounter2==2:
                        df2 = data_rainfall
                        lg_df2 = pd.read_csv(excel_filename2)
                    elif scancounter2==0:
                        df2 = pd.read_csv(excel_filename2)
                        lg_df2 = pd.read_csv(excel_filename2) 
                else:
                    if scancounter2==2:
                        df2 = data_rainfall
                        lg_df2 = pd.read_excel(excel_filename2)
                    elif scancounter2==0:
                        df2 = pd.read_excel(excel_filename2)
                        lg_df2 = pd.read_excel(excel_filename2)


        except ValueError:
            messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        #if only rainfall load
        if file_path2 !="":
              my_notebook.add(frame2,text="Rainfall")
              my_notebook.select(1)
              tv2["column"] = list(df2.columns)
              tv2["show"] = "headings"
              for column in tv2["columns"]:
                  tv2.heading(column, text=column) 

              df_rows = df2.to_numpy().tolist() 
              for row in df_rows:
                  tv2.insert("", "end", values=row) 
               

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

    def ScanFile():

        file_path = label2_file["text"]
        file_path2 = label3_file["text"]
        global scannum
        global scancounter1
        global scancounter2
        global data_discharge
        global data_rainfall

        NewWindow = Toplevel(root)
        NewWindow.title("HyFFlow")
        NewWindow.geometry("500x200")
        NewWindow.resizable(0, 0)

        if scannum == 1:
            data_discharge = pd.read_excel(file_path)
            scancounter1 = 1
            if data_discharge.isnull().values.any():
                label_question = Label(NewWindow, text="Excel file contains NULL values, would you like to remove NULL values?")
                label_question.place(x=100, y=69)
                def RemoveNA():
                    data_discharge[data_discharge.columns].replace('', np.nan, inplace = True)
                    data_discharge.dropna(inplace = True)
                    messagebox.showinfo("Information","NULL values removed, file is imported successfully")
                    NewWindow.destroy()
                b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="white", font="bold", command=RemoveNA)
                b1.place(x=130, y=150)

                def NoRemove():
                    messagebox.showinfo("Information","File imported, NULL values in excel file ignored.")
                    NewWindow.destroy()
                b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="white", font="bold", command=NoRemove)
                b2.place(x=280, y=150)
            else:
                messagebox.showinfo("Information", "Excel file contains no error data, file imported successfully")
                NewWindow.destroy()
        elif scannum == 2:
            data_rainfall = pd.read_excel(file_path2)
            scancounter2 = 2
            if data_rainfall.isnull().values.any():
                label_question = Label(NewWindow, text="Excel file contains NULL values, would you like to remove NULL values?")
                label_question.place(x=100, y=69)
                def RemoveNA():
                    data_rainfall[data_rainfall.columns].replace('', np.nan, inplace = True)
                    data_rainfall.dropna(inplace = True)
                    messagebox.showinfo("Information","NULL values removed, file is imported successfully")
                    NewWindow.destroy()
                b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="white", font="bold", command=RemoveNA)
                b1.place(x=130, y=150)

                def NoRemove():
                    messagebox.showinfo("Information","File imported, NULL values in excel file ignored.")
                    NewWindow.destroy()
                b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="white", font="bold", command=NoRemove)
                b2.place(x=280, y=150)
            else:
                messagebox.showinfo("Information", "Excel file contains no error data, file imported successfully")
                NewWindow.destroy()


#importing the rainfall data
    def ImportRainfall():
        filename2=None
        filename2 = filedialog.askopenfilename(initialdir="/",
                                           title="Select A File",
                                           filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        label3_file.configure(text=filename2)
        if filename2!="":
            NewWindow = Toplevel(root)
            NewWindow.title("HyFFlow")
            NewWindow.geometry("500x200")
            NewWindow.resizable(0, 0)

            label_question = Label(NewWindow, text="Would you like to scan through the data in the Excel Sheet")
            label_question.place(x=100, y=69)

            global scannum
            scannum = 2

            def Continue_ScanFile():
                NewWindow.destroy()
                ScanFile()

            b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="black", font="bold", command=Continue_ScanFile)
            b1.place(x=130, y=150)
            def Continue():
                messagebox.showinfo("Innformation","file is imported successfully ")
                NewWindow.destroy()
            b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="black", font="bold", command=Continue)

            b2.place(x=280, y=150)



# importing the discharge data
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

            def Continue_ScanFile():
                NewWindow.destroy()
                ScanFile()

            b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="black", font="bold", command=Continue_ScanFile)
            b1.place(x=130, y=150)
            def Continue():
                messagebox.showinfo("Innformation","file is imported successfully ")
                NewWindow.destroy()
            b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="black", font="bold", command=Continue)
            b2.place(x=280, y=150)
    

   #function for Exptoring

    def allgraphs (root,data,data2,graphName):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        canvas = FigureCanvasTkAgg(fig, master=Top)
        canvas.get_tk_widget()
        Top.withdraw()
        df = data.copy()
        df2 = data2.copy()
        plt.clf()  # clear plot first
        g = gridspec.GridSpec(2, 1, height_ratios=[1, 2])

        if graphName == "hydrograph":
            pf.hydrograph(df, df2, g)
            plt.savefig('Hydrograph and hyetrograph.png')

        elif graphName == "flowduration":
            pf.flowplot(df)
            plt.savefig('Flow duration.png')

        elif graphName == "floodgraph":
            pf.floodcurve(data)
            plt.savefig('Flood frequency.png')
        elif graphName == "MedianDischarge":
            pf.medianmonthDis(df)
            plt.savefig('Median Discharge.png')

        elif graphName == "medianRain":
            ty.choosestation4median(root,data2)

        elif graphName == "anovaa":
            an.anovaa(df2, root, True)
        elif graphName == "posthoc":
            an.posthoc(df2, root,True)
        elif graphName == "barchart":
            an.barchart(df2, root, True)
        elif graphName == "baseflowdiagram":
            hb.baseflowdiagram(df, root, True)
        elif graphName == "hydrographbaseflow":
            hb.hydrograph_baseflow(df, root, True)
        elif graphName == "linearregression":
            hb.linear_regression(lg_df, lg_df2, root, True)
        # elif graphName == "Colwell Indices(Discharge)":
        #     c4d.CI_window(df,root,True)
        # elif graphName == "Colwell Indices(Rainfall)":
        #     c4r.selectwinfunction(df2,root,True)
        Top.destroy()
    #
    #
    # def anovatable():
    #
    #     an.anovaa(df2, root, True)
    #
    # def posthoctable():
    #
    #     an.posthoc(df2, root,True)
    #
    # def barcharttable():
    #
    #     an.barchart(df2, root, True)
    #
    # def baseflow_diagram():
    #     hb.baseflowdiagram(df, root, True)
    # def hydrographbaseflow():
    #     hb.hydrograph_baseflow(df, root, True)
    # def linearregression():
    #     hb.linear_regression(df, df2, root, True)


    # function for exporting file

    def ExportFile():
        x = True
        for graph in ex.getGraphs():
            allgraphs(root, df, df2,graph)
            if graph == "medianRain":
                x = False

        if x:
            messagebox.showinfo("Innformation", "file is exported successfully ")

    def callhydroanalyse():
        global togglehydro
        togglehydro = not togglehydro
        if togglehydro:
            ex.addNewGraph("hydrograph")
        else:
            ex.removeGraph("hydrograph")

        ty.hydro_graph(root, df, df2)

    def flowduration():
        global toggleflow
        toggleflow = not toggleflow
        if toggleflow:
            ex.addNewGraph("flowduration")
        else:
            ex.removeGraph("flowduration")
        ty.flow_curve(root, df)

    def floodgraph():
        global toggleflood
        toggleflood = not toggleflood
        if toggleflood:
            ex.addNewGraph("floodgraph")
        else:
            ex.removeGraph("floodgraph")
        ty.flood_curve(root,df)

    def MedianDischarge():
        global toggleMD
        toggleMD = not toggleMD
        if toggleMD:
            ex.addNewGraph("MedianDischarge")
        else:
            ex.removeGraph("MedianDischarge")
        ty.medianDischarge(root, df)

    def medianRain():
        global toggleMR
        toggleMR = not toggleMR
        if toggleMR:
            ex.addNewGraph("medianRain")
        else:
            ex.removeGraph("medianRain")
        ty.median_Rain(root, df2)

    def anovaa():
            global toggleanovaa
            toggleanovaa = not toggleanovaa
            if toggleanovaa:
                ex.addNewGraph("anovaa")
            else:
                ex.removeGraph("anovaa")
            an.anovaa(df2,root,False)

    def posthoc():
            global toggleposthoc
            toggleposthoc = not toggleposthoc
            if toggleposthoc:
                ex.addNewGraph("posthoc")
            else:
                ex.removeGraph("posthoc")
            an.posthoc(df2, root,False)

    def barchart():
            global togglebarchart
            togglebarchart = not togglebarchart
            if togglebarchart:
                ex.addNewGraph("barchart")
            else:
                ex.removeGraph("barchart")
            an.barchart(df2, root,False)

    def baseflowdiagram():
        global togglehydrographbf
        togglehydrographbf = not togglehydrographbf
        if togglehydrographbf:
            ex.addNewGraph("baseflowdiagram")
        else:
            ex.removeGraph("baseflowdiagram")
        hb.baseflowdiagram(df, root, False)

    def hydrograph_baseflow():
        global toggleHB
        toggleHB = not toggleHB
        if toggleHB:
            ex.addNewGraph("hydrographbaseflow")
        else:
            ex.removeGraph("hydrographbaseflow")
        hb.hydrograph_baseflow(df, root, False)

    def linear_regression():
        global toggleLR
        toggleLR = not toggleLR
        if toggleLR:
            ex.addNewGraph("linearregression")
        else:
            ex.removeGraph("linearregression")
        hb.linear_regression(lg_df,lg_df2,root,False)

    # def colwell4rainfall():
    #     global toggleCIr
    #     toggleCIr = not toggleCIr
    #     if toggleCIr:
    #         ex.addNewGraph("Colwell Indices(Rainfall)")
    #     else:
    #         ex.removeGraph("Colwell Indices(Rainfall)")
    #     c4r.selectwinfunction(df2, root, False)
    #
    # def colwell4discharge():
    #     global toggleCId
    #     toggleCId = not toggleCId
    #     if toggleCId:
    #         ex.addNewGraph("Colwell Indices(Discharge)")
    #     else:
    #         ex.removeGraph("Colwell Indices(Discharge)")
    #     c4d.CI_window(df,root,False)
    #
    # def mankendalltest():
    #     global togglemk
    #     togglemk = not togglemk
    #     if togglemk:
    #         ex.addNewGraph("Man-Kendall Test")
    #     else:
    #         ex.removeGraph("Man-Kendall Test")
    #     mk.choosestation(df2,root)

    #About
    def About():
        print(".......")

    #Toolbar menu
    menu = Menu(root)
    root.config(menu=menu)

    def closepackage():
        root.destroy()
        loadroot.deiconify()
    #'File'
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=filemenu)
    Importexcel_menu = Menu(filemenu, tearoff=0)
    Importexcel_menu.add_command(label="Discharge", command=ImportDischarge)
    Importexcel_menu.add_command(label="Rainfall", command=ImportRainfall)
    filemenu.add_cascade(label="Select Excel", menu=Importexcel_menu)
    filemenu.add_command(label="Export", command=ExportFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=closepackage)


    #'Package 1'
    p1_analysis = Menu(menu, tearoff=0)
    menu.add_cascade(label="Package 1", menu=p1_analysis)
    
    #submenu for analysis p1
    p1menu = Menu(p1_analysis, tearoff=0)
    p1_analysis.add_cascade(label="Fundamentals of the Flow Regime", menu=p1menu)

    #drop down list of analyses p1
    p1menu.add_checkbutton(label="Hydrograph and hyetrograph", command=lambda:callhydroanalyse())
    p1menu.add_checkbutton(label="Flow duration ", command=lambda:flowduration())
    p1menu.add_checkbutton(label="Flood frequency",  command=lambda:floodgraph())
    p1menu.add_checkbutton(label="Median Discharge",  command=lambda:MedianDischarge())
    p1menu.add_checkbutton(label="Median RainFall",  command=lambda:medianRain())
    p1menu.add_checkbutton(label="Anova",  command=lambda: anovaa())
    p1menu.add_checkbutton(label="Anova Post Hoc",  command=lambda:posthoc())
    p1menu.add_checkbutton(label="Rainfallstations Mean Chart",  command=lambda:barchart())
    p1menu.add_checkbutton(label="Baseflow diagram", command=lambda:baseflowdiagram())
    p1menu.add_checkbutton(label="Hydrograph with Baseflow", command=lambda:hydrograph_baseflow())
    p1menu.add_checkbutton(label="Rainfall-runoff relations", command=lambda:linear_regression())

   



    
    #'Package 2'
    p2_analysis = Menu(menu, tearoff=0)
    menu.add_cascade(label="Package 2", menu=p2_analysis)


    #submenu for analyses p2
    p2menu = Menu(p2_analysis, tearoff=0)
    p2_analysis.add_cascade(label="Flow Metrics", menu=p2menu)

    #drop down list of analyses p2
    p2menu.add_checkbutton(label="Colwell's Indices(Rainfall)", command=lambda:c4r.selectwinfunction(df2,root))
    p2menu.add_checkbutton(label="Colwell's Indices(Discharge) ", command=lambda:c4d.CI_window(df,root))
    p2menu.add_checkbutton(label="IHA", command=lambda : iha.OpenIHA())

   




    #'Package 3'
    p3_analysis = Menu(menu, tearoff=0)
    menu.add_cascade(label="Package 3", menu=p3_analysis)

    #submenu for analysis p3
    p3menu = Menu(p3_analysis, tearoff=0)
    p3_analysis.add_cascade(label="Flow Metrics", menu=p3menu)

    #Drop down list for analyses p3
    p3menu.add_checkbutton(label="PCA & AHC", command=lambda:mP.monthPca(root,df))




    #'Package 4'
    p4_analysis = Menu(menu, tearoff=0)
    menu.add_cascade(label="Package 4", menu=p4_analysis)

    #submenu for analysis p3
    p4menu = Menu(p4_analysis, tearoff=0)
    p4_analysis.add_cascade(label="Long-term Trends on Flow and Rainfall Regimes", menu=p4menu)

    #Dropdown list for analyses p4
    p4menu.add_checkbutton(label="Classic man-kendall Test", command=lambda:mk.choosestation(root,df2))



    #Help Menu
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="User Manual/User Guide", command=About)

    def quit_me():
        root.destroy()
        loadroot.quit()

    root.protocol("WM_DELETE_WINDOW", quit_me)
