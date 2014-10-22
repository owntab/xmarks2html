#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from xmarks2html import BookTree
from jinja2 import Environment, PackageLoader

def main():
    with open('bookmarks.txt') as bookmarksFile:
        data = json.load(bookmarksFile)

    book_tree = BookTree()
    for command in data['commands']:
        if command['action'] == 'insert':
            args = command['args']
            book_tree.Add(command['nid'], args['pnid'],
                          {'type': args['ntype'], 'url': args.get('url', None)})

    env = Environment(loader=PackageLoader('xmarks2html', ''))
    template = env.get_template('bookmarks.template')
    print template.render(tree=book_tree)


if __name__ == "__main__":
    main()


