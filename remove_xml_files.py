#!/usr/bin/python3

import os

SOURCE_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/2015/"

def remove_xml_files():
    directories = listdir_fullpath(SOURCE_PATH)
    for dir in directories:
        files = listdir_fullpath(dir)
        for file in files:
            if file.endswith(".xml"):
                print("Removing "+file)
                os.remove(file)

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

if __name__ == '__main__':
    remove_xml_files()
