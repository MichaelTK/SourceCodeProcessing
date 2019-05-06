#!/usr/bin/python3
""" Usage: call with <filename> <typename>
"""

import sys
import clang.cindex


def find_typerefs(node):
    """ Find all references to the type named 'typename'
    """
    #if node.kind.is_reference():
        #ref_node = node.get_definition()
    #    print(node.spelling)
        #file.write(node.spelling)

        #if ref_node.spelling == typename:
        #    print 'Found %s [line=%s, col=%s]' % (
        #        typename, node.location.line, node.location.column)
    try:
        print(node.kind.name+": "+node.spelling)
    except:
        print("exception")
    #print(node.spelling)
    # Recurse for children of this node
    for c in node.get_children():
        find_typerefs(c)

    #if 'RC4Crypt' in str(node.displayname):
    #    print (str(node.displayname))
    #    print (node.location)
    #    print (node.type)
    #    print (node.kind)
    #    print (node.canonical)

index = clang.cindex.Index.create()
tu = index.parse(sys.argv[1])
print('Translation unit:', tu.spelling)
#f= open("BaseNodeDump.txt","w+")
find_typerefs(tu.cursor)
#f.close()
