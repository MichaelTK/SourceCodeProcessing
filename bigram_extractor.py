#!/usr/bin/python3
""" Usage: call with <filename> <typename>
"""

import sys
import os
import clang.cindex

SOURCE_PATH="/home/k1462425/Documents/Research/ZooTestSubset/2015/"
#BASE_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/2015/Alina/Base2.cpp"
#ASTDUMP_PATH="/home/k1462425/Documents/Research/MalwareSourceTestSet/2015/Alina/Base2.astdump"

translation_unit = ""
function_name = ""

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def append_to_nodes(parentNode, childNode, file):
    #print("Appending to nodes!")
    global function_name, translation_unit
    try:
        if "TRANSLATION_UNIT" in parentNode.kind.name:
            translation_unit = parentNode.spelling
        if parentNode.kind.name != "FUNCTION_DECL" and parentNode.kind.name != "DECL_STMT" and parentNode.kind.name != "IF_STMT" and parentNode.kind.name != "FOR_STMT" and parentNode.kind.name != "NULL_STMT" and parentNode.kind.name != "BREAK_STMT" and parentNode.kind.name != "RETURN_STMT" and parentNode.kind.name != "COMPOUND_STMT" and parentNode.kind.name != "UNEXPOSED_EXPR" and parentNode.kind.name != "UNEXPOSED_DECL" and parentNode.kind.name != "TRANSLATION_UNIT" and parentNode.kind.name != "VAR_DECL" and parentNode.kind.name != "CXX_BOOL_LITERAL_EXPR" and parentNode.kind.name != "ARRAY_SUBSCRIPT_EXPR" and parentNode.kind.name != "CSTYLE_CAST_EXPR" and parentNode.kind.name != "BINARY_OPERATOR" and parentNode.kind.name != "PAREN_EXPR" and parentNode.kind.name != "DECL_REF_EXPR" and parentNode.kind.name != "CALL_EXPR" and parentNode.kind.name != "INTEGER_LITERAL" and parentNode.kind.name != "STRING_LITERAL" and parentNode.kind.name != "CXX_BOOL_LITERAL_EXPR" and parentNode.kind.name != "CHARACTER_LITERAL" and parentNode.kind.name != "PARM_DECL" and parentNode.kind.name != "UNARY_OPERATOR" and parentNode.kind.name != "SWITCH_STMT" and parentNode.kind.name != "CASE_STMT" and parentNode.kind.name != "DEFAULT_STMT" and parentNode.kind.name != "WHILE_STMT" and parentNode.kind.name != "DO_STMT" and parentNode.kind.name != "CONDITIONAL_OPERATOR" and parentNode.kind.name != "INIT_LIST_EXPR" and parentNode.kind.name != "NAMESPACE" and parentNode.kind.name != "TYPE_REF" and parentNode.kind.name != "ENUM_DECL" and parentNode.kind.name != "ENUM_CONSTANT_DECL" and parentNode.kind.name != "FIELD_DECL" and parentNode.kind.name != "STRUCT_DECL" and parentNode.kind.name != "FUNCTION_TEMPLATE" and parentNode.kind.name != "GOTO_STMT" and parentNode.kind.name != "LABEL_STMT" and parentNode.kind.name != "CONSTRUCTOR" and parentNode.kind.name != "CLASS_DECL" and parentNode.kind.name != "CXX_METHOD" and parentNode.kind.name != "DESTRUCTOR" and parentNode.kind.name != "MEMBER_REF_EXPR" and parentNode.kind.name != "COMPOUND_ASSIGNMENT_OPERATOR" and parentNode.kind.name != "CXX_UNARY_EXPR" and parentNode.kind.name != "TYPEDEF_DECL" and parentNode.kind.name != "UNION_DECL" and parentNode.kind.name != "UNEXPOSED_ATTR":
            print("ERROR! NO RECOGNIZED STATEMENT TYPE: "+parentNode.kind.name)
            return
        if childNode.kind.name != "FUNCTION_DECL" and childNode.kind.name != "DECL_STMT" and childNode.kind.name != "IF_STMT" and childNode.kind.name != "FOR_STMT" and childNode.kind.name != "NULL_STMT" and childNode.kind.name != "BREAK_STMT" and childNode.kind.name != "RETURN_STMT" and childNode.kind.name != "COMPOUND_STMT" and childNode.kind.name != "UNEXPOSED_EXPR" and childNode.kind.name != "UNEXPOSED_DECL" and childNode.kind.name != "TRANSLATION_UNIT" and childNode.kind.name != "VAR_DECL" and childNode.kind.name != "CXX_BOOL_LITERAL_EXPR" and childNode.kind.name != "ARRAY_SUBSCRIPT_EXPR" and childNode.kind.name != "CSTYLE_CAST_EXPR" and childNode.kind.name != "BINARY_OPERATOR" and childNode.kind.name != "PAREN_EXPR" and childNode.kind.name != "DECL_REF_EXPR" and childNode.kind.name != "CALL_EXPR" and childNode.kind.name != "INTEGER_LITERAL" and childNode.kind.name != "STRING_LITERAL" and childNode.kind.name != "CXX_BOOL_LITERAL_EXPR" and childNode.kind.name != "CHARACTER_LITERAL" and childNode.kind.name != "PARM_DECL" and childNode.kind.name != "UNARY_OPERATOR" and childNode.kind.name != "SWITCH_STMT" and childNode.kind.name != "CASE_STMT" and childNode.kind.name != "DEFAULT_STMT" and childNode.kind.name != "WHILE_STMT" and childNode.kind.name != "DO_STMT" and childNode.kind.name != "CONDITIONAL_OPERATOR" and childNode.kind.name != "INIT_LIST_EXPR" and childNode.kind.name != "NAMESPACE" and childNode.kind.name != "TYPE_REF" and childNode.kind.name != "ENUM_DECL" and childNode.kind.name != "ENUM_CONSTANT_DECL" and childNode.kind.name != "FIELD_DECL" and childNode.kind.name != "STRUCT_DECL" and childNode.kind.name != "FUNCTION_TEMPLATE" and childNode.kind.name != "GOTO_STMT" and childNode.kind.name != "LABEL_STMT" and childNode.kind.name != "CONSTRUCTOR" and childNode.kind.name != "CLASS_DECL" and childNode.kind.name != "CXX_METHOD" and childNode.kind.name != "DESTRUCTOR" and childNode.kind.name != "MEMBER_REF_EXPR" and childNode.kind.name != "COMPOUND_ASSIGNMENT_OPERATOR" and childNode.kind.name != "CXX_UNARY_EXPR" and childNode.kind.name != "TYPEDEF_DECL"and childNode.kind.name != "UNION_DECL" and childNode.kind.name != "UNEXPOSED_ATTR":
            print("ERROR! NO RECOGNIZED STATEMENT TYPE: "+childNode.kind.name)
            return
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

        parent_node_combined = parent_node_kind_name+","+parent_node_spelling+","+parent_token_spelling+","+function_name+","+translation_unit
        #print(parent_node_combined)
        child_node_combined = child_node_kind_name+","+child_node_spelling+","+child_token_spelling+","+function_name+","+translation_unit
        #print(child_node_combined)
        pair = (parent_node_combined, child_node_combined)
        #print(pair)
        #nodes.append(pair)
        FILENAME=file[:-5]+".astdump"
        write_nodes_to_file(pair,FILENAME)
        #print(nodes[-1])
    except:
        print("Some kind of format/encoding error probably.")

