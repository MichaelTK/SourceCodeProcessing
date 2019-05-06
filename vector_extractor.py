import fileinput
import sys

ARFF_FILE_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/SCAAarffs/"
VECTOR_FILE_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/vectors/"


filename = sys.argv[1] if len(sys.argv) >= 2 else 'defaultfile.arff'
copy = False
for line in fileinput.input(inplace=True): # edit files inplace
    if fileinput.isfirstline() or not copy: # reset `copy` flag for next file
       copy = "@data" in line
    if copy:
       print line, # copy line

with open(filename, 'r') as fin:
    data = fin.read().splitlines(True)
with open(filename, 'w') as fout:
    fout.writelines(data[1:])

def trim_arff_files():
    arffs = listdir_fullpath(ARFF_FILE_PATH)
    for arff in arffs:
        trim_arff_file(arff)

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

#if __name__ == '__main__':
#    trim_arff_files()
