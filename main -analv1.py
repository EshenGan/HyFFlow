from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import analysis1 as ty
from pandas import DataFrame

root = Tk()
root.title("HyFFlow")
root.geometry("733x566")

def OpenFile():
    filename2 = filedialog.askopenfilename(initialdir="/",
                                          title="Select A ZIP",
                                          filetype=(("ZIP files", "*.zip"), ("RAR files","*.rar"),("all files", "*.*")))
    label2_file.configure(text=filename2)



#code for uploading saved data file
file_frame = LabelFrame(root, text="Open File")
file_frame.place(height=800, width=280, x=0, y=0)

label2_file =ttk.Label(file_frame, text="")
label2_file.place(x=0, y=0)
#button for loading saved excel data
button2 = Button(root, text="Load File", command=lambda: Load_excel_data())
button2.place(x=100, y=0)
#excel data frame
frame1 = LabelFrame(root, text="Excel Data")
frame1.place(height=800, width=1080 ,x=280,y=0)



tv1 = ttk.Treeview(frame1)  # This is the Treeview Widget
column_list_account = ["date/time", "rainfall station", "rainfall"]  # These are our headings
tv1['columns'] = column_list_account  # We assign the column list to the widgets columns
tv1["show"] = "headings"  # this hides the default column..

for column in column_list_account:  # foreach column
    tv1.heading(column, text=column)  # let the column heading = column name
    tv1.column(column, width=50)  # set the columns size to 50px
tv1.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).
treescroll = Scrollbar(frame1)  #  scrollbar
treescroll.configure(command=tv1.yview)  # make it vertical
tv1.configure(yscrollcommand=treescroll.set)  #scrollbar for the Treeview Widget
treescroll.pack(side="right", fill="y")  # scrollbar fill the yaxis of the Treeview widget








#function for loading excel data

def  Load_excel_data():
  #if your file is valid this will load the file into the treeview
  
    try:
        global df
        excel_filename = r"{}".format(label2_file['text'])
        df = pd.read_excel(excel_filename)


    except ValueError:
        messagebox.showerror("Information", "The File you have entered is invalid")
        return None

    df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row)  # inserts each list into the treeview
    


#If user will click on button yes ,it will ask for file name which u want for data cleaning 
#and then after giving file name it will generate new popup window for data cleaning
def File_Dialog():

    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
    label_file.configure(text=filename)
    



#it will open new window
def OpenNew():

            
            newWindow2=Toplevel(root)
            newWindow2.title("HyFFlow")
            newWindow2.geometry("500x230")
            newWindow2.resizable(0,0)
             
            

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


            



            
# function for importing file(after clicking import option it will generate popup window to ask question about data cleaning
def ImportFile():

          NewWindow=Toplevel(root)
          NewWindow.title("HyFFlow")
          NewWindow.geometry("500x200")
          NewWindow.resizable(0, 0)


          label_question=Label(NewWindow,text="Would you like to scan through the data in filename")
          label_question.place(x=100,y=69)


          b1=Button(NewWindow,text="Yes",height=1,width=7,bg="lightblue",fg="white",font="bold",command=OpenNew)
          b1.place(x=130,y=150)



          b2=Button(NewWindow,text="No",height=1,width=7,bg="lightblue",fg="white",font="bold" ,command=file)

          b2.place(x=280,y=150)


#If  user will click on button no ,it will ask for file name for importing
def file():
  filename3 = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))

  label2_file.configure(text=filename3)

def ImportExcel():
    filename2 = filedialog.askopenfilename(initialdir="/",
                                           title="Select A File",
                                           filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
    label2_file.configure(text=filename2)

    NewWindow = Toplevel(root)
    NewWindow.title("HyFFlow")
    NewWindow.geometry("500x200")
    NewWindow.resizable(0, 0)

    label_question = Label(NewWindow, text="Would you like to scan through the data in the Excel Sheet")
    label_question.place(x=100, y=69)

    b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="white", font="bold", command=OpenNew)
    b1.place(x=130, y=150)

    b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="white", font="bold", command=file)

    b2.place(x=280, y=150)




  


          
#function for exporting file
def ExportFile():
    print("Need to figure out")

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
filemenu.add_command(label="Open Graph", command=OpenFile)
filemenu.add_command(label="Import Excel",command=ImportExcel)

#submenu for switching Menu
Switchpackage_menu = Menu(filemenu, tearoff=0)
Switchpackage_menu.add_command(label="Fundamentals of the Flow Regime", command=function)
Switchpackage_menu.add_command(label="Flow Metrics", command=function)
Switchpackage_menu.add_command(label="Hyrograph Shape", command=function)
Switchpackage_menu.add_command(label="Long-term Trends on Flow and Rainfall Regimes", command=function)

filemenu.add_cascade(label="Switch to other package", menu=Switchpackage_menu)

filemenu.add_command(label="Export", command=ExportFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

#Window Menu
Windowmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Window", menu=Windowmenu)
Windowmenu.add_command(label="About", command=About)


#Analysis Menu
Analysismenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Analysis", menu=Analysismenu)

#SubMenu for selecting visualization
Visualization_menu = Menu(Analysismenu, tearoff=0)

Visualization_menu.add_checkbutton(label="Hydrograph and hyetrograph" , command=lambda:ty.hydroOnly(root,df))
Visualization_menu.add_checkbutton(label="Flow duration " , command=lambda:ty.flow_curve(root,df))
Visualization_menu.add_checkbutton(label="Flood frequency" ,  command=lambda:ty.flood_curve(root,df))
Visualization_menu.add_checkbutton(label="Median Discharge" ,  command=lambda:ty.medianDischarge(root,df))
Visualization_menu.add_checkbutton(label="Median RainFall" ,  command=lambda:ty.median_Rain(root,df))
Visualization_menu.add_checkbutton(label="Baseflow diagram" , command=Output)
Visualization_menu.add_checkbutton(label="Plots to show of flow seasonality" , command=Output)
Visualization_menu.add_checkbutton(label="Rainfall-runoff relations" , command=Output)
Visualization_menu.add_separator()
Visualization_menu.add_checkbutton(label="select all" , command=All)

Analysismenu.add_cascade(label="Visualization", menu=Visualization_menu)






#Help Menu
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)

def quit_me():

    root.quit()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", quit_me)
root.mainloop()