#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from xmarks2html import BookTree


def main():
    with open('bookmarks.txt') as bookmarksFile:
        data = json.load(bookmarksFile)

    book_tree = BookTree()
    for command in data['commands']:
        if command['action'] == 'insert':
            args = command['args']
            book_tree.Add(command['nid'], args['pnid'],
                          {'type': args['ntype'], 'url': args.get('url', None)})

if __name__ == "__main__":
    main()