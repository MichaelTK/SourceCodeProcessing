#!/usr/bin/python3

import os
import subprocess

SOURCE_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/2015/"

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def generate_asts():
    directories = listdir_fullpath(SOURCE_PATH)
    for dir in directories:
        generate_asts_for_dir(dir)

def generate_asts_for_dir(dir):
    files = listdir_fullpath(dir)
    for file in files:
        if file.endswith(".cpp"):
            generate_ast(file)

def generate_ast(file):
    bashCommand = "clang -Xclang -ast-dump -fno-color-diagnostics "+file
    print(bashCommand)
    xmlfilename=file[0:-3]+"xml"
    f = open(xmlfilename, "w")
    process = subprocess.Popen(bashCommand.split(), stdout=f)
    output, error = process.communicate()

if __name__ == '__main__':
    generate_asts()
