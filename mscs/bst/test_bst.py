import pytest

from .bst import BST

def test_bst_add():
    bst = BST()
    values = [10, 5, 15, 3, 7, 12, 18]
    for v in values:
        bst.add(v)
    # Check that all values are present
    for v in values:
        assert bst.contains(v)
    # Optionally, check BST structure
    root = bst.getRoot()
    assert root is not None
    assert root.getData() == 10

    left = root.getLeft()
    assert left is not None
    assert left.getData() == 5

    right = root.getRight()
    assert right is not None
    assert right.getData() == 15