from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import analysis1 as ty
import anova as an
import hydrograph_baseflow as hb
from pandas import DataFrame
from matplotlib import pyplot as plt
import Export as ex
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import gridspec
import plotfunction as pf
import numpy as np
from statsmodels.formula.api import ols
import p2main as mn2
import p4main as mn4
import p3main as mn3







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
def package1(menuroot):
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
    button2 = Button(root, text="Load File", command=lambda: Load_excel_data())
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
        df=None
        df2=None
        try:
            
            #if filepath fpr discharge is not empty only load
            if file_path!="":
                excel_filename = r"{}".format(file_path)
                if excel_filename[-4:] == ".csv":
                    if scancounter1==0:
                        df = pd.read_csv(excel_filename)
                else:
                    if scancounter1==0:
                        df = pd.read_excel(excel_filename)
            #if filepath for rainfall is not empty only load
            if file_path2 !="":
                excel_filename2 = r"{}".format(file_path2)
            
                if excel_filename2[-4:] == ".csv":
                    if scancounter2==0:
                        df2 = pd.read_csv(excel_filename2)
                else:
                    if scancounter2==0:
                        df2 = pd.read_excel(excel_filename2)


        except ValueError:
            messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        clear_data()
        #this part need to change to tabbing
        #################################################
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
            
             
             
              
          
            
        #################################################
    def clear_data():
        print("data")
        return None






