import unittest

from trees import BinaryTree


class BinaryTreeTest(unittest.TestCase):
    def test_init(self):
        tree = BinaryTree(None, None, 4)
        self.assertEqual(tree.value, 4)

    def test_add(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(None, BinaryTree(None,
                                                                 None,
                                                                 5),
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)

        tree = tree.add(11)
        expected_str = "8,4,2,6,5,13,10,11,16,15,18"
        self.assertEqual(str(tree), expected_str)

    def test_remove(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(BinaryTree(None,
                                                           None,
                                                           5),
                                                None,
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)

        expected_tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                              BinaryTree(None, None, 6),
                                              4),
                                   BinaryTree(BinaryTree(None,
                                                         None,
                                                         10),
                                              BinaryTree(
                                                      BinaryTree(None, None,
                                                                 15),
                                                      BinaryTree(None, None,
                                                                 18),
                                                      16),
                                              13),
                                   8)
        self.assertEqual(tree.remove(5), expected_tree)

    def test_str(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(BinaryTree(None,
                                                           None,
                                                           5),
                                                None,
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)

        expected_str = "8,4,2,6,5,13,10,16,15,18"
        self.assertEqual(expected_str, str(tree))

    def test_repr(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(None, BinaryTree(None,
                                                                 None,
                                                                 5),
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)
        self.assertEqual(eval(repr(tree)), tree)

    def test_in(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(BinaryTree(None,
                                                           None,
                                                           5),
                                                None,
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)

        self.assertIn(13, tree)
        self.assertIn(8, tree)
        self.assertIn(16, tree)
        self.assertIn(18, tree)
        self.assertIn(15, tree)
        self.assertIn(10, tree)
        self.assertIn(4, tree)
        self.assertIn(6, tree)
        self.assertIn(5, tree)
        self.assertNotIn(5.5, tree)
        self.assertIn(2, tree)

    def test_iter(self):
        tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(BinaryTree(None,
                                                           None,
                                                           5),
                                                None,
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8)

        expected_list = [8, 4, 2, 6, 5, 13, 10, 16, 15, 18]
        self.assertEqual(list(tree), sorted(expected_list))


class HeapTest(unittest.TestCase):
    def test_init_alot_of_numbers(self):
        pass

    def test_init_empty(self):
        pass

    def test_init_list(self):
        pass

    def test_init_abstract_data_type(self):
        pass

    def test_insert(self):
        pass

    def test_remove(self):
        pass

    def test_find_maximum(self):
        pass

    def test_delete_maximum(self):
        pass
