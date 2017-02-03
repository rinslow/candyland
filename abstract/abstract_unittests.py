from abstract import Queue, Stack, List, KeyValuePair

import unittest


class QueueTest(unittest.TestCase):

    def test_different_inits_equal(self):
        q1 = Queue(1, 2)
        q2 = Queue().enqueue(1).enqueue(2)

        self.assertEqual(q1, q2)

    def test_init_empty(self):
        queue = Queue()
        self.assertEqual(len(queue), 0)

    def test_init_lot_of_numbers(self):
        queue = Queue(1, 2, 3)
        self.assertEqual(len(queue), 3)

    def test_init_queue(self):
        queue = Queue([1, 2, 3])
        self.assertEqual(len(queue), 3)

    def test_enqueue(self):
        queue = Queue(1, 2, 3).enqueue(4)
        self.assertEqual(queue.top(), 1)

    def test_dequeue(self):
        queue = Queue(1, 2, 3).dequeue()
        self.assertEqual(queue.top(), 2)

    def test_top(self):
        queue = Queue(1, 2, 3)
        self.assertEqual(queue.top(), 1)

    def test_count(self):
        queue = Queue(1, 2, 3)
        self.assertEqual(len(queue), 3)


class StackTest(unittest.TestCase):
    def test_count(self):
        self.assertEqual(len(Stack(1, 2, 3, 4)), 4)

    def test_head(self):
        self.assertEqual(Stack(1, 2, 3, 4).head(), 1)

    def test_push(self):
        self.assertEqual(Stack(1, 2, 3).push(0).head(), 0)

    def test_pop(self):
        self.assertEqual(Stack(1, 2, 3).pop().head(), 2)

    def test_init_empty(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)

    def test_init_lot_of_numbers(self):
        stack = Stack(1, 2, 3)
        self.assertEqual(len(stack), 3)

    def test_init_list(self):
        stack = Stack([1, 2, 3])
        self.assertEqual(len(stack), 3)


class ListTest(unittest.TestCase):
    def test_init_empty(self):
        l = List()
        self.assertEqual(len(l), 0)

    def test_init_lot_of_numbers(self):
        l = List(1, 2, 3)
        self.assertEqual(len(l), 3)

    def test_init_list(self):
        l = List([1, 2, 3])
        self.assertEqual(len(l), 3)

    def test_append(self):
        list1 = List().append(1).append(2)

        list2 = List(1, 2)
        self.assertEqual(list1, list2)

    def test_count(self):
        list1 = List(1, 2, 1, 4)
        self.assertEqual(list1.count(1), 2)

    def test_index(self):
        list1 = List(1, 2, 1, 4)
        self.assertEqual(list1.index(2), 1)

    def test_insert(self):
        list1 = List(1, 2, 3)
        expected_list = List(1, 7, 2, 3)
        actual_list = list1.insert(1, 7)

        self.assertEqual(expected_list, actual_list)

    def test_pop(self):
        list1 = List(1, 2, 3)
        expected_list = List(1, 3)
        actual_list = list1.pop(1)

        self.assertEqual(expected_list, actual_list)

    def test_pop_empty(self):
        list1 = List(1, 2, 3)
        expected_list = List(2, 3)
        actual_list = list1.pop()

        self.assertEqual(expected_list, actual_list)

    def test_remove(self):
        actual_list = List(1, 2, 3, 2, 2).remove(2)
        expected_list = List(1, 3)

        self.assertEqual(actual_list, expected_list)

    def test_extend(self):
        actual_list = List(1, 2).extend([1, 2])
        self.assertEqual(actual_list, List(1, 2, 1, 2))

    def test_reverse(self):
        self.assertEqual(List(1, 2, 3).reverse(), List(3, 2, 1))

    def test_sort(self):
        self.assertEqual(List(1, 2, 3, 0).sort(), List(0, 1, 2, 3))

    def test_iter(self):
        self.assertEqual(list(iter(List(1, 2, 3))), list(iter([1, 2, 3])))

    def test_add(self):
        self.assertEqual(List(1, 2) + List(3), List(1, 2, 3))

    def test_mul(self):
        self.assertEqual(List(1, 2) * 2, List(1, 2, 1, 2))

    def test_in(self):
        self.assertTrue(1 in List(2, 1, 2))

    def test_get_item(self):
        self.assertEqual(List(2, 1, 3)[2], 3)

    def test_len(self):
        self.assertEqual(len(List(2, 1, 3)), 3)

    def test_str(self):
        self.assertEqual(str(List(2, 1, 3)), str([2, 1, 3]))


class KeyValuePairTest(unittest.TestCase):
    def test_pair(self):
        kvp = KeyValuePair("Hello", "World")
        self.assertEqual(kvp.key(), "Hello")
        self.assertEqual(kvp.value(), "World")