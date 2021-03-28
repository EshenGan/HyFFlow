from tkinter import *
from tkinter import font
import main as mn
import p2main as mn2
import p4main as mn4
import p3main as mn3

root =Tk()
root.title("HyFFlow")
root.geometry("830x500")
root.resizable(0, 0)

theLabel=Label(root, text="Welcome to HyFFlow", fg='grey', font=("Pristina", 30))
theLabel.place(x=60, y=50)
theLabel.pack()



def OpenPackage3():
	print(" Hydrograph Shape")

def OpenPackage1():
	print(" Fundamentals of the Flow Regime ")

def OpenPackage2():
	print(" Flow Metrics")

def OpenPackage4():
	print(" Long-term Trends on Flow and Rainfall Regimes")



b1 = Button(root, text = " Hydrograph Shape",height="5",width="40" ,bg="grey",fg = "white" ,command=lambda:mn3.package3(root))
b1.place(x=100,y=280)

b2 = Button(root, text = " Fundamentals of the Flow Regime ",height="5", width="40",bg ="grey",fg= "white" ,command=lambda:mn.package1(root))
b2.place(x=100,y=180)

b3 = Button(root, text = " Flow Metrics",height="5",width="40",bg="grey" ,fg = "white",command=lambda:mn2.package2(root))
b3.place(x=440,y=180)

b4 = Button(root, text = " Long-term Trends on Flow and Rainfall Regimes",height="5",width="40",bg="grey" ,fg = "white", command=lambda:mn4.package4(root))
b4.place(x=440,y=280)
def quit_me():
    root.quit()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", quit_me)
root.mainloop()