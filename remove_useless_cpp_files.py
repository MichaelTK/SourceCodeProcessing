#!/usr/bin/python3

import os

DATASET_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/2015"

def removeUselessCPPFiles():
    directories=listdir_fullpath(DATASET_PATH)
    for directory in directories:
        filesInDir = listdir_fullpath(directory)
        for file in filesInDir:
            found = False
            if file.endswith(".cpp"):
                for file2 in filesInDir:
                    #print(file[0:-3])
                    if file[0:-3] == file2[0:-3] and file != file2:
                        found = True
                if found == False:
                    #pass
                    print("Removing: "+file)
                    os.remove(file)


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


if __name__ == '__main__':
    removeUselessCPPFiles()
