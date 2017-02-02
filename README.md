# candyland
Immutable Data Structures for python, for better OOP Programming and Safer Multi-threading.

## Currently Supported Data Structures
  - Queue
  - Stack

## Usage
### Stack
```python
from immutable import Stack
s = Stack(1, 2, 3)  # Can also: s = Stack() or s = Stack([1, 2, 3])
print s.push(7).head()  # Prints 7
print s.pop().head()  # Prints 2
print len(s)  # Prints 3
```

### Queue
```python
from immutable import Queue
q = Queue(1, 2, 3)  # Can also: q = Queue() or q = Queue([1, 2, 3])
print q.enqueue(7).top()  # Prints 1
print q.dequeue().top()  # Prints 1
print len(q)  # Prints 3
```

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
####  candyland's True Immutability stems from it's ability to equate based on an object's state and not by it's reference.