def write_nodes_to_file(pair, FILENAME):

    f=open(FILENAME,"a+")

    parent=pair[0]
    child=pair[1]

    f.write(parent+"\n")
    f.write(child+"\n\n")

    f.close()

def extract_bigrams(node,file):
    """ Find all node bigrams. """
    global bigrams, function_name

    children = node.get_children()
    for child in children:
        if node.kind.name == "FUNCTION_DECL":
            print(node.spelling)
            function_name = node.spelling
        pair = (node, child)
        #bigrams.append(pair)
        append_to_nodes(pair[0],pair[1],file)
        extract_bigrams(child,file)

def extract_bigrams_from_file(file):
    global nodes, bigrams
    index = clang.cindex.Index.create()
    tu = index.parse(file)

    extract_bigrams(tu.cursor,file)
    #extract_nodes(tu.cursor)
    #nodes = []
    #bigrams = []

def remove_duplicate_bigrams():
    global global_bigrams
    global_bigrams = list(set(global_bigrams))

def main():
    global BASE_PATH, ASTDUMP_PATH

    directories = listdir_fullpath(SOURCE_PATH)

    for dir in directories:
        files = listdir_fullpath(dir)
        for file in files:
            if file.endswith("2.cpp"):
                print("Extracting bigrams from: "+file)
                exists = os.path.isfile(file[:-5]+".astdump")
                if exists:
                    os.remove(file[:-5]+".astdump")
                extract_bigrams_from_file(file)

    #extract_bigrams_from_file(BASE_PATH)


main()
