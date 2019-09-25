import os
import pydicom
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Listbox, Scrollbar, Frame, Label, RIGHT, END
from tkinter.filedialog import askdirectory


def view(path):
    dataset = pydicom.read_file(path)
    plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
    plt.show()


root = Tk(className="DICOM Viewer")

frm = Frame(root)
frm.pack()

geo = root.geometry
geo("300x300")


def open_folder():

    def selected(event):
        path = dcm_list.get(dcm_list.curselection())
        view(folder + "/" + path)

    folder = askdirectory()
    flist = os.listdir(folder)

    sb = Scrollbar(frm, orient='vertical')
    dcm_list = Listbox(frm, width=20, yscrollcommand=sb.set)
    dcm_list.bind("<<ListboxSelect>>", selected)
    sb.config(command=dcm_list.yview)
    sb.pack(side=RIGHT, fill='y')
    dcm_list.pack()
    for f in flist:
        dcm_list.insert(END, f)


file_path = Button(root, text="Choose Folder (.dcm)", command=open_folder)
file_path.pack()

lab = Label(root, text="Double click the folder \n and then click OK")
lab.pack()

root.mainloop()
