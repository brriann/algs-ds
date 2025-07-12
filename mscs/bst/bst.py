from typing import Generic
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
    
    def contains(self, data: T):
        return self._contains(self. root, data)
    
    def _contains(self, node: BSTNode[T] | None, data: T) -> bool:
        if node is None:
            return False
        elif data < node.getData():
            return self._contains(node.getLeft(), data)
        elif data > node.getData():
            return self._contains(node.getRight(), data)
        else:
            return True
        
    def getRoot(self) -> BSTNode[T] | None:
        return self.root
        

            