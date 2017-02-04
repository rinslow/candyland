"""Provides immutable data structures for use in python."""
import copy

from immutable import Immutable


COLLECTIONS = (list, tuple, set, frozenset)


class Queue(Immutable):
    """Immutable queue.

    Attributes:
        _list (list): queue's implementation.
    """
    def __init__(self, queue=NotImplemented, *args):
        super(Queue, self).__init__()

        if type(queue) not in COLLECTIONS and queue is not NotImplemented:
            self._list = [queue] + list(args)

        else:
            self._list = copy.copy(queue) if queue is not NotImplemented else []

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
        if type(stack) not in COLLECTIONS and stack is not NotImplemented:
            self._list = [stack] + list(args)

        else:
            self._list = copy.copy(stack) if stack is not NotImplemented else []

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
        if type(_list) not in COLLECTIONS and _list is not NotImplemented:
            self._list = [_list] + list(args)

        else:
            self._list = copy.copy(_list) if _list is not NotImplemented else []

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


class Dictionary(Immutable):
    """Immutable dictionary.

    Attributes:
        _dict (dict): dictionary's implementation.
    """
    def __init__(self, var=NotImplemented):
        super(Dictionary, self).__init__()
        if type(var) is dict:
            self._dict = var.copy()

        elif isinstance(var, (list, tuple, List)):
            #  We'll assume we've got a list of KeyValuePair.
            self._dict = dict(((pair.key(), pair.value()) for pair in var))

        elif var is NotImplemented or var is None:
            self._dict = dict()

        else:
            raise TypeError("Couldn't instansiate Dictionary object with "
                            "variable of class %s " % type(var).__name__)

    def clear(self):
        return Dictionary()

    def copy(self):
        return Dictionary(copy.deepcopy(self._dict))

    # noinspection PyMethodOverriding
    @classmethod
    def fromkeys(cls, keys, values=None):
        return cls(dict.fromkeys(keys, values))

    def get(self, key, default=None):
        return self._dict.get(key, default)

    def has_key(self, key):
        return key in self._dict

    def items(self):
        return copy.deepcopy(self._dict).items()

    def itervalues(self):
        return iter(copy.deepcopy(self._dict).values())

    def iteritems(self):
        return copy.deepcopy(self._dict).iteritems()

    def iterkeys(self):
        return iter(copy.deepcopy(self._dict).keys())

    def to_list(self):
        return [KeyValuePair(k, v) for (k, v) in self._dict.iteritems()]

    def __iter__(self):
        return self.iterkeys()

    def __len__(self):
        return len(self._dict.keys())

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return self.has_key(item)

    def __add__(self, other):
        if isinstance(other, Dictionary):
            return Dictionary(self._dict.copy()).update(other)

        elif isinstance(other, dict):
            return Dictionary(self._dict.copy()).update(other)

        else:
            raise TypeError("Cannot add Dictionary to %s" %
                            type(other).__name__)

    def __str__(self):
        return str(self._dict)

    def append(self, key, value):
        return Dictionary(self._dict).update(Dictionary({key: value}))

    def update(self, other=None):
        if type(other) is dict:
            cpy = self._dict.copy()
            cpy.update(other)
            return Dictionary(cpy)

        elif type(other) is Dictionary:
            return self.update(dict(other.items()))

        else:
            raise TypeError("cannot update Dictionary and %s" % type(other))

    def viewvalues(self):
        return self._dict.viewvalues()

    def viewkeys(self):
        return self._dict.viewkeys()

    def viewitems(self):
        return self._dict.viewitems()

    def setdefault(self, key, default=None):
        if key in self:
            return self

        else:
            return Dictionary(self._dict).append(key, default)

    def pop(self, k):
        return Dictionary(dict([(key, value) for (key, value) in
                                self._dict.items() if key != k]))


class Set(Immutable):
    """Immutable set.

    Attributes:
        _list (list): set's implementation.
    """
    def __init__(self, _list=NotImplemented, *args):
        super(Set, self).__init__()
        if type(_list) not in COLLECTIONS and _list is not NotImplemented:
            self._list = list(set([_list] + list(args)))

        else:
            self._list = list(set(copy.copy(_list)
                                  if _list is not NotImplemented else []))

    def append(self, p_object):
        return Set(list(set(self._list + [p_object])))

    def count(self, value):
        return self._list.count(value)

    def index(self, value, start=None, stop=None):
        for var, index in enumerate(self._list[start:stop]):
            if var == value:
                return index

    def insert(self, index, p_object):
        return Set(list(set(self._list[:index] +
                            [p_object] +
                            self._list[index:])))

    def pop(self, index=None):
        index = index if index is not None else 0
        return Set([item for (idx, item) in enumerate(self._list)
                    if idx != index])

    def remove(self, value):
        return Set([item for item in self._list if item != value])

    def extend(self, iterable):
        return Set(list(set(self._list + iterable)))

    def reverse(self):
        return Set(self._list[::-1])

    def sort(self, compareable=None, key=None, reverse=False):
        return Set(sorted(self._list), compareable, key, reverse)

    def __iter__(self):
        return iter(self._list)

    def __add__(self, other):
        return Set(list(set(self._list + list(other))))

    def __contains__(self, item):
        return item in self._list

    def __getitem__(self, item):
        return self._list[item]

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return str(self._list)
