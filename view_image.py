import os
import pydicom
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Listbox, END, Scrollbar, Frame, RIGHT
from tkinter.filedialog import askopenfile, askdirectory


def view(path):
    dataset = pydicom.read_file(path)
    print("Slice location...:", dataset.get('SliceLocation', "(missing)"))
    plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
    plt.show()


# def open_dicom():
#     patient = askopenfile(mode='r', filetypes=[('DICOM file', '*.dcm')]).name
#     view(patient)


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
    print(folder)
    flist = os.listdir(folder)

    dcm_list = Listbox(frm, width=20)
    dcm_list.bind("<<ListboxSelect>>", selected)
    dcm_list.pack()
    for f in flist:
        dcm_list.insert(END, f)


file_path = Button(root, text="Choose Folder (.dcm)", padx=5, pady=5, command=open_folder)
file_path.pack()


# view_button = Button(root, text="View", command=view, args=selected_dcm)

root.mainloop()
