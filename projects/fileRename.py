
import os

path = r"C:\Users\HP\Pictures\2020-08-09 001\Internal shared storage\test\home"
import zipfile
import os
path = r"C:\Users\HP\Pictures\2020-08-09 001\Internal shared storage\test\home"
files = os.listdir(path)


def fileParse(path):
    "The file is valid" if os.path.exists(path) else "The path is invald"
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, str(index).join(["cathir", '.jpg'])))
fileParse(path)

