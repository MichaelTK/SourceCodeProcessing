#!/usr/bin/python3

SOURCE_PATH1="/home/k1462425/Documents/Research/MalwareSourceTestSet2/malsource_dataset/"
SOURCE_PATH2="/home/k1462425/Documents/Research/TheZoo/theZoo/malwares/Source/Original/"

import os

def countFilesRec(directory):
    files = listdir_fullpath(directory)
    cppcount = 0
    for file in files:
        #print(file)
        if file.endswith('.cpp'):
            cppcount += 1
        elif os.path.isdir(file):
            #print(file)
            cppcount += countFilesRec(file)
    return cppcount


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

if __name__ == '__main__':
    directories=listdir_fullpath(SOURCE_PATH2)
    numbercppfiles=0
    numbermalwareswithcpp=0
    totalcppfiles=0
    numberofmalwares=0
    for dir in directories:
        if os.path.isdir(dir):
            numberofmalwares += 1
            numbercppfiles=countFilesRec(dir)
            if numbercppfiles > 0:
                print(dir+": "+str(numbercppfiles))
            if numbercppfiles > 0:
                numbermalwareswithcpp += 1
                totalcppfiles += numbercppfiles
                #print(dir+": "+str(numbercppfiles))
    print("Number of malwares: "+str(numberofmalwares))
    print("Number of malwares with cpp files: "+str(numbermalwareswithcpp))
    print("Total number of cpp files: "+str(totalcppfiles))
