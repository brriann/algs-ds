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

