"""Provides immutable data structures for use in python."""
from collections import defaultdict


class Immutable(object):
    """Immutability class.

    Attributes:
        changed_values (dict): whether or not a property was set.
    """
    def __init__(self):
        self.__dict__["changed_values"] = defaultdict(bool)

    def __setattr__(self, key, value):
        if self.changed_values[key]:
            raise ImmutabilityException("Cannot change attribute %s." % key)

        self.__dict__[key] = value
        self.changed_values[key] = True

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.__class__.__name__ + "@" + str(self.__dict__))


class ImmutabilityException(Exception):
    """Occurs when trying to change an immutable object."""


class Queue(Immutable):
    """Immutable queue.

    Attributes:
        _list (list): queue's implementation.
    """
    def __init__(self, queue=NotImplemented, *args):
        super(Queue, self).__init__()

        # If we're given a lot of numbers
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
