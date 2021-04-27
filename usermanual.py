from tkinter import *
from PIL import ImageTk,Image
import main as mn




def openguide(loadroot):
    loadroot.withdraw()
    root = Toplevel(loadroot)
    root.geometry("1300x800")
    root.resizable(0, 0)

    can1 = Canvas(root, width = 400, height = 400)
    can1.pack()
    img1 = ImageTk.PhotoImage(Image.open("selectfile.png"))
    can1.place(x=0,y=30)
    seltxt=Label(root, text="NO 1. Under the file tab, go to 'select file' option and \n choose  the data type you want to import", fg='black', font=("Times new roman", 12))
    seltxt.place(x=60, y=250)
    can1.create_image(0, 0, anchor=NW, image=img1)

    can2 = Canvas(root, width = 400, height = 400)
    can2.pack()
    img2= ImageTk.PhotoImage(Image.open("scanfiles.png"))
    can2.place(x=440,y=20)
    scantxt=Label(root, text="NO 2.click Yes to scan the files to search for missing \n values or click No to ignore the mising values in the file.", fg='black', font=("Times new roman", 12))
    scantxt.place(x=480, y=255)
    can2.create_image(20, 30, anchor=NW, image=img2)


    can3= Canvas(root, width = 400, height = 400)
    can3.pack()
    img3= ImageTk.PhotoImage(Image.open("formatofdata.png"))
    can3.place(x=840,y=20)
    formattxt=Label(root, text="NO 3.the dataframe is shown above, the first column is the data \n and  the second column is the discharge/rainfall.", fg='black', font=("Times new roman", 12))
    formattxt.place(x=870, y=255)
    can3.create_image(20, 30, anchor=NW, image=img3)


    can4= Canvas(root, width = 400, height = 400)
    can4.pack()
    img4= ImageTk.PhotoImage(Image.open("selectmedian.png"))
    can4.place(x=0,y=330)
    seltxt2=Label(root, text="NO 4.To perform analysis on median Rainfall under \n package1,  first choose the rainfall station then click ok", fg='black', font=("Times new roman", 12))
    seltxt2.place(x=40, y=560)
    can4.create_image(20, 30, anchor=NW, image=img4)


    can5= Canvas(root, width = 400, height = 400)
    can5.pack()
    img5= ImageTk.PhotoImage(Image.open("selstation.png"))
    can5.place(x=390,y=330)
    sel=Label(root, text="NO.5 To perform analysis on Colwell's Indices under \n package2,  first choose the rainfall station then click ok", fg='black', font=("Times new roman", 12))
    sel.place(x=470, y=580)
    can5.create_image(20, 30, anchor=NW, image=img5)


    can6= Canvas(root, width = 400, height = 400)
    can6.pack()
    img6= ImageTk.PhotoImage(Image.open("man-kendall.png"))
    can6.place(x=830,y=300)
    mankendalltxt=Label(root, text="NO6.To perform analysis on classic man-kendall Test under \n package4,  first choose the rainfall station then choose \n the start month and end month then click ok", fg='black', font=("Times new roman", 12))
    mankendalltxt.place(x=880, y=570)
    can6.create_image(20, 30, anchor=NW, image=img6)




    def back():
        can1.delete("all")
        can1.create_image(0, 0, anchor=NW, image=img1)
        seltxt.configure(text="No 1. Under the file tab, go to 'select file' option and \n choose  the data type you want to import")

        can2.create_image(0, 0, anchor=NW, image=img2)
        scantxt.configure(text="NO 2.click Yes to scan the files to search for missing \n values or click No to ignore the mising values in the file.")

        can3.create_image(0, 0, anchor=NW, image=img3)
        formattxt.configure(text="NO 3.The dataframe is shown above, the first column is the data  \nand  the second column is the discharge/rainfall. ")

        can4.create_image(0, 0, anchor=NW, image=img4)
        seltxt2.configure(text="NO 4.To perform analysis on median Rainfall under \n package1,  first choose the rainfall station then click ok")

        can5.create_image(0, 0, anchor=NW, image=img5)
        sel.configure(text="NO.5 To perform analysis on Colwell's Indices under \n package2,  first choose the rainfall station then click ok")

        can6.create_image(0, 0, anchor=NW, image=img6)
        mankendalltxt.configure(text="NO6.To perform analysis on classic man-kendall Test under \n package4,  first choose the rainfall station then choose \n the start month and end month then click ok")
        backbutton.place_forget()
        nxtbtn.place(x=600, y=650)

    backbutton = Button(root, text="Back", height="2", width="20", bg="lightblue", fg="black", command=back)
    backbutton.place(x=600, y=650)
    
    Homebutton = Button(root, text="Home", height="2", width="20", bg="lightblue", fg="black", command=lambda: mn.loadpackages(loadroot))
    Homebutton.place(x=400, y=650)


    img7 = ImageTk.PhotoImage(Image.open("pca1.png"))
    img8 = ImageTk.PhotoImage(Image.open("pca2.png"))
    img9 = ImageTk.PhotoImage(Image.open("iha.png"))

    def next():

        can1.delete("all")
        can2.delete("all")
        can3.delete("all")
        can4.delete("all")
        can5.delete("all")
        can6.delete("all")

        mankendalltxt.configure(text="")
        sel.configure(text="")

        can1.create_image(0, 20, anchor=NW, image=img7)
        seltxt.configure(text="No7.To perform analysis on PCA, first choose the start and \nend month of  wet season as well as dry season then if \nyou want to check whether you put the correct data click \non the check button and then click on submit button")

        seltxt2.configure(text="")



        can2.create_image(0, 20, anchor=NW, image=img8)
        scantxt.configure(text="NO8. After you submit the data, the factor score \nwindow will pop up, then click on the dendogram button \non the left side buttom")

        can3.create_image(0, 20, anchor=NW, image=img9)
        formattxt.configure(text="NO9. To open IHA on the software,"
                                 " select IHA option\n under package2. Download IHA software before you try to open")

        backbutton.place(x=600, y=650)
        nxtbtn.place_forget()



    nxtbtn = Button(root, text="Next", height="2", width="20", bg="lightblue", fg="black" ,command=next)

    nxtbtn.place(x=600, y=650)


    def quit_me():
        root.destroy()
        loadroot.deiconify()


    root.protocol("WM_DELETE_WINDOW", quit_me)





