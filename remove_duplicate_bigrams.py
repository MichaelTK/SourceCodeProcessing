#!/usr/bin/python3

import sys
import os

SOURCE_PATH="/home/k1462425/Documents/Research/ZooTestSubset/2015/LiquidBot_May2005"

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def main():
    directories = listdir_fullpath(SOURCE_PATH)

    #for dir in directories:
    #    files = listdir_fullpath(dir)
    #    for file in files:
    #        if file.endswith(".astdump"):
    #            remove_duplicate_bigrams(file)

    files = listdir_fullpath(SOURCE_PATH)
    for file in files:
        if file.endswith(".astdump"):
            remove_duplicate_bigrams(file)

def remove_duplicate_bigrams(file):
    print(file)
    bigrams = []
    bigram = []
    with open(file) as open_file:
        for line in open_file:
            #print(repr(line))
            #if line == "\n":
            #    print("AYYYYYYYYYYYYYYYY")
            if line != "\n":
                bigram.append(line)
                #print("APPENDING to BIGRAM:"+line)
            if line == "\n":
                #print("EMPTY LINE")
                print(line)
                bigrams.append(bigram)
                bigram = []

    #print_bigrams(bigrams)

    f=open(file,"a+")

    for big in bigrams:
        count = 0
        for elem in big:
            print(str(count)+": "+elem)
            count += 1

    for big in bigrams:
        count = 0
        print("First bigram is: "+big[0])
        for big2 in bigrams:
            if big2 == big:
                count += 1
                print("AAEYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
                if count > 1:
                    bigrams.remove(big2)

    for big in bigrams:
        f.write(big[0]+"\n")
        f.write(big[1]+"\n\n")
    f.close()

def print_bigrams(bigrams):
    for big in bigrams:
        print(big[0]+"\n")
        print(big[1])
        print("\n\n")

main()
