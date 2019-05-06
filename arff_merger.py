#!/usr/bin/python3

import os
import fileinput

FILE1_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/SCAAarffs/76authors_syntactical2.arff"
FILE2_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/SCAAarffs/76authors_lexical.arff"
TEMP_FILE1="/home/k1462425/Documents/Research/MalwareSourceTestSet/SCAAarffs/syntactical_76authors_temp"
TEMP_FILE2="/home/k1462425/Documents/Research/MalwareSourceTestSet/SCAAarffs/lexical_76authors_temp"
COMPILED_VECTORS_FILEPATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/SCAAarffs/compiled_76authors"
PADDING_ARRAY=[]

def truncate_arffs(syntaxarffpath, lexicalarffpath):
    print("Within truncate_arffs")
    truncate_arff(syntaxarffpath,TEMP_FILE1)
    print("After truncating syntax")
    truncate_arff(lexicalarffpath,TEMP_FILE2)
    print("After truncating lexical")

def truncate_arff(arfffile,tempfilepath):
    TAG = '@data'

    tag_found = False
    with open(arfffile) as in_file:
        with open(tempfilepath, 'w') as out_file:
            for line in in_file:
                if not tag_found:
                    if line.strip() == TAG:
                        tag_found = True
                else:
                    out_file.write(line)

def load_vectors(syntaxarffpath,lexicalarffpath):
    syntax_vectors = load_vectors_from_arff(syntaxarffpath)
    lexical_vectors = load_vectors_from_arff(lexicalarffpath)
    vectors = [syntax_vectors, lexical_vectors]
    return vectors

def load_vectors_from_arff(arffpath):
    vectors=[]
    with open(arffpath) as fp:
        line = fp.readline()
        cnt = 1

        while line:
            splitline = line.strip().split(',')
            vectors.append(splitline)
            line = fp.readline()
            cnt += 1
    return vectors

def merge_vectors(vectors):
    syntax_vectors = vectors[0]
    print("Syntax vector length: "+str(len(syntax_vectors[0])))
    print("Last element of syntax vector: "+syntax_vectors[0][-1])
    lexical_vectors = vectors[1]
    print("Lexical vector length: "+str(len(lexical_vectors[0])))
    print("Last element of lexical vector: "+lexical_vectors[0][-1])
    merged_vectors = []
    #debugc = 0
    for lex_vector in lexical_vectors:
        #print(debugc)
        #debugc += 1
        match_found = False
        for syn_vector in syntax_vectors:
            if "kuvol" not in lex_vector[0] and "Копия" not in lex_vector[0]:
                if lex_vector[0] == syn_vector[0] and lex_vector[-1] == syn_vector[-1]:
                    syn_vector = syn_vector[:-1]
                    lex_vector = lex_vector[1:]
                    #print(lex_vector[0])
                    match_found = True
                    merged_vector = merge_vector(syn_vector, lex_vector)
                    merged_vectors.append(merged_vector)
        if match_found == False:
            print("Match not found.")
            print("lex_vector without match: "+lex_vector[0])
                #WHAT TO DO IF THERE'S A MISMATCH BETWEEN LEXICAL AND SYNTACTICAL?
    return merged_vectors

def merge_vector(syn_vector, lex_vector):
    syn_vector.extend(lex_vector)
    return syn_vector

def write_vectors(vectors):
    with open(COMPILED_VECTORS_FILEPATH, 'a') as the_file:
        debugc = 0
        for vector in vectors:
            print(debugc)
            debugc += 1
            write_vector(the_file,vector)

def write_vector(file,vector):
    for elem in vector:
        file.write(elem+',')
    file.write('\n')

def pad_vectors(vectors):
    padding_vector=[0,0,0,0]
    for vector in vectors:
        if len(vector) < 36043:
            print("PADDING!")
            vector.extend(padding_vector)
        #print(len(vector))
    return vectors


def merge_files(syntaxarffpath, lexicalarffpath):
    print("In merge_files")
    truncate_arffs(syntaxarffpath,lexicalarffpath)
    print("After truncating")
    vectors = load_vectors(TEMP_FILE1,TEMP_FILE2)
    print("After loading vectors")
    merged_vectors = merge_vectors(vectors)
    print("After merging vectors")
    #finished_vectors = pad_vectors(merged_vectors)
    #print("After padding vectors")
    write_vectors(merged_vectors)
    print("After writing vectors")

def cleanup():
    os.remove(TEMP_FILE1)
    os.remove(TEMP_FILE2)

if __name__ == '__main__':
    print("In main")
    merge_files(FILE1_PATH, FILE2_PATH)
    cleanup()
    print("Theoretically finished")
