import matplotlib.pyplot as plt
import pydicom
import os
import numpy as np
import cv2
import math

data_dir = 'dicom_files/'
patients = os.listdir(data_dir)

IMG_SIZE = 150
NO_OF_SLICES = 21


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


def mean(l):
    return sum(l)/len(l)


def main():
    for _ in patients[:2]:
        slices = [pydicom.read_file(data_dir + '/' + s) for s in os.listdir(data_dir)]  # 61 slices
        slices.sort(key=lambda x: int(x.ImagePositionPatient[2]))

        new_slices = []

        slices = [cv2.resize(np.array(each_slice.pixel_array), (IMG_SIZE, IMG_SIZE)) for each_slice in slices]
        chunk_size = math.ceil(len(slices) / NO_OF_SLICES)

        for slice_chunk in chunks(slices, chunk_size):
            slice_chunk = list(map(mean, zip(*slice_chunk)))
            new_slices.append(slice_chunk)

        new_slices.pop()  # to reduce it to 20 slices

        fig = plt.figure()
        for num, each_slice in enumerate(new_slices):
            y = fig.add_subplot(4, 5, num+1)
            y.imshow(each_slice)
        plt.show()


if __name__ == '__main__':
    main()
