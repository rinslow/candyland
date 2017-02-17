import copy

from abstract import List
from immutable import Immutable


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
            #  We'll assume we've got a list of tuples
            self._dict = dict(list(var))

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
        return [(k, v) for (k, v) in self._dict.iteritems()]

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
