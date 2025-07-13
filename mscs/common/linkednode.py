from typing import Generic
from .typeparam import T

class LinkedNode(Generic[T]):
    def __init__(
            self,
            data: T,
            next: "LinkedNode[T] | None" = None) -> None:
        self.data = data
        self.next = next

    def getData(self) -> T:
        return self.data
    
    def getNext(self) -> "LinkedNode[T] | None":
        return self.next
    
    def setNext(self, next: "LinkedNode[T] | None") -> None:
        self.next = next
