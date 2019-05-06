#!/usr/bin/python3
""" Usage: call with <filename> <typename>
"""

import sys
import os
import clang.cindex as cl

cl.Config.set_library_file("/opt/rh/llvm-toolset-7/root/usr/lib64/libclang.so")

SOURCE_PATH="/home/k1462425/scratch/data1/TheZooDataset/2015/"
COMPILED_BIGRAMS_PATH="compiled_bigrams.txt"

nodes = []
bigrams = []
global_bigrams = []
function_name = ""

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def extract_nodes(node):
    """ Find all nodes."""
    global bigrams

    for bigram in bigrams:
        parent = bigram[0]
        child = bigram[1]

        append_to_nodes(parent,child)


def append_to_nodes(parentNode, childNode):
    #print("Appending to nodes!")
    global nodes
    try:

        if parentNode.kind.name == "FUNCTION_DECL":
            #print(node.spelling)
            function_name = parentNode.spelling

        if childNode.kind.name == "FUNCTION_DECL":
            #print(node.spelling)
            function_name = childNode.spelling

        parent_token_spelling=""
        for token in parentNode.get_tokens():
            if "<" in token.spelling or ">" in token.spelling or "==" in token.spelling:
                if parent_token_spelling != "":
                    parent_token_spelling=parent_token_spelling+","+token.spelling
                else:
                    parent_token_spelling=token.spelling

        parent_node_spelling = parentNode.spelling
        parent_node_kind_name = parentNode.kind.name

        child_token_spelling=""
        for token in childNode.get_tokens():
            if "<" in token.spelling or ">" in token.spelling or "==" in token.spelling:
                if child_token_spelling != "":
                    child_token_spelling=child_token_spelling+","+token.spelling
                else:
                    child_token_spelling=token.spelling

        child_node_spelling = childNode.spelling
        child_node_kind_name = childNode.kind.name

        parent_node_combined = parent_node_kind_name+","+parent_node_spelling+","+parent_token_spelling+","+function_name
        #print(parent_node_combined)
        child_node_combined = child_node_kind_name+","+child_node_spelling+","+child_token_spelling+","+function_name
        #print(child_node_combined)
        pair = (parent_node_combined, child_node_combined)
        #print(pair)
        nodes.append(pair)
        #print(nodes[-1])
    except Exception as ex:
        print(ex)

def extract_bigrams(node):
    """ Find all node bigrams. """
    global bigrams, function_name

    children = node.get_children()
    for child in children:
        if node.kind.name == "FUNCTION_DECL":
            print(node.spelling)
            function_name = node.spelling
        pair = (node, child)
        bigrams.append(pair)
        extract_bigrams(child)

def print_bigrams():
    global nodes
    for pair in nodes:
        print(pair[0])
        print(pair[1])
        print("\n\n")

def print_nodes():
    global nodes
    for node in nodes:
        print(node)

def write_bigrams(FILENAME):
    global nodes
    print(nodes)
    f=open(FILENAME,"w+")
    print(len(nodes))
    for pair in nodes:
        #print("in loop")
        parent=pair[0]
        child=pair[1]
        #print(parent+"\n")
        #print(child+"\n\n")
        f.write(parent+"\n")
        f.write(child+"\n\n")
    f.close()

def extract_bigrams_from_file(file):
    global nodes, bigrams
    index = cl.Index.create()
    tu = index.parse(file)

    extract_bigrams(tu.cursor)
    extract_nodes(tu.cursor)
    #nodes = []
    #bigrams = []

def compile_bigrams():
    directories = listdir_fullpath(SOURCE_PATH)
    for dir in directories:
        #print(dir)
        source_files = listdir_fullpath(dir)
        for source_file in source_files:
            if source_file.endswith(".astdump"):
                compile_bigrams_from_file(source_file)

def compile_bigrams_from_file(file):
    global global_bigrams
    first_node = ""
    second_node = ""
    with open(file) as fp:
        line = fp.readline()
        cnt = 1
        new_value = True
        while line:
            line = fp.readline()
            if line == "\n":
                pair = (first_node, second_node)
                global_bigrams.append(pair)
                new_value = True
            else:
                if new_value == True:
                    first_node = line
                elif new_value == False:
                    second_node = line

                new_value = False
            cnt += 1
    remove_duplicate_bigrams()
    write_compiled_bigrams()

def write_compiled_bigrams():
    global global_bigrams
    f=open(COMPILED_BIGRAMS_PATH,"w+")
    for pair in nodes:
        parent=pair[0]
        child=pair[1]
        f.write(parent+"\n")
        f.write(child+"\n\n")
    f.close()

def remove_duplicate_bigrams():
    global_bigrams = list(set(global_bigrams))

def produce_feature_vectors():
    directories = listdir_fullpath(SOURCE_PATH)
    for dir in directories:
        #print(dir)
        source_files = listdir_fullpath(dir)
        for source_file in source_files:
            if source_file.endswith(".astdump"):
                produce_feature_vector(source_file)

def produce_feature_vector(file):
    global global_bigrams
    first_node = ""
    second_node = ""
    file_bigrams = []
    with open(file) as fp:
        line = fp.readline()
        cnt = 1
        new_value = True
        while line:
            line = fp.readline()
            if line == "\n":
                pair = (first_node, second_node)
                file_bigrams.append(pair)
                new_value = True
            else:
                if new_value == True:
                    first_node = line
                elif new_value == False:
                    second_node = line

                new_value = False
            cnt += 1
    vector = produce_vector(file_bigrams)
    return vector

def produce_vector(file_bigrams):
    vector = pad_vector(vector, len(global_bigrams))

def pad_vector(vector, length):
    i = 0
    while i < length:
        vector.append(0)

def main():
    directories = listdir_fullpath(SOURCE_PATH)

    BASE_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/2015/"

    x = 0
    for dir in directories:
        source_files = listdir_fullpath(dir)
        for source_file in source_files:
            if source_file.endswith("2.cpp"):
                print(source_file[:-5])
                extract_bigrams_from_file(source_file)
                write_bigrams(source_file[:-5]+".astdump")
                print(x)
                x = x + 1
                nodes = []
                bigrams = []
    #extract_bigrams_from_file(BASE_PATH)
    #print_nodes()
    #write_bigrams(BASE_PATH[:-5]+".astdump")
    #nodes = []
    #bigrams = []
    #for dir in directories:
    #    #print(dir)
    #    source_files = listdir_fullpath(dir)
    #    for source_file in source_files:
    #        if source_file.endswith("2.cpp"):
    #            print(source_file[:-5])
    #            extract_bigrams_from_file(source_file)
    #            write_bigrams(source_file[:-5]+".astdump")


main()
