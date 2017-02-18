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
        if self.right_is_heavier():
            if self.right.left_is_heavier():
                return self.rotate_double_left()

            else:
                return self.rotate_left()

        elif self.left_is_heavier():
            if self.left.right_is_heavier():
                return self.rotate_double_right()

            else:
                return self.rotate_right()

        else:
            return self

    def rotate_left(self):
        if self.right is None:
            return self

        return AVLTree(self.right.value,
                       AVLTree(self.value,
                               self.left,
                               self.right.left),
                       self.right.right)

    def rotate_right(self):
        if self.left is None:
            return self

        return AVLTree(self.left.value,
                       self.left.left,
                       AVLTree(self.value,
                               self.left.right,
                               self.right))

    def rotate_double_right(self):
        if self.left is None:
            return self

        return AVLTree(self.value,
                       self.left.rotate_left(),
                       self.right).rotate_right()

    def rotate_double_left(self):
        if self.right is None:
            return self

        return AVLTree(self.value,
                       self.left,
                       self.right.rotate_right()).rotate_left()

    def right_is_heavier(self):
        balance = len(self.right) if self.right else 0 - len(
                self.left) if self.left else 0
        return balance >= 2

    def left_is_heavier(self):
        balance = len(self.right) if self.right else 0 - len(
                self.left) if self.left else 0
        return balance <= -2

    def pop(self, element):
        if self.value == element:
            # This is the element to be removed.
            if not self.right and not self.left:
                return None

            elif self.right and not self.left:
                return self.right

            elif self.left and not self.right:
                return self.left

            else:
                # We have two children
                sucessor = self.right
                while sucessor.left:
                    sucessor = sucessor.left

                return AVLTree(sucessor.value, self.left, self.right.pop(
                        sucessor.value)).balance()

        elif self.value > element:
            return AVLTree(self.value, self.left.pop(element),
                           self.right).balance()

        else:
            return AVLTree(self.value, self.left,
                           self.right.pop(element)).balance()

    def search(self, element):
        if element == self.value:
            return self

        elif element > self.value and self.right is not None:
            return self.right.search(element)

        elif element <= self.value and self.left is not None:
            return self.left.search(element)

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

    def is_balanced(self):
        left_height = len(self.left) if self.left else 0
        right_height = len(self.right) if self.right else 0

        if not abs(left_height - right_height) <= 1:
            return False

        if self.left and not self.left.is_balanced():
            return False

        if self.right and not self.right.is_balanced():
            return False

        return True

    @classmethod
    def make(cls, arr):
        tree = cls(arr[0], None, None)
        for var in arr[1:]:
            tree = tree.add(var)

        return tree
