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
  - Queue
  - Stack
  - List

## Upcoming:
  1. <strike> Queue </strike>
  2. <strike> Stack </strike>
  3. <strike> List </strike>
  4. Set
  5. PriorityQueue
  6. LinkedList
  7. SortedList
  8. AVLTree
  9. BinarySearchTree
  10. RedBlackTree
  11. Heap
  12. HashMap

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

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
####  candyland's True Immutability stems from it's ability to equate based on an object's state and not by it's reference.
![](http://i.imgur.com/rWlnEwy.png)
