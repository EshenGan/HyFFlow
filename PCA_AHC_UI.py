from tkinter import *
import PCA as pt
import pcatable as pcad


def pca_ahc_ui(mainroot, df):
    #set up the menu
    pcaroot = Toplevel(mainroot)
    pcaroot.iconbitmap('iconlogo.ico')
    pcaroot.geometry("300x350")
    choices = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    pcaroot.resizable(0, 0)

    #create variable to take in option
    clicked = StringVar()
    clicked1 = StringVar()
    clicked2 = StringVar()
    clicked3 = StringVar()

#convert month to interger    
    def switch_demo(argument):
        switcher = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sept": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12
        }
        return switcher.get(argument)

    def return_value():
        #drop down menu to select month
        d1 = switch_demo(clicked.get())
        d2 = switch_demo(clicked1.get())
        w1 = switch_demo(clicked2.get())
        w2 = switch_demo(clicked3.get())
        data = df.copy()
        pcadf = pt.pcapreprocess(data, d1, d2, w1, w2)
        df2 = pcadf.copy()
        pcad.displaypca(pcaroot, df2)

        #check input value
    def check_value():
        label = Label(pcaroot, text="User Input")
        label.place(x=110, y=210)
        # display value chosen
        label1 = Label(pcaroot, text=clicked.get())
        label1.place(x=60, y=230)
        # display value chosen
        label2 = Label(pcaroot, text=clicked1.get())
        label2.place(x=200, y=230)
        # display value chosen
        label3 = Label(pcaroot, text=clicked2.get())
        label3.place(x=60, y=260)
        # display value chosen
        label4 = Label(pcaroot, text=clicked3.get())
        label4.place(x=200, y=260)

        label5 = Label(pcaroot, text="Dry Start:")
        label5.place(x=0, y=230)

        label6 = Label(pcaroot, text="Dry End:")
        label6.place(x=150, y=230)

        label7 = Label(pcaroot, text="Wet Start:")
        label7.place(x=0, y=260)

        label8 = Label(pcaroot, text="Wet End:")
        label8.place(x=150, y=260)

    w = Label(pcaroot, text="Select Month")
    w.pack(padx=11, pady=11)

    w = Label(pcaroot, text="Dry Season")
    w.place(x=110, y=55)

    w = Label(pcaroot, text="From")
    w.place(x=0, y=85)

    w = Label(pcaroot, text="End")
    w.place(x=160, y=85)
#drop down menu for dry season
    drop = OptionMenu(pcaroot, clicked, *choices)
    drop.place(x=40, y=80)
    drop1 = OptionMenu(pcaroot, clicked1, *choices)
    drop1.place(x=200, y=80)

    w = Label(pcaroot, text="Wet Season")
    w.place(x=110, y=135)

    w = Label(pcaroot, text="From")
    w.place(x=0, y=165)

    w = Label(pcaroot, text="End")
    w.place(x=160, y=165)
#drop down menu for wet season
    drop3 = OptionMenu(pcaroot, clicked2, *choices)
    drop3.place(x=40, y=160)
    drop4 = OptionMenu(pcaroot, clicked3, *choices)
    drop4.place(x=200, y=160)
#submit input button
    submitbutton = Button(pcaroot, text="Submit", command=return_value)
    submitbutton.place(x=120, y=300)
#check input button
    checkbutton1 = Button(pcaroot, text="Check", command=check_value)
    checkbutton1.place(x=0, y=300)
#close window button
    checkbutton2 = Button(pcaroot, text="Quit", command=pcaroot.destroy)
    checkbutton2.place(x=250, y=300)
#exit menu function
    def quit_me():
        pcaroot.quit()
        pcaroot.destroy()

    pcaroot.protocol("WM_DELETE_WINDOW", quit_me)
    pcaroot.mainloop()
