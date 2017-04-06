import os

def run(**kwargs):
    print "[*]In dirlist module"
    files = os.listdir(".")

    return  str(files)
