from shutil import copy
import os
from zipfile import ZipFile

SOURCE_PATH = "/home/k1462425/Documents/Research/TheZoo/theZoo/malwares/Source/Original"
DEST_PATH = "/home/k1462425/Documents/Research/MalwareSourceTestSet/2015/"
ancestorDirectories = []

def initialListingOfDirectories():
    return listdir_fullpath(SOURCE_PATH)

def copyFromDirectory(directoryPath):
    initialDirectories = initialListingOfDirectories()
    global ancestorDirectories
    #print "Directory path is: " + directoryPath
    if directoryPath in initialDirectories:
        ancestorDirectories = [directoryPath]
        #print "True"
    else:
        #print "False"
        if directoryPath != SOURCE_PATH:
            #print "Appending"
            ancestorDirectories.append(directoryPath)

    filesAndDirectories = listdir_fullpath(directoryPath)

    for file in filesAndDirectories:
        if os.path.isfile(file):
            name, ext = os.path.splitext(file)
            if ext == ".h":
                normalisedDirectory =  os.path.basename(os.path.normpath(ancestorDirectories[0]))
                destination = DEST_PATH+normalisedDirectory
                #print normalisedDirectory
                print "Copying file "+ file + " to "+destination
                try:
                    copy(file,destination)
                except:
                    print("Exception.")
            #print file
        elif os.path.isdir(file):
            #print "ayy"+file
            copyFromDirectory(file)

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def unzipInDirectory(directoryPath):
    filesAndDirectories = listdir_fullpath(directoryPath)
    password = ""
    for file in filesAndDirectories:
        if os.path.isfile(file):
            name, ext = os.path.splitext(file)
            if ext == ".pass":
                f=open(file, "r")
                if f.mode == "r":
                    contents = f.read()
                password = contents

    for file in filesAndDirectories:
        if os.path.isfile(file):
            name, ext = os.path.splitext(file)
            if ext == ".zip":
                print "Attempting to unzip: " + file + " with password " + password
                try:
                    with ZipFile(file) as zf:
                        try:
                            zf.extractall(directoryPath, None, pwd=password)
                        except:
                            print "An exception occurred."
                except:
                    print "File not a zip file?"
        elif os.path.isdir(file):
            #print "ayy"+file
            unzipInDirectory(file)

if __name__ == '__main__':
    #directories=initialListingOfDirectories()
    #for directory in directories:
    #    normalisedDirectory =  os.path.basename(os.path.normpath(directory))
    #    try:
    #        os.mkdir(DEST_PATH+"/"+normalisedDirectory)
    #    except:
    #        print "Directory probably exists already. Exception."
    #unzipInDirectory(SOURCE_PATH)
    copyFromDirectory(SOURCE_PATH)
