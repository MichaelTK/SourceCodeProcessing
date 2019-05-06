#!/usr/bin/python3

import sys
import os

SOURCE_PATH="/home/k1462425/Documents/Research/ZooTestSubset/2015/"

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def main():
    astdump_count = count_astdump_files()

def count_astdump_files():
    directories = listdir_fullpath(SOURCE_PATH)
    astdump_count = 0

    for dir in directories:
        files = listdir_fullpath(dir)
        for file in files:
            if file.endswith(".astdump"):
                astdump_count += 1

    return astdump_count


main()
