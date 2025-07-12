from typing import Generic
from mscs.typeparam import T

class BSTNode(Generic[T]):
    def __init__(
            self, 
            data: T, 
            left: "BSTNode[T] | None" = None, 
            right: "BSTNode[T] | None" = None) -> None:
        self.data = data
        self.left = left
        self.right = right
    
    def getData(self)-> T:
        return self.data
    
    def setData(self, data: T) -> None:
        self.data = data
    
    def getLeft(self) -> "BSTNode[T] | None":
        return self.left
    
    def setLeft(self, left: "BSTNode") -> None:
        self.left = left
    
    def getRight(self)-> "BSTNode[T] | None":
        return self.right
    
    def setRight(self, right: "BSTNode") -> None:
        self.right = right
    
