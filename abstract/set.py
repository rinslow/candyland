import copy

from immutable import Immutable


class Set(Immutable):
    """Immutable set.

    Attributes:
        _list (list): set's implementation.
    """
    def __init__(self, _list=NotImplemented, *args):
        super(Set, self).__init__()
        if type(_list) not in (list, set) and _list is not NotImplemented:
            self._list = list(set([_list] + list(args)))

        else:
            self._list = list(set(copy.copy(_list)
                                  if _list is not NotImplemented else []))

    def add(self, p_object):
        return Set(list(set(self._list + [p_object])))

    def count(self, value):
        return self._list.count(value)

    def pop(self):
        index = 0
        return Set([item for (idx, item) in enumerate(self._list)
                    if idx != index])

    def remove(self, value):
        if value not in self:
            raise KeyError

        return self.discard(value)

    def discard(self, value):
        return Set([item for item in self._list if item != value])

    def update(self, iterable):
        return Set(list(set(self._list + list(iterable))))

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

    def __xor__(self, other):
        return Set(set(self._list).symmetric_difference(other))

    def __or__(self, other):
        return self.update(other)

    def __and__(self, other):
        return Set(set(self._list).intersection(other))

    def __sub__(self, other):
        return Set(set(self._list).difference(other))
