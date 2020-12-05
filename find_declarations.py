#!/bin/python3

"""
Find all variable declarations in a program
"""

import clang.cindex
from clang.cindex import CursorKind, TypeKind

import argparse
import logging
import sys

log = logging.getLogger()
stdout_handler = logging.StreamHandler(sys.stdout)
verbose_fmt = logging.Formatter('%(levelname)s - %(message)s')
stdout_handler.setFormatter(verbose_fmt)
log.addHandler(stdout_handler)

def pp(node):
    """
    Return str of node for pretty print
    """
    return f'{node.displayname} ({node.kind}) [{node.location}]'

def find(node, kind):
    """
    Return all node's descendants of a certain kind
    """

    log.debug(f'find: walked node {pp(node)}')

    if node.kind == kind:
        yield node
    # Recurse for children of this node
    for child in node.get_children():
        yield from find(child, kind)

def get_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input_file', help="Path to the input file")
    return parser.parse_args()

def main():
    index = clang.cindex.Index.create()
    tu = index.parse('main.c')
    cur = tu.cursor
    funcdecls = find(cur, CursorKind.FUNCTION_DECL)
    for func in (f for f in funcdecls if f.location.file.name == 'main.c'):
        print(f'{func.location.file.name}:{func.location.line}', 'function', func.spelling)
        vardecls = find(func, CursorKind.VAR_DECL)
        for var in vardecls:
            print(f'{var.type.spelling} {var.spelling};')

if __name__ == "__main__":
    main()
