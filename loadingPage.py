from tkinter import *
import main as mn


loadroot = Tk()
loadroot.title("HyFFlow")
loadroot.geometry("415x410")
loadroot.iconbitmap('iconlogo.ico')
loadroot.resizable(0, 0)

# Title label
hyfflow = Label(loadroot, text="Welcome to HyFFlow", fg='grey', font=("Pristina", 30))
hyfflow.place(x=60, y=50)
hyfflow.pack()

# Start button leading to main page
startbutton = Button(loadroot, text="HOME", height="5", width="40", bg="lightblue", fg="black",
                     command=lambda: mn.loadpackages(loadroot))
startbutton.place(x=60, y=70)

# guide button leads to user manual
guidebutton = Button(loadroot, text="GUIDE", height="5", width="40", bg="lightblue", fg="black")
guidebutton.place(x=60, y=170)


def exitt():
    loadroot.destroy()
    loadroot.quit()


guidebutton = Button(loadroot, text="EXIT", height="5", width="40", bg="lightblue", fg="black", command=exitt)
guidebutton.place(x=60, y=270)


def quit_me():
    loadroot.quit()
    loadroot.destroy()


loadroot.protocol("WM_DELETE_WINDOW", quit_me)
loadroot.mainloop()
