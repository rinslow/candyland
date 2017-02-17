import copy

from immutable import Immutable


class Stack(Immutable):
    """Immutable stack.

    Attributes:
        _list (list): stacks's implementation.
    """
    def __init__(self, stack=NotImplemented, *args):
        super(Stack, self).__init__()
        if type(stack) not in (list, set) and stack is not NotImplemented:
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
