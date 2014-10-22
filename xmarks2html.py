#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import unittest


class TreeNode(object):
    def __init__(self):
        self.Childs = []

    def Add(self, node):
        self.Childs.append(node)


class BookTree(object):
    Root = None
    Nodes = {}
    def _GetNode(self, nodeId, listOfNodes):
        for testNode in listOfNodes:
            if testNode.Id == nodeId:
                return testNode

        for testNode in listOfNodes:
            result = self._GetNode(nodeId, testNode.Childs)
            if result:
                return result
        return None

    def Add(self, id, parentId, data):
        Node = TreeNode()
        Node.Id = id
        Node.Data = data
        if (parentId is None):
            self.Root = Node
        else:
            Parent = self._GetNode(parentId, [self.Root])
            Parent.Add(Node)
            Node.Parent = Parent
        self.Nodes[id]=Node
        return Node


def main():
    with open('bookmarks.txt') as bookmarksFile:
        data = json.load(bookmarksFile)

    book_tree = BookTree()
    for command in data['commands']:
        if command['action'] == 'insert':
            args = command['args']
            book_tree.Add(command['nid'], args['pnid'],
                          {'type': args['ntype'], 'url': args.get('url', None)})



class TestSequenceFunctions(unittest.TestCase):
    def test_tree(self):
        book_tree = BookTree()
        One=book_tree.Add(1, None, None)
        Two=book_tree.Add(2, 1, None)
        Three=book_tree.Add(3, 1, None)
        Four=book_tree.Add(4, 2, None)
        self.assertTrue(book_tree.Root == One)
        self.assertTrue(book_tree.Nodes[1] == One)
        self.assertTrue(book_tree.Nodes[3] == Three)
        self.assertTrue(Two.Id==2)
        self.assertTrue(Four.Parent==Two)

if __name__ == "__main__":
    unittest.main()