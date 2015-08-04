from subprocess import call
from glob import glob
from sys import argv
import os
import shutil

def extract(filename):
    foldername = filename.split(".")[0].replace(" ","_")
    if not os.path.exists(foldername):
        os.mkdir(foldername)
    shutil.copy(filename,foldername+"/"+filename)
    os.chdir(foldername)
    call(["pdfimages","-j",filename,foldername])
    pbm = glob("*.pbm")
    ppm = glob("*.ppm")
    for elem in ppm:
        os.remove(elem)
    for elem in pbm:
        os.remove(elem)
    os.chdir("../")

if __name__ == '__main__':
    folder = argv[1]
    files = glob("*.pdf")
    for File in files:
        extract(File)
