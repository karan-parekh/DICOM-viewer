import os
import pydicom
import matplotlib.pyplot as plt
from tkinter import Tk, Button
from tkinter.filedialog import askopenfile

data_dir = 'dicom_files/'
patients = os.listdir(data_dir)


def view(path):
    dataset = pydicom.read_file(path)
    print("Slice location...:", dataset.get('SliceLocation', "(missing)"))
    plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
    plt.show()


def open_dicom():
    patient = askopenfile(mode='r', filetypes=[('DICOM file', '*.dcm')]).name
    view(patient)


root = Tk(className="DICOM Viewer")

file_path = Button(root, text="Choose File (.dcm)", padx=5, pady=5, command=open_dicom)
file_path.pack()

root.mainloop()
