#!/usr/bin/python3

import os

VECTOR_FILE_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/SCAAarffs/compiled_76authors"

elements_popped = 0
number_of_vectors = 1010
number_of_elems = 200000*number_of_vectors

def load_vectors():
    print("In load_vectors()")
    lines = []
    malwarenames = []
    filenames = []
    with open(VECTOR_FILE_PATH) as fp:
        line = fp.readline()
        cnt = 1
        #while line:
        while line:
            print("Loading "+str(cnt)+" vector")
            splitline = line.strip().split(',')
            #print(splitline)
            filename=splitline.pop(0)
            splitline.pop(-1)
            malwarename=splitline.pop(-1)
            try:
                for idx,value in enumerate(splitline):
                    if value == '-Infinity':
                        #print("INFINITY")
                        splitline[idx] = '0'
                    elif value == 'TRUE':
                        #print("TRUE")
                        splitline[idx] = '1'
                    elif value == 'FALSE':
                        #print("FALSE")
                        splitline[idx] = '0'
                    elif len(value) > 2:
                        if  (value[1] == '.' or value[2] == '.') and len(value) > 4:
                            #print(value)
                            splitline[idx] = truncate(value, 3)
                    if value == 'NaN':
                        #print('NaN')
                        splitline[idx] = '0'
            except:
                traceback.print_exc(file=sys.stdout)

            #print(splitline)
            lines.append(splitline)
            line = fp.readline()
            cnt += 1
    return lines

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


def integerise(lines):
    print("In integerise()")
    debugc = 0
    for line in lines:
        print("Integerising "+str(debugc)+" vector")
        debugc += 1
        for idx, value in enumerate(line):
            value = float(value)
            line[idx] = value
    return lines

def trim_vectors(vectors):
    vecIndex = 0
    for idx, vec in enumerate(vectors):
        valIndex = 0
        trim_vector(vec, vectors)
        print("Trimmed "+str(idx)+" vectors\n")

def trim_vector(vec, vectors):
    number_of_popped_indices = 0
    global elements_popped, number_of_elems
    for idx, elem in enumerate(vec):
        if elem != 0.0:
            if isZeroElement(idx,vectors):
                remove_index_from_all_vectors(idx, vectors)
                number_of_popped_indices += 1
    print("Popped "+str(number_of_popped_indices)+" elements from all vectors")
    print("Elements popped so far: "+str(elements_popped))
    percentage = (elements_popped/number_of_elems) * 100
    print("Percentage of total elements that has been popped: "+str(percentage)+"%")

def isZeroElement(id,vectors):
    isZeroElem = False
    count = 0
    for vec in vectors:
        if vec[id] != 0.0:
            count += 1
    if count < 2:
        isZeroElem = True
    return isZeroElem

def remove_index_from_all_vectors(idy,vectors):
    #print("Popping element "+str(idy))
    global elements_popped
    count = 0
    for vec in vectors:
        vec.pop(idy)
        count += 1
        elements_popped += 1


if __name__=="__main__":
    lines = load_vectors()
    vectors = integerise(lines)
    vectors = trim_vectors(vectors)
