![Candyland Sativa](http://i.imgur.com/pznIBJe.png)


# candyland
Immutable Data Structures for python.

### Why Should Objects Be Immutable?
This is an incomplete list of arguments in favor of immutability:

* immutable objects are simpler to construct, test, and use
* truly immutable objects are always thread-safe
* they help to avoid temporal coupling
* their usage is side-effect free (no defensive copies)
* identity mutability problem is avoided
* they always have failure atomicity
* they are much easier to cache
* they prevent NULL references, which are bad

(Taken from [Yegor Bugayenko's blog](http://www.yegor256.com/2014/06/09/objects-should-be-immutable.html).)


## Currently Supported Data Structures
  - [Queue](https://github.com/d-kiss/candyland/blob/master/abstract/queue.py)
  - [Stack](https://github.com/d-kiss/candyland/blob/master/abstract/stack.py)
  - [List](https://github.com/d-kiss/candyland/blob/master/abstract/list.py)
  - [Dictionary (Associative Array)](https://github.com/d-kiss/candyland/blob/master/abstract/dictionary.py)
  - [Set](https://github.com/d-kiss/candyland/blob/master/abstract/set.py)
  - [BinaryTree](https://github.com/d-kiss/candyland/blob/master/trees/binary_tree.py)
  - [Heap](https://github.com/d-kiss/candyland/blob/master/trees/heap.py)
  - [AVLTree](https://github.com/d-kiss/candyland/blob/master/trees/avl_tree.py)

## Upcoming:
  1. <strike> [Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))  </strike>
  2. <strike> [Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) </strike>
  3. <strike> [List](https://en.wikipedia.org/wiki/List_(abstract_data_type)) </strike>
  4. <strike>KeyValuePair</strike> (Who needs a key-value pair in python? <img src='https://www.bleepingcomputer.com/forums/public/style_emoticons/default/huh.gif'/>))
  5. <strike>[Set](https://en.wikipedia.org/wiki/Set_(abstract_data_type))</strike>
  6. [PriorityQueue](https://en.wikipedia.org/wiki/Priority_queue)
  7. [LinkedList](https://en.wikipedia.org/wiki/Linked_list)
  8. [SortedList](https://en.wikipedia.org/wiki/Ordered_list)
  9. <strike>[AVLTree](https://en.wikipedia.org/wiki/AVL_tree)</strike>
  10. [BinarySearchTree](https://en.wikipedia.org/wiki/Binary_search_tree)
  11. [RedBlackTree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
  12. <strike>[Heap](https://en.wikipedia.org/wiki/Heap_(data_structure))</strike>
  13. [HashTable](https://en.wikipedia.org/wiki/Hash_table)
  14. <strike>[Dictionary](https://en.wikipedia.org/wiki/Associative_array)</strike>
  15. <strike>[BinaryTree](https://en.wikipedia.org/wiki/Binary_tree)</strike>

* For suggestion you can [mail](mailto:speakupness@gmail.com) us
* Suggestions taken from [Wikipedia's Data Structures](https://en.wikipedia.org/wiki/List_of_data_structures)

## Usage

### Stack
```python
from immutable.abstract import Stack
s = Stack(1, 2, 3)  # Can also: s = Stack() or s = Stack([1, 2, 3])
print s.push(7).head()  # Prints 7
print s.pop().head()  # Prints 2
print s.count()  # Prints 3
```

### Queue
```python
from immutable.abstract import Queue
q = Queue(1, 2, 3)
print q.enqueue(7).head()  # Prints 1
print q.pop().head()  # Prints 1
print q.count()  # Prints 3
```

### List
```python
from immutable.abstact import List
l = List(1, 2, 3)
print 2 in l 
print l.reverse().append(3).remove(2).extend([1, 2]).pop(1).sort().insert(1, 3).count(3)
```

### Dictionary
```python
from immutable.abstract import Dictionary
d = Dictionary({1:2, 4:5})
d + Dictionary([(1, 2), (3, 4)]).append(4, 5).pop(1) + Dictionary.from_keys([1, 2], 0)
```

### Set
```python
from immutable.abstract import Set
print 1 in (Set(1, 2, 3) & Set(3, 4, 5) | [1, 2, 0] - [3, 4]).add(9).update(List(3,3)).pop().remove(2)
```

### BinaryTree
```python
from immutable.trees import BinaryTree
tree = BinaryTree(BinaryTree(BinaryTree(None, None, 2),
                                     BinaryTree(BinaryTree(None,
                                                           None,
                                                           5),
                                                None,
                                                6),
                                     4),
                          BinaryTree(BinaryTree(None,
                                                None,
                                                10),
                                     BinaryTree(BinaryTree(None, None, 15),
                                                BinaryTree(None, None, 18),
                                                16),
                                     13),
                          8) 
print tree, repr(tree), 13 in tree, 3.14 in tree, list(tree), iter(tree), tree.add(1).add(2).remove(3).remove(4) 

for x in BinaryTree.make([1, 2, 3, -1, 4, 7, 9, 14, 8, -23]):
  print x
```

### Heap
```python
from immutable.trees import Heap

h1 = Heap.make([1, 2, 3, 4, 5, 6, 10, 14, 11, 0, -2], min)  
h2 = Heap([1, 2, 3], max)
h3 = Heap([1, 2, 3])
# second parameter is an optional comparator, default is max.

print h1.add(1).pop(3).pop(4).add(20).head()
```

### AVLTree
```python
from immutable.trees import AVLTree
tree = AVLTree(1, None, None)
print 2 in tree.add(1).add(2).pop(4)
for x in AVLTree.make([1, 2, 3, -1, 4, 7, 9, 14, 8, -23]):
  print x
```

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
####  candyland's True Immutability stems from it's ability to equate based on an object's state and not by it's reference.
![](http://i.imgur.com/rWlnEwy.png)
