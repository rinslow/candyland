![Candyland Sativa](http://i.imgur.com/pznIBJe.png)


# candyland
Immutable Data Structures for python, for better OOP Programming and Safer Multi-threading.

## Currently Supported Data Structures
  - Queue
  - Stack
  - List
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
