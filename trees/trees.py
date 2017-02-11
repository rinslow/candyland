"""Provides immutable tree data structures for use in python."""
from immutable import Immutable


class BinaryTree(Immutable):
    """Immutable Binary Tree.

    Left child always smaller than the parent.
    Right child always bigger than the parent.
    Each element exists only once in a binary tree.

    Attributes:
        left (BinaryTree): left node.
        right (BinaryTree): right node.
        value (object): node's value.
    """
    def __init__(self, left, right, value):
        super(BinaryTree, self).__init__()
        self.value = value
        self.right = right
        self.left = left

    def add(self, element):
        if self.value == element:
            return self  # Element already exists

        return self.add_subtree(BinaryTree(None, None, element))

    def add_subtree(self, subtree):
        if subtree is None:
            return self

        if self.value == subtree.value:
            # Need to merge subtree's children with this tree's children
            new_left = (self.left.add_subtree(subtree.left)
                        if self.left is not None else subtree.left)
            new_right = (self.right.add_subtree(subtree.right)
                         if self.right is not None else subtree.right)
            return BinaryTree(new_left, new_right, self.value)

        elif subtree.value > self.value:  # Element goes on right
            if self.right is not None:
                return BinaryTree(self.left, self.right.add_subtree(subtree),
                                  self.value)
            else:
                return BinaryTree(self.left, subtree, self.value)

        else:  # Element goes on the left
            if self.left is not None:
                return BinaryTree(self.left.add_subtree(subtree), self.right,
                                  self.value)

            else:
                return BinaryTree(subtree, self.right, self.value)

    def remove(self, element):
        if self.value == element:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            return self.left.add_subtree(self.right)

        if self.value < element and self.right is not None:
            return BinaryTree(self.left, self.right.remove(element), self.value)

        elif self.value > element and self.left is not None:
            return BinaryTree(self.left.remove(element), self.right, self.value)

        return self  # Element Not Found

    def __contains__(self, item):
        if self.value == item:
            return True

        elif item > self.value:
            return item in self.right if self.right is not None else False

        else:
            return item in self.left if self.left is not None else False

    def __str__(self):
        return ",".join(str(value) for value in filter(lambda x: x is not None,
                                                       [self.value,
                                                        self.left,
                                                        self.right]))

    def __repr__(self):
        return "%s(%s, %s, %s)" % (self.__class__.__name__,
                                   repr(self.left),
                                   repr(self.right),
                                   repr(self.value))

    def __iter__(self):
        if self.left:
            for left_num in self.left:
                yield left_num

        yield self.value

        if self.right:
            for right_num in self.right:
                yield right_num


class Heap(Immutable):
    """Immutable heap.

    Attributes:

    """
    pass
