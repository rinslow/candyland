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

    def __str__(self):
        return str(self._list)

    def __iter__(self):
        return iter(self._list)


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

    def __str__(self):
        return str(self._list)

    def __iter__(self):
        return iter(self._list)


class List(Immutable):
    """Immutable list.

    Attributes:
        _list (list): list's implementation.
    """
    def __init__(self, _list=NotImplemented, *args):
        super(List, self).__init__()
        if type(_list) is int:
            self._list = [_list] + list(args)

        else:
            self._list = _list if _list is not NotImplemented else []

    def append(self, p_object):
        return List(self._list + [p_object])

    def count(self, value):
        return self._list.count(value)

    def index(self, value, start=None, stop=None):
        for var, index in enumerate(self._list[start:stop]):
            if var == value:
                return index

    def insert(self, index, p_object):
        return List(self._list[:index] + [p_object] + self._list[index:])

    def pop(self, index=None):
        index = index if index is not None else 0
        return List([item for (idx, item) in enumerate(self._list) if idx !=
                     index])

    def remove(self, value):
        return List([item for item in self._list if item != value])

    def extend(self, iterable):
        return List(self._list + iterable)

    def reverse(self):
        return List(self._list[::-1])

    def sort(self, compareable=None, key=None, reverse=False):
        return List(sorted(self._list), compareable, key, reverse)

    def __iter__(self):
        return iter(self._list)

    def __add__(self, other):
        return List(self._list + list(other))

    def __mul__(self, other):
        return List(self._list * other)

    def __contains__(self, item):
        return item in self._list

    def __getitem__(self, item):
        return self._list[item]

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return str(self._list)


class KeyValuePair(Immutable):
    """Immutable key-value pair.

    Attributes:
        _key (object): pair's key.
         _value (object): pair's value.
    """
    def __init__(self, key, value):
        super(KeyValuePair, self).__init__()
        self._key = key
        self._value = value

    def key(self):
        return self._key

    def value(self):
        return self._value
