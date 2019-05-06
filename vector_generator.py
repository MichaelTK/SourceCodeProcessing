#!/usr/bin/python3

import sys
import os
import clang.cindex

SOURCE_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/2015/"
COMPILED_BIGRAMS_PATH="compiled_bigrams.txt"

debugc = 0
bigrams = [] #list to store all bigrams
function_names = [] #list to store all source function names
function_unit_pairs = [] #list to store all source function names along with the source files they came from
vectors = [] #list to store all feature vectors
bigrams_by_function = [] #list to store bigrams with what function and source file they came from
bigrams_by_function_count = [] #list to store how many instances of each bigram are in each function in the source

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def main():
    generate_vectors()

def generate_vectors():
    global bigrams_by_function_count, bigrams, function_unit_pairs, vectors
    number_of_bigrams=count_bigrams()
    write_all_bigrams()
    load_bigrams_by_function()
    print("Length of bigrams is: "+str(len(bigrams)))
    print(bigrams[1])
    print(bigrams_by_function[1][1])
    equivalent = False
    if bigrams[1] == bigrams_by_function[1][1]:
        equivalent = True
    print("Those two are equal: "+str(equivalent))
    print("Length of bigrams_by_function is: "+str(len(bigrams_by_function)))
    for function_unit_pair in function_unit_pairs:
        for bigram in bigrams:
            unit = (function_unit_pair,bigram,count_bigrams_by_function(function_unit_pair, bigram))
            bigrams_by_function_count.append(unit)

    #for bigram_by_function_count in bigrams_by_function_count:
    #    print(bigram_by_function_count[2])

    print("Length of bigrams_by_function_count is: "+str(len(bigrams_by_function_count)))

    print("DEBUGC IS: "+str(debugc))
    x = 0
    for function_unit_pair in function_unit_pairs:
        print(x)
        vectors.append([])
        vectors[x].append([])
        x = x + 1

    y = 0
    for function_unit_pair in function_unit_pairs:
        vectors[y][0]=(function_unit_pair)
        y = y + 1

    for vector in vectors:
        for bigram_by_function_count_instance in bigrams_by_function_count:
            #print(bigram_by_function_count_instance[2])
            if bigram_by_function_count_instance[0] == vector[0]:
                #print(bigram_by_function_count_instance[2])
                vector.append(bigram_by_function_count_instance[2])
                f=open("temp.txt","a+")
                f.write(str(bigram_by_function_count_instance[1])+str(bigram_by_function_count_instance[2])+"\n")
                f.close()

    print_vectors()

def print_vectors():
    global vectors
    print("There are "+str(len(vectors))+" vectors")
    for vector in vectors:
        print("Length of the vector is: "+str(len(vector)))
        for elem in vector:
            print(str(elem))

def count_bigrams_by_function(function_unit_pair, bigram):
    global bigrams, vectors, function_unit_pairs, debugc
    vector = []
    count = 0
    #print(bigram)
    #debugc = 0
    for bigram_by_function in bigrams_by_function:
        #count = 0
        #print(bigram_by_function[1])
        #print(bigram)
        if bigram_by_function[0] == function_unit_pair:
            if bigram == bigram_by_function[1]:
                #print("--------------------------")
                #print(bigram)
                #print(bigram_by_function[1])
                #print("--------------------------")
                #print("MATCH FOUND!"+str(bigram))
                #print(bigram)
                count = count + 1
                debugc = debugc + 1
    #if count > 1:
    #    print("COUNT IS BIGGER THAN 1!")
    return count


def load_bigrams_by_function():
    global function_unit_pairs, bigrams, bigrams_by_function
    for function_unit_pair in function_unit_pairs:
        for bigram in bigrams:
            if (function_unit_pair[0] in bigram[0] and function_unit_pair[1] in bigram[0]) or (function_unit_pair[0] in bigram[1] and function_unit_pair[1] in bigram[1]):
                unit = (function_unit_pair,bigram)
                bigrams_by_function.append(unit)

def write_all_bigrams():
    exists = os.path.isfile(COMPILED_BIGRAMS_PATH)
    if exists:
        os.remove(COMPILED_BIGRAMS_PATH)

    f = open(COMPILED_BIGRAMS_PATH,"a+")
    for bigram in bigrams:
        f.write(bigram[0])
        f.write(bigram[1])
        f.write("\n")
    f.close()

def count_bigrams():
    global bigrams
    directories = listdir_fullpath(SOURCE_PATH)

    for dir in directories:
        source_files = listdir_fullpath(dir)
        for source_file in source_files:
            if source_file.endswith(".astdump"):
                print("FILE:"+source_file)
                bigrams.extend(read_bigrams_from_astdump(source_file))

    print(len(bigrams))
    return len(bigrams)

def read_bigrams_from_astdump(file):
    bigrams = []
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    bigrams = extract_bigrams_from_lines(lines)
    return bigrams

def extract_bigrams_from_lines(lines):
    bigrams = []
    pair = []
    global function_unit_pairs
    new_bigram = True
    for line in lines:
        #print("start")
        #print(line)
        #print("stop")
        if line == "\n":
            new_bigram = False
        else:
            new_bigram = True
        if new_bigram == True:
            pair.append(line)
            splitline = line.split(',')
            #print(splitline)
            function_unit_pair = (splitline[-2],splitline[-1])
            if function_unit_pair not in function_unit_pairs:
                print(function_unit_pair)
                function_unit_pairs.append(function_unit_pair)
        if len(pair) > 1:
            bigrams.append(pair)
            pair = []
    #print_bigrams(bigrams)
    return bigrams


def print_bigrams(bigrams):
    for bigram in bigrams:
        print("start of bigram")
        print(bigram[0])
        print(bigram[1])
        print("end of bigram")

main()
