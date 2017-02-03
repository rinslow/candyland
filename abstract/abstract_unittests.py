from abstract import Queue, Stack

import unittest


class QueueTest(unittest.TestCase):
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

    def test_init_queue(self):
        stack = Stack([1, 2, 3])
        self.assertEqual(len(stack), 3)
