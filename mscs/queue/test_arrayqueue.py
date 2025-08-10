import pytest

from .arrayqueue import ArrayQueue

def test_arrayqueue_enqueue():
    # arrange
    queue = ArrayQueue()
    elt = 'a'

    # act
    queue.enqueue(elt)

    # assert
    assert queue.getSize() == 1
    assert queue.peek() == elt


def test_arrayqueue_enqueue2():
    # arrange
    queue = ArrayQueue()
    elt1 = 1
    elt2 = 2

    # act
    queue.enqueue(elt1)
    queue.enqueue(elt2)

    # assert
    assert queue.getSize() == 2
    assert queue.peek() == elt1


def test_arrayqueue_enqueue_resize():
    # arrange
    queue = ArrayQueue()

    # act
    for elt in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        queue.enqueue(elt)

    # assert
    assert queue.getSize() == 10
    assert queue.peek() == 0

    assert len(queue.getBackingArray()) == 18


def test_arrayqueue_dequeue():
    # arrange
    queue = ArrayQueue()
    elt1 = 1
    elt2 = 2

    # act
    queue.enqueue(elt1)
    queue.enqueue(elt2)

    dequeued = queue.dequeue()

    # assert
    assert dequeued == elt1

    assert queue.getSize() == 1
    assert queue.peek() == elt2


def test_arrayqueue_dequeue_resize():
    # arrange
    queue = ArrayQueue()

    # act
    for elt in [0, 1, 2, 3, 4, 5]:
        queue.enqueue(elt)

    dq1 = queue.dequeue()
    dq2 = queue.dequeue()

    for elt in [6, 7, 8, 9, 10, 11]:
        queue.enqueue(elt)

    # assert
    assert dq1 == 0
    assert dq2 == 1

    assert queue.getSize() == 10
    assert queue.peek() == 2

    assert len(queue.getBackingArray()) == 18


def test_arrayqueue_empty():
    # arrange
    queue = ArrayQueue()
    elt = 'a'

    # act
    queue.enqueue(elt)

    # assert
    assert queue.getSize() == 1
    assert not queue.empty()
    

def test_arrayqueue_empty2():
    # arrange
    queue = ArrayQueue()

    # assert
    assert queue.getSize() == 0
    assert queue.empty()