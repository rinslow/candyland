from immutable import Immutable


class AVLTree(Immutable):
    """Immutable AVL Tree.

    Left child always smaller or equal to parent.
    Right child always bigger than the parent.

    Attributes:
        height (int): height of the tree.
        left (AVLTree): the left node of the avl tree.
        right (AVLTree): the right node of the avl tree.
        value (object): the tree's value.
    """

    def __init__(self, value, left, right):
        super(AVLTree, self).__init__()
        self.left = left
        self.right = right
        self.value = value
        self.height = 1 + max([len(child) if child is not None else 0 for
                               child in [left, right]])

    def add(self, element):
        if element > self.value:
            if self.right is not None:
                return AVLTree(self.value, self.left,
                               self.right.add(element)).balance()

            else:
                return AVLTree(self.value, self.left, AVLTree(element, None,
                                                              None)).balance()

        else:
            if self.left is not None:
                return AVLTree(self.value, self.left.add(element),
                               self.right).balance()

            else:
                return AVLTree(self.value, AVLTree(element, None, None),
                               self.right).balance()

    def balance(self):
        return self

    def rotate_right(self):
        pass

    def rotate_left(self):
        pass

    def rotate_double_right(self):
        pass

    def rotate_double_left(self):
        pass

    def right_is_heavier(self):
        pass

    def left_is_heavier(self):
        pass

    def pop(self, element):
        pass

    def delete(self, node):
        pass

    def search(self, element):
        pass

    def __contains__(self, item):
        if item == self.value:
            return True

        elif item > self.value and self.right is not None:
            return item in self.right

        elif item <= self.value and self.left is not None:
            return item in self.left

    def __str__(self):
        return ",".join(str(x) for x in list(self))

    def __iter__(self):
        if self.right:
            for right_child in self.right:
                yield right_child

        yield self.value

        if self.left:
            for left_child in self.left:
                yield left_child

    def __len__(self):
        return self.height

    def __cmp__(self, other):
        return cmp(self.value, other.value)

    def __repr__(self):
        return "%s(%s, %r, %r)" % (self.__class__.__name__,
                                   self.value, self.left, self.right)