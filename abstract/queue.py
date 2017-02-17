import copy

from immutable import Immutable


class Queue(Immutable):
    """Immutable queue.

    Attributes:
        _list (list): queue's implementation.
    """
    def __init__(self, queue=NotImplemented, *args):
        super(Queue, self).__init__()

        if type(queue) not in (list, set) and queue is not NotImplemented:
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
