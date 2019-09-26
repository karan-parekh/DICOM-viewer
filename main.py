import os
import pydicom
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Listbox, Scrollbar, Frame, Label, END, NS, NW
from tkinter.filedialog import askdirectory


class Viewer(Frame):
    files = None
    folder = None

    def __init__(self, parent):
        Frame.__init__(self, parent)
        # frame for Listbox and Scrollbar
        self.frm = Frame(self)
        self.frm.grid(row=2, sticky=NW)
        # Button and Label
        self.file_path = Button(self, text="Choose Folder", command=self.set_dcm_files)
        self.file_path.grid(row=0)
        self.lab = Label(self, text="Double click the folder \n and then click OK")
        self.lab.grid(row=1)
        # Declaring Scrollbar and Listbox
        self.sbar = Scrollbar(self.frm, orient='vertical')
        self.dcm_list = Listbox(self.frm, width=20, yscrollcommand=self.sbar.set)
        self.dcm_list.bind("<<ListboxSelect>>", self.view_selected_item)
        self.sbar.config(command=self.dcm_list.yview)
        # Rendering Listbox and Scrollbar
        self.dcm_list.grid(row=0, column=0)
        self.sbar.grid(row=0, column=1, sticky=NS)

    # Sets dcm files and populates Listbox
    def set_dcm_files(self):
        self.folder = askdirectory()
        self.files = os.listdir(self.folder)
        self.populate_list()

    # Populates the Listbox
    def populate_list(self):
        self.dcm_list.delete(0, 'end')
        for f in self.files:
            self.dcm_list.insert(END, f)

    # Views the selected item from the Listbox
    def view_selected_item(self, event):
        path = self.dcm_list.get(self.dcm_list.curselection())
        dataset = pydicom.read_file(self.folder + "/" + path)
        plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
        plt.show()


if __name__ == '__main__':
    root = Tk(className="DICOM Viewer")
    Viewer(root).pack(fill='both', expand=True)
    root.mainloop()
