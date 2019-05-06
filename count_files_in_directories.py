#!/usr/bin/python3

SOURCE_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/2015/"

import os

def countFiles(directory):

    print(directory+": "+str(len(listdir_fullpath(directory))))

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

if __name__ == '__main__':
    directories=listdir_fullpath(SOURCE_PATH)
    for dir in directories:
        countFiles(dir)
