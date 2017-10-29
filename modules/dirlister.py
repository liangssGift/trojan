import os

def run(**args):
    print "[*] In dirlister module."
    files = os.lisrdir(".")

    return str(files)
