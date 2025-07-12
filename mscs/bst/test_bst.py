import pytest

from .bst import BST

def test_bst_add():
    # arrange
    bst = BST()
    values = [10, 5, 15, 3, 7, 12, 18]

    # act
    for v in values:
        bst.add(v)

    # assert
    assert bst.getSize() == len(values)
    for v in values:
        assert bst.contains(v)

    root = bst.getRoot()
    assert root is not None
    assert root.getData() == 10

    left = root.getLeft()
    assert left is not None
    assert left.getData() == 5

    right = root.getRight()
    assert right is not None
    assert right.getData() == 15


'''
              1
             / \
            0   2
                 \
                  3
                   \
                    4

            ->

              1
             / \
            0   3
                 \
                  4
'''
def test_bst_remove():
    # arrange
    bst = BST()
    values = [1, 0, 2, 3, 4]
    expected_in_order_final = [0, 1, 3, 4]

    for v in values:
        bst.add(v)

    # act
    result = bst.remove(2)

    # assert
    assert result == 2
    assert bst.getSize() == len(values) - 1
    assert bst.inOrder() == expected_in_order_final


'''
              1
             / \
            0   2
                 \
                  3
                   \
                    4

            ->

              2
             / \
            0   3
                 \
                  4
'''
def test_bst_remove_2():
    # arrange
    bst = BST()
    values = [1, 0, 2, 3, 4]
    expected = [0, 2, 3, 4]

    for v in values:
        bst.add(v)

    # act
    result = bst.remove(1)

    # assert
    assert result == 1
    assert bst.inOrder() == expected


def test_bst_contains():
    # arrange
    bst = BST()
    values = ['c', 'b', 'd', 'a', 'e']

    for v in values:
        bst.add(v)

    # act + assert
    for v in values:
        assert bst.contains(v)


def test_bst_inOrder():
    # arrange
    bst = BST()
    values = ['c', 'b', 'd', 'a', 'e']
    expected_in_order_final = ['a', 'b', 'c', 'd', 'e']

    for v in values:
        bst.add(v)


    # act
    in_order_elts = bst.inOrder()

    # assert
    assert in_order_elts == expected_in_order_final



def test_bst_inOrder_2():
    # arrange
    bst = BST()
    values = [10, 5, 15, 3, 7, 12, 18]
    expected_in_order_final = [3, 5, 7, 10, 12, 15, 18]

    for v in values:
        bst.add(v)

    # act
    in_order_elts = bst.inOrder()

    # assert
    assert in_order_elts == expected_in_order_final


'''
              5
             / \
            3   7
           / \ / \
          2  4 6  8

            ->

              5
             / \
            7   3
           / \ / \
          8  6 4  2
'''
def test_bst_invert():
    # arrange
    bst = BST()
    values = [5, 3, 7, 2, 4, 6, 8]
    expected_in_order_original = [2, 3, 4, 5, 6, 7, 8]
    expected_in_order_final = [8, 7, 6, 5, 4, 3, 2]
    expected_level_order_final = [5, 7, 3, 8, 6, 4, 2]

    for v in values:
        bst.add(v)

    assert bst.inOrder() == expected_in_order_original
    assert bst.levelOrder() == values

    # act
    bst.invert()

    # assert
    assert bst.inOrder() == expected_in_order_final
    assert bst.levelOrder() == expected_level_order_final

