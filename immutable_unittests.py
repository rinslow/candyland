import unittest

import immutable


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
