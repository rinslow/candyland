from immutable import Immutable


class Heap(Immutable):
    """Immutable maximum heap.

    In order to take a list and make a heap out of it you must call
    Heap.make()! and not Heap's constructor!

    comparator should accept *args of arguments and retrieve one of them back.

    Attributes:
        array (list): the heap surfaced to a list.
        comparator (func): function that determines who's on top of the heap.

    """

    def __init__(self, array=None, comparator=max):
        super(Heap, self).__init__()

        self.comparator = comparator

        if array is None:
            self.array = []

        else:
            self.array = array

    def head(self):
        return self.array[0]

    @classmethod
    def make(cls, arr, comparator=max):
        """Make a heap from an unheapified list.

        Args:
            arr (list): list to make the heap from.
            comparator (function): the comparing function of the heap.

        Returns:
            Heap. a heap with all of arr's variables.
        """
        heap = Heap(comparator=comparator)
        for obj in arr:
            heap = heap.add(obj)

        return heap

    def add(self, element):
        return Heap(self.array[:] + [element],
                    self.comparator).sift_up(len(self.array))

    def sift_up(self, item_idx):
        arr = self.array[:]
        while item_idx > 0:
            parent_idx = int((item_idx + 1) / 2) - 1

            if self.comparator(arr[item_idx],
                               arr[parent_idx]) == arr[parent_idx]:
                return Heap(arr, self.comparator)

            arr[parent_idx], arr[item_idx] = arr[item_idx], arr[parent_idx]
            item_idx = parent_idx

        return Heap(arr, self.comparator)

    def sift_down(self, item_idx):
        arr = self.array[:]
        while True:
            left_idx, right_idx = ((item_idx + 1) * 2) - 1, (item_idx + 1) * 2
            if left_idx >= len(arr) or right_idx >= len(arr):
                # There are no two children
                if left_idx > len(arr) and self.comparator(arr[right_idx],
                                                           arr[item_idx]) == \
                        arr[right_idx]:
                    arr[item_idx], arr[right_idx] = (arr[right_idx],
                                                     arr[item_idx])
                    item_idx = right_idx
                    continue

                elif right_idx > len(arr) and self.comparator(arr[left_idx],
                                                              arr[item_idx]) \
                        == arr[left_idx]:
                    arr[item_idx], arr[left_idx] = (arr[left_idx],
                                                    arr[item_idx])
                    item_idx = left_idx
                    continue

                else:
                    break

            if self.comparator(arr[item_idx],
                               arr[left_idx],
                               arr[right_idx]) == arr[item_idx]:
                # Children are smaller
                break

            biggest = self.comparator(arr[left_idx], arr[right_idx])
            biggest_idx = {arr[left_idx]: left_idx,
                           arr[right_idx]: right_idx}.get(biggest)

            arr[item_idx], arr[biggest_idx] = arr[biggest_idx], arr[item_idx]
            item_idx = biggest_idx

        return Heap(arr, self.comparator)

    def pop(self):
        return Heap(self.array[-1:] + self.array[1:-1]).sift_down(0)

    def __iter__(self):
        return iter(self.array)

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self.array))

    def __str__(self):
        return str(self.array)

    def __contains__(self, item):
        return item in self.array

    def __len__(self):
        return len(self.array)
