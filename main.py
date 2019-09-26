import os
import pydicom
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Listbox, Scrollbar, Frame, Label, RIGHT, END, NS, NW
from tkinter.filedialog import askdirectory


class Viewer(Frame):
    files = None
    folder = None

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.frm = Frame(self)
        self.frm.grid(row=2, sticky=NW)

        self.file_path = Button(self, text="Choose Folder", command=self.get_all_files)
        self.file_path.grid(row=0)
        self.lab = Label(self, text="Double click the folder \n and then click OK")
        self.lab.grid(row=1)

        self.sb = Scrollbar(self.frm, orient='vertical')
        self.dcm_list = Listbox(self.frm, width=20, yscrollcommand=self.sb.set)
        self.dcm_list.bind("<<ListboxSelect>>", self.view_selected_item)
        self.sb.config(command=self.dcm_list.yview)

        self.dcm_list.grid(row=0, column=0)
        self.sb.grid(row=0, column=1, sticky=NS)

    def get_all_files(self):
        self.folder = askdirectory()
        self.files = os.listdir(self.folder)
        self.populate_list()

    def populate_list(self):
        self.dcm_list.delete(0, 'end')
        for f in self.files:
            self.dcm_list.insert(END, f)

    def view_selected_item(self, event):
        path = self.dcm_list.get(self.dcm_list.curselection())
        dataset = pydicom.read_file(self.folder + "/" + path)
        plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
        plt.show()


if __name__ == '__main__':
    root = Tk(className="DICOM Viewer")
    Viewer(root).pack(fill='both', expand=True)
    root.mainloop()