#it will open new window
    def OpenNew():

            
                newWindow2=Toplevel(root)
                newWindow2.title("HyFFlow")
                newWindow2.geometry("500x230")
                newWindow2.resizable(0,0)
                
                def File_Dialog():
                     filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
                     label_file.configure(text=filename)
                
            

                label_name=Label(newWindow2,text="File Name: ")
                label_name.place(x=10,y=50)



                file_frame=LabelFrame(newWindow2,bg='white')
                file_frame.place(height=30,width=378,x=10,y=69)


                label_file=Label(file_frame,text="",bg='white')
                label_file.place(x=0,y=0)

    
                b3=Button(newWindow2,text="Browse",height='1',width=7,bg='lightblue',fg='white',font="bold",command=File_Dialog)
                b3.place(x=393,y=69)
               
                
                    
                b4=Button(newWindow2,text="ok",height='1',width=7,bg='lightblue',fg='white',font="bold")
                b4.place(x=200,y=190)
               

    def ScanFile():

        file_path = label2_file["text"]
        file_path2 = label3_file["text"]
        global df
        global df2
        global scannum
        global scancounter1
        global scancounter2
        if scannum == 1:
            df = pd.read_excel(file_path)
            colname = df.columns[1]
            scancounter1=1
        elif scannum == 2:
            df2 = pd.read_excel(file_path2)
            df2 = pd.melt(df.reset_index(), value_vars = df2.columns.values)
            df2.columns = ['rainfallstations', 'rainfall']
            colname = df2.columns[1]
            scancounter2=1

        NewWindow = Toplevel(root)
        NewWindow.title("HyFFlow")
        NewWindow.geometry("500x200")
        NewWindow.resizable(0, 0)

        if df2.isnull().values.any():
            label_question = Label(NewWindow, text="Excel file contains NULL values, would you like to remove NULL values?")
            label_question.place(x=100, y=69)
            def RemoveNA():
                df2[colname].replace('', np.nan, inplace = True)
                df2.dropna(inplace = True)
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

            b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="white", font="bold", command=ScanFile)
            b1.place(x=130, y=150)
            def Continue():
                messagebox.showinfo("Innformation","file is imported successfully ")
                NewWindow.destroy()
            b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="white", font="bold", command=Continue)

            b2.place(x=280, y=150)




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
    





  


          
   #function for Exporing

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
            selectmedianRain(root, data2)

            # anovaa
        elif graphName == "anovaa":
            anovatable()
        elif graphName == "posthoc":
            posthoctable()
        elif graphName == "barchart":
            barcharttable()
        elif graphName == "baseflowdiagram":
            baseflowgraph()

        elif graphName == "hydrographbaseflow":
            hydrographbaseflow()
        elif graphName == "linearregression":
            linearregression()

        Top.destroy()

    def anovatable():

        an.anovaa(df2, root, True)

    def posthoctable():

        an.posthoc(df2, root,True)

    def barcharttable():

        an.barchart(df2, root, True)

    def baseflowgraph():

        hb.baseflowdiagram(df, root, True)
    def hydrographbaseflow():
        hb.hydrograph_baseflow(df, root, True)
    def linearregression():
        hb.linear_regression(df, df2, root, True)


    def selectmedianRain(root, data2):

        df = data2.copy()
        l = len(data2.columns) - 1
        Top2 = tk.Toplevel(root)
        var = tk.IntVar()
        var.set(0)

        tk.Radiobutton(Top2, text='all columns', variable=var, value=0).pack(anchor=tk.W)
        for i in range(l):
            b = i + 1
            tk.Radiobutton(Top2, text=data2.columns[i + 1], variable=var, value=b).pack(anchor=tk.W)

        def _continue():

            fig, ax = plt.subplots(figsize=(12, 6))
            Top = tk.Toplevel(root)
            canvas = FigureCanvasTkAgg(fig, master=Top)
            canvas.get_tk_widget()
            Top.withdraw()
            g = var.get()
            Top2.destroy()
            plt.clf()  # clear plot first
            pf.medianmonthRain(df, g)
            plt.savefig('Median RainFall.png')
            messagebox.showinfo("Innformation", "file is exported successfully ")

        tk.Button(Top2, text='OK', command=_continue).pack(anchor=tk.W)


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
        hb.linear_regression(df,df2,root,False)



    #function for switching package
    def function():
        print("Need to figure out function")

    #About
    def About():
        print(".......")

    #Function for selecting visualization output
    def Output():
        print("Need to figure out")
    #Function for selecting
    def All():
        print("Need to figure out")






    #Menu

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=filemenu)


    Importexcel_menu = Menu(filemenu, tearoff=0)
    Importexcel_menu.add_command(label="Discharge", command=ImportDischarge)
    Importexcel_menu.add_command(label="Rainfall", command=ImportRainfall)

    filemenu.add_cascade(label="Select Excel", menu=Importexcel_menu)
    filemenu.add_command(label="Open Graph", command=OpenFile)
    #submenu for switching Menu
    Switchpackage_menu = Menu(filemenu, tearoff=0)
    Switchpackage_menu.add_command(label="Flow Metrics", command=lambda:mn2.package2(root))
    Switchpackage_menu.add_command(label="Hyrograph Shape", command=lambda:mn3.package3(root))
    Switchpackage_menu.add_command(label="Long-term Trends on Flow and Rainfall Regimes", command=lambda:mn4.package4(root))

    filemenu.add_cascade(label="Switch to other package", menu=Switchpackage_menu)

    filemenu.add_command(label="Export", command=ExportFile)
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

    Visualization_menu.add_checkbutton(label="Hydrograph and hyetrograph" , command=lambda:callhydroanalyse())
    Visualization_menu.add_checkbutton(label="Flow duration " , command=lambda:flowduration())
    Visualization_menu.add_checkbutton(label="Flood frequency" ,  command=lambda:floodgraph())
    Visualization_menu.add_checkbutton(label="Median Discharge" ,  command=lambda:MedianDischarge())
    Visualization_menu.add_checkbutton(label="Median RainFall" ,  command=lambda:medianRain())
    Visualization_menu.add_checkbutton(label="Anova" ,  command=lambda: anovaa())
    Visualization_menu.add_checkbutton(label="Anova Post Hoc" ,  command=lambda:posthoc())
    Visualization_menu.add_checkbutton(label="Rainfallstations Mean Chart" ,  command=lambda:barchart())
    Visualization_menu.add_checkbutton(label="Baseflow diagram" , command= lambda:baseflowdiagram())
    Visualization_menu.add_checkbutton(label="Hydrograph with Baseflow" , command=lambda:hydrograph_baseflow())
    Visualization_menu.add_checkbutton(label="Plots to show of flow seasonality" , command=Output)
    Visualization_menu.add_checkbutton(label="Rainfall-runoff relations" , command=lambda:linear_regression())
    Visualization_menu.add_separator()
    Visualization_menu.add_checkbutton(label="select all" , command=All)

    Analysismenu.add_cascade(label="Visualization", menu=Visualization_menu)






    #Help Menu
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About", command=About)

    def quit_me():
        root.destroy()
        menuroot.quit()

    root.protocol("WM_DELETE_WINDOW", quit_me)
