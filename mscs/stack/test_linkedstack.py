import pytest

from .linkedstack import LinkedStack

def test_linkedstack_push():
    # arrange
    stack = LinkedStack()
    elt = 'a'

    # act
    stack.push(elt)

    # assert
    assert stack.getSize() == 1

    head = stack.getHead()
    assert head is not None
    assert head.getData() == elt

    assert stack.peek() == elt


def test_linkedstack_pop():
    # arrange
    stack = LinkedStack()
    elt1 = 1
    elt2 = 2

    # act
    stack.push(elt1)
    stack.push(elt2)

    popped = stack.pop()

    # assert
    assert popped == elt2

    assert stack.getSize() == 1
    
    head = stack.getHead()
    assert head is not None
    assert head.getData() == elt1

    assert stack.peek() == elt1

