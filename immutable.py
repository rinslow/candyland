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


class ImmutabilityException(Exception):
    """Occurs when trying to change an immutable object."""


class Queue(Immutable):
    """Immutable queue.

    Attributes:
        _list (list): amount of list in the queue.
    """
    def __init__(self, queue=NotImplemented, *args):

        # If we're given alot of numbers
        super(Queue, self).__init__()
        if type(queue) is int:
            self._list = [queue] + list(args)

        else:
            self._list = queue if queue is not NotImplemented else []

    def enqueue(self, obj):
        return Queue(self._list + [obj])

    def dequeue(self):
        return Queue(self._list[:-1])

    def top(self):
        return self._list[-1]

    def count(self):
        return len(self._list)
