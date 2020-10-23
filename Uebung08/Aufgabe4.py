import pprint
from typing import Any


class Tree:
    def __init__(self, main: Any = None, left: Any = None, right: Any = None):
        self.left = left
        self.right = right
        self.main = main

    def traverse(self):
        print(self.main)
        if self.left != None:
            try:
                self.left.traverse()
            except:
                print(self.left)
        if self.right != None:
            try:
                self.right.traverse()
            except:
                print(self.right)


root = Tree(
    main=15,
    left=Tree(
        main=5,
        left=3,
        right=Tree(main=12, left=Tree(main=10, left=Tree(main=6, right=7)), right=13),
    ),
    right=Tree(main=16, right=Tree(main=20, left=18, right=23)),
)

root.traverse()