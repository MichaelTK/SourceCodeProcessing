#!/usr/bin/python3
import os

SOURCE_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/2015"

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def trim_file(file):
    bad_words = ['#include']

    newfile = file[:-4]
    print(newfile)
    with open(file,encoding="utf-8", errors='ignore') as oldfile, open(newfile+"2.cpp", 'w') as newfile:
        #count = 0
        #if count < 15:
        for line in oldfile:
            #print("1")
            #line=bytes(line, 'utf-8').decode('utf-8','ignore')
            #print("2")
            if not any(bad_word in line for bad_word in bad_words):
                try:
                    newfile.write(line)
                except:
                    print("Exception occurred.")
        #count = count + 1

def trim_dir(dir):
    files=listdir_fullpath(dir)
    for file in files:
        if file.endswith(".cpp"):
            trim_file(file)

def main():
    directories=listdir_fullpath(SOURCE_PATH)
    for dir in directories:
        trim_dir(dir)

main()
