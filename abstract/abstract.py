"""Provides immutable data structures for use in python."""
from immutable import Immutable


class Queue(Immutable):
    """Immutable queue.

    Attributes:
        _list (list): queue's implementation.
    """
    def __init__(self, queue=NotImplemented, *args):
        super(Queue, self).__init__()

        if type(queue) is int:
            self._list = [queue] + list(args)

        else:
            self._list = queue if queue is not NotImplemented else []

    def enqueue(self, obj):
        return Queue(self._list + [obj])

    def dequeue(self):
        return Queue(self._list[1:])

    def top(self):
        return self._list[0]

    def __len__(self):
        return len(self._list)


class Stack(Immutable):
    """Immutable stack.

    Attributes:
        _list (list): stacks's implementation.
    """
    def __init__(self, stack=NotImplemented, *args):
        super(Stack, self).__init__()
        if type(stack) is int:
            self._list = [stack] + list(args)

        else:
            self._list = stack if stack is not NotImplemented else []

    def push(self, obj):
        return Stack([obj] + self._list)

    def pop(self):
        return Stack(self._list[1:])

    def head(self):
        return self._list[0]

    def __len__(self):
        return len(self._list)
