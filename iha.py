from tkinter import filedialog
import os


def openiha():
    # if the txt file will not be empty.So it will save the user path first in the txt file for opening IHA
    if os.stat("ihaPath.txt").st_size == 0:
        filename = filedialog.askopenfilename(initialdir="/", title="Select IHA executable file",
                                              filetype=(("exe files", "*.exe"), ("all files", "*.*")))

        os.system(filename)
        f = open("ihaPath.txt", "w")
        f.write(filename)
        f.close()

    # if the txt file has already user path for IHA.It will open the IHA directly
    else:
        f = open("ihaPath.txt", "r")
        path = f.read()
        os.system(path)
