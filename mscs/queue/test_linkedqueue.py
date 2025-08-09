import pytest

from .linkedqueue import LinkedQueue

def test_linkedqueue_enqueue():
    # arrange
    queue = LinkedQueue()
    elt = 'a'

    # act
    queue.enqueue(elt)

    # assert
    assert queue.getSize() == 1
    
    head = queue.getHead()
    assert head is not None
    assert head.getData() == elt

    tail = queue.getTail()
    assert tail is not None
    assert tail.getData() == elt

    assert queue.peek() == elt


def test_linkedqueue_enqueue2():
    # arrange
    queue = LinkedQueue()
    elt1 = 1
    elt2 = 2

    # act
    queue.enqueue(elt1)
    queue.enqueue(elt2)

    # assert
    assert queue.getSize() == 2
    
    head = queue.getHead()
    assert head is not None
    assert head.getData() == elt1

    tail = queue.getTail()
    assert tail is not None
    assert tail.getData() == elt2

    assert queue.peek() == elt1


def test_linkedqueue_dequeue():
    # arrange
    queue = LinkedQueue()
    elt1 = 1
    elt2 = 2

    # act
    queue.enqueue(elt1)
    queue.enqueue(elt2)

    dequeued = queue.dequeue()

    # assert
    assert dequeued == elt1

    assert queue.getSize() == 1
    
    head = queue.getHead()
    assert head is not None
    assert head.getData() == elt2

    tail = queue.getTail()
    assert tail is not None
    assert tail.getData() == elt2

    assert queue.peek() == elt2


def test_linkedqueue_empty():
    # arrange
    queue = LinkedQueue()
    elt = 'a'

    # act
    queue.enqueue(elt)

    # assert
    assert queue.getSize() == 1
    assert not queue.empty()
    

def test_linkedqueue_empty2():
    # arrange
    queue = LinkedQueue()

    # assert
    assert queue.getSize() == 0
    assert queue.empty()