import pytest

from .arraystack import ArrayStack

def test_arraystack_push():
    # arrange
    stack = ArrayStack()
    elt = 'a'

    # act
    stack.push(elt)

    # assert
    assert stack.getSize() == 1

    assert stack.peek() == elt


def test_arraystack_push_resize():
    # arrange
    stack = ArrayStack()

    # act
    for elt in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        stack.push(elt)

    # assert
    assert stack.getSize() == 10

    assert stack.peek() == 9

    assert len(stack.getBackingArray()) == 18


def test_arraystack_pop():
    # arrange
    stack = ArrayStack()
    elt1 = 1
    elt2 = 2

    # act
    stack.push(elt1)
    stack.push(elt2)

    popped = stack.pop()

    # assert
    assert popped == elt2

    assert stack.getSize() == 1
    

    assert stack.peek() == elt1

