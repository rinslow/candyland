import immutable

import unittest


class ImmutabilityTest(unittest.TestCase):

    class ImmutableStub(immutable.Immutable):
        def __init__(self):
            super(ImmutabilityTest.ImmutableStub, self).__init__()
            self.num = 0

        def foo(self):
            pass

    def test_cannot_change_properties(self):
        with self.assertRaises(immutable.ImmutabilityException):
            queue_stub = ImmutabilityTest.ImmutableStub()
            queue_stub.num = 1

    def test_can_access_methods(self):
        queue_stub = ImmutabilityTest.ImmutableStub()
        try:
            queue_stub.foo()

        except immutable.ImmutabilityException:
            pass


class QueueTest(unittest.TestCase):
    def test_init_empty(self):
        queue = immutable.Queue()
        self.assertEqual(queue.count(), 0)

    def test_init_lot_of_numbers(self):
        queue = immutable.Queue(1, 2, 3)
        self.assertEqual(queue.count(), 3)

    def test_init_queue(self):
        queue = immutable.Queue([1, 2, 3])
        self.assertEqual(queue.count(), 3)

    def test_enqueue(self):
        queue = immutable.Queue(1, 2, 3).enqueue(4)
        self.assertEqual(queue.count(), 4)

    def test_dequeue(self):
        queue = immutable.Queue(1, 2, 3).dequeue()
        self.assertEqual(queue.count(), 2)

    def test_top(self):
        queue = immutable.Queue(1, 2, 3)
        self.assertEqual(queue.top(), 3)

    def test_count(self):
        queue = immutable.Queue(1, 2, 3)
        self.assertEqual(queue.count(), 3)
