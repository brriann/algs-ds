from typing import Generic
from mscs.typeparam import T


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