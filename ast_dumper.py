#!/usr/bin/env python3
import sys
import clang.cindex

INDENT = 4
K = clang.cindex.CursorKind

def is_std_ns(node):
    return node.kind == K.NAMESPACE and node.spelling == 'std'

def vit(node: clang.cindex.Cursor, indent: int, saw):
    pre = ' ' * indent
    k = node.kind  # type: clang.cindex.CursorKind
    # skip printting UNEXPOSED_*
    if not k.is_unexposed():
        print(pre, end='')
        print(k.name, end=' ')
        if node.spelling:
            print('s:', node.spelling, end=' ')
            if node.type.spelling:
                print('t:', node.type.spelling, end=' ')
            # FIXME: print opcode or literal
        print()
    saw.add(node.hash)
    if node.referenced is not None and node.referenced.hash not in saw:
        vit(node.referenced, indent + INDENT, saw)
    # FIXME: skip auto generated decls
    skip = len([c for c in node.get_children()
                if indent == 0 and is_std_ns(c)])
    for c in node.get_children():
        if not skip:
            vit(c, indent + INDENT, saw)
        if indent == 0 and is_std_ns(c):
            skip -= 1
    saw.remove(node.hash)

def main():
    index = clang.cindex.Index.create()
    tu = index.parse(sys.argv[1])
    vit(tu.cursor, 0, set())

main()
