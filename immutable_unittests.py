import immutable

import unittest


class ImmutabilityTest(unittest.TestCase):

    class ImmutableStub(immutable.Immutable):
        def __init__(self, val=0, val2=3):
            super(ImmutabilityTest.ImmutableStub, self).__init__()
            self.num = val
            self.num2 = val2

        def foo(self):
            pass

    def test_cannot_change_properties(self):
        with self.assertRaises(immutable.ImmutabilityException):
            stub = ImmutabilityTest.ImmutableStub()
            stub.num = 1

    def test_can_access_methods(self):
        stub = ImmutabilityTest.ImmutableStub()
        try:
            stub.foo()

        except immutable.ImmutabilityException:
            self.fail()

    def test_equality_by_state(self):
        stub1 = ImmutabilityTest.ImmutableStub(5, 4)
        stub2 = ImmutabilityTest.ImmutableStub(5, 4)

        self.assertEqual(stub1, stub2)

    def test_inequality_by_state(self):
        stub1 = ImmutabilityTest.ImmutableStub(5, 4)
        stub2 = ImmutabilityTest.ImmutableStub(5, 3)

        self.assertNotEqual(stub1, stub2)


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
        self.assertEqual(queue.top(), 1)

    def test_dequeue(self):
        queue = immutable.Queue(1, 2, 3).dequeue()
        self.assertEqual(queue.top(), 2)

    def test_top(self):
        queue = immutable.Queue(1, 2, 3)
        self.assertEqual(queue.top(), 1)

    def test_count(self):
        queue = immutable.Queue(1, 2, 3)
        self.assertEqual(queue.count(), 3)


class StackTest(unittest.TestCase):
    def test_count(self):
        self.assertEqual(immutable.Stack(1, 2, 3, 4).count(), 4)

    def test_head(self):
        self.assertEqual(immutable.Stack(1, 2, 3, 4).head(), 1)

    def test_push(self):
        self.assertEqual(immutable.Stack(1, 2, 3).push(0).head(), 0)

    def test_pop(self):
        self.assertEqual(immutable.Stack(1, 2, 3).pop().head(), 2)

    def test_init_empty(self):
        stack = immutable.Stack()
        self.assertEqual(stack.count(), 0)

    def test_init_lot_of_numbers(self):
        stack = immutable.Stack(1, 2, 3)
        self.assertEqual(stack.count(), 3)

    def test_init_queue(self):
        stack = immutable.Stack([1, 2, 3])
        self.assertEqual(stack.count(), 3)
