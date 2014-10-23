#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import json
import sys
from xmarks2html import BookTree
from jinja2 import Environment, PackageLoader


class Data:
    pass


def GetData(args):

    data = Data()
    data.Type = args['ntype']
    if 'url' in args:
        data.Url = args['url']
    else:
        data.Url=''

    data.Name = args.get('name', data.Url)

    return data


def main():
    if len(sys.argv)!=2:
        print 'Usage: python main.py path_to_xmarks_json_file'
        return

    json_file = sys.argv[1]

    with codecs.open(json_file, encoding='utf-8') as bookmarksFile:
        data = json.load(bookmarksFile)

    book_tree = BookTree()
    for command in data['commands']:
        if command['action'] == 'insert':
            args = command['args']
            book_tree.Add(command['nid'], args['pnid'], GetData(args))

    env = Environment(loader=PackageLoader('xmarks2html', ''))
    template = env.get_template('bookmarks.template')
    print template.render(tree=book_tree ).encode('utf-8')


if __name__ == "__main__":
    main()


