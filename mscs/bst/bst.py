from typing import Generic
# TODO, replace with my own queue implementation
from queue import Queue
from mscs.typeparam import T
from .bstnode import BSTNode

class BST(Generic[T]):
    def __init__(
            self,
            list: list[T] | None = None):
        self.root = None
        self.size = 0

        if list is not None:
            for i in range(len(list)):
                self.add(list[i])
    
    
    ### ADD

    def add(self, data: T):
        if data is not None:
            self.root = self._add(self.root, data)


    def _add(self, node: BSTNode[T] | None, data: T) -> BSTNode[T]:
        if node is None:
            self.size += 1
            return BSTNode(data)
        elif data < node.getData():
            node.setLeft(self._add(node.getLeft(), data))
        elif data > node.getData():
            node.setRight(self._add(node.getRight(), data))
        
        return node
    

    ### REMOVE

    def remove(self, data: T) -> T | None:
        dummy = BSTNode[T]()
        self.root = self._remove(self.root, data, dummy)

        # if dummy.getData() is None:
        #     raise Exception('Data to be remoed was not present in the BST')
        
        return dummy.getData()

    def _remove(
            self, 
            node: BSTNode[T] | None, 
            data: T, 
            dummy: BSTNode[T]) -> BSTNode[T] | None:
        if node is None:
            return None
        elif data < node.getData():
            node.setLeft(self._remove(node.getLeft(), data, dummy))
        elif data > node.getData():
            node.setRight(self._remove(node.getRight(), data, dummy))
        else:
            # store data in dummy for return and remove node
            dummy.setData(node.getData())
            self.size -= 1

            if node.getLeft() is None and node.getRight() is None:
                return None
            elif node.getLeft() is None:
                return node.getRight()
            elif node.getRight() is None:
                return node.getLeft()
            else:
                # node has 2 children - replace with successor (next largest)
                dummy2 = BSTNode[T]()
                node.setRight(self._removeSuccessor(node.getRight(), dummy2))
                node.setData(dummy2.getData())

        return node


    def _removeSuccessor(self, node: BSTNode[T] | None, dummy: BSTNode[T]):
        # upstream, node has been verified to be not None
        assert node is not None

        if node.getLeft() is None:
            dummy.setData(node.getData())
            return node.getRight()
        else:
            node.setLeft(self._removeSuccessor(node.getLeft(), dummy))
            return node


    ### CONTAINS

    def contains(self, data: T):
        return self._contains(self.root, data)
    

    def _contains(self, node: BSTNode[T] | None, data: T) -> bool:
        if node is None:
            return False
        elif data < node.getData():
            return self._contains(node.getLeft(), data)
        elif data > node.getData():
            return self._contains(node.getRight(), data)
        else:
            return True
        

    ### TRAVERSALS

    def preOrder(self) -> list[T]:
        elts: list[T] = []
        self._preOrder(self.root, elts)

        return elts

    
    def _preOrder(self, node: BSTNode[T] | None, elts: list[T]):
        if node is not None:
            elts.append(node.getData())
            self._preOrder(node.getLeft(), elts)
            self._preOrder(node.getRight(), elts)


    def inOrder(self) -> list[T]:
        elts: list[T] = []
        self._inOrder(self.root, elts)

        return elts
    

    def _inOrder(self, node: BSTNode[T] | None, elts: list[T]) -> None:
        if node is not None:
            self._inOrder(node.getLeft(), elts)
            elts.append(node.getData())        
            self._inOrder(node.getRight(), elts)


    def postOrder(self) -> list[T]:
        elts: list[T] = []
        self._postOrder(self.root, elts)

        return elts

    
    def _postOrder(self, node: BSTNode[T] | None, elts: list[T]):
        if node is not None:
            self._postOrder(node.getLeft(), elts)
            self._postOrder(node.getRight(), elts)    
            elts.append(node.getData())


    def levelOrder(self) -> list[T]:
        elts: list[T] = []

        queue = Queue[BSTNode[T]](maxsize = self.size)

        if self.root is not None:
            queue.put(self.root)

        while not queue.empty():
            curr = queue.get()

            elts.append(curr.getData())

            leftChild = curr.getLeft()
            if leftChild is not None:
                queue.put(leftChild)

            rightChild = curr.getRight()
            if rightChild is not None:
                queue.put(rightChild)

        return elts


    ### INVERT

    def invert(self) -> None:
        self._invert(self.root)


    def _invert(self, node: BSTNode[T] | None) -> None:
        if node is None:
            return
        
        if node.getLeft() is None and node.getRight() is None:
            # leaf node
            return
        
        self._invert(node.getLeft())
        self._invert(node.getRight())

        self._swapChildren(node)


    def _swapChildren(self, node: BSTNode[T]):
        temp = node.getLeft()
        node.setLeft(node.getRight())
        node.setRight(temp)

    
    ### TEST HELPERS

    def getRoot(self) -> BSTNode[T] | None:
        return self.root
        
    def getSize(self) -> int:
        return self.size

            