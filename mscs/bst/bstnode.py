from typing import Generic
from mscs.common.typeparam import T, Comparable


class BSTNode(Generic[T]):
    def __init__(
            self, 
            data: T | None = None, 
            left: "BSTNode[T] | None" = None, 
            right: "BSTNode[T] | None" = None) -> None:
        self.data = data
        self.left = left
        self.right = right
    
    def getData(self)-> T:
        # allow "dummy" BSTNodes to initialize with a None data
        # ... for data transfer through recursive function calls
        assert self.data is not None, "Data must not be None"
        return self.data
    
    def setData(self, data: T) -> None:
        self.data = data
    
    def getLeft(self) -> "BSTNode[T] | None":
        return self.left
    
    def setLeft(self, left: "BSTNode[T] | None") -> None:
        self.left = left
    
    def getRight(self)-> "BSTNode[T] | None":
        return self.right
    
    def setRight(self, right: "BSTNode[T] | None") -> None:
        self.right = right

    # invalid/unused, but allows LinkedQueue[BSTNode[T]]
    def __lt__(self, other: "Comparable") -> bool:
        return self < other
    
    # invalid/unused, but allows LinkedQueue[BSTNode[T]]
    def __gt__(self, other: "Comparable") -> bool:
        return self > other


# # container for data transfer through recursive function returns
# class BSTNodeDummy(Generic[T]):
#     def __init__(
#             self,
#             data: T | None = None
#     ) -> None:
#         self.data = data

#     def getData(self)-> T | None:
#         return self.data
    
#     def setData(self, data: T) -> None:
#         self.data = data