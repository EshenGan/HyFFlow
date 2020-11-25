from tkinter import *
from tkinter import font
import main as mn

root =Tk()
root.title("HyFFlow")

root.geometry("990x566")


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



b1 = Button(root, text = " Hydrograph Shape",height="5",width="40" ,bg="grey",fg = "white" ,command=lambda:mn.package1(root))
b1.place(x=460,y=390)

b2 = Button(root, text = " Fundamentals of the Flow Regime ",height="5", width="40",bg ="grey",fg= "white" ,command=lambda:mn.package1(root))
b2.place(x=460,y=290)

b3 = Button(root, text = " Flow Metrics",height="5",width="40",bg="grey" ,fg = "white",command=lambda:mn.package1(root))
b3.place(x=800,y=290)

b4 = Button(root, text = " Long-term Trends on Flow and Rainfall Regimes",height="5",width="40",bg="grey" ,fg = "white", command=lambda:mn.package1(root))
b4.place(x=800,y=390)
def quit_me():
    root.quit()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", quit_me)
root.mainloop()