#!/usr/bin/python3

import os
import shutil

DATASET_PATH = "/home/k1462425/Documents/Research/MalwareSourceTestSet/2015/"


def removeAllBut10Files(directory):
    filesListing = listdir_fullpath(directory)
    count = 0
    for file in filesListing:
        if count > 9:
            os.remove(file)
        count = count + 1

def removeDirectoryWithFewerThan40Files(directory):
    filesListing=listdir_fullpath(directory)
    if len(filesListing) < 40:
        shutil.rmtree(directory)

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

if __name__ == '__main__':
    directoriesToTrim = listdir_fullpath(DATASET_PATH)
    #for directory in directoriesToTrim:
    #    removeDirectoryWithFewerThan40Files(directory)
    for directory in directoriesToTrim:
        directoryFiles = listdir_fullpath(directory)
        if not directoryFiles:
            os.rmdir(directory)
        else:
            removeAllBut10Files(directory)
