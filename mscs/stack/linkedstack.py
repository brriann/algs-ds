from typing import Generic
from mscs.common.typeparam import T
from mscs.common.linkednode import LinkedNode

class LinkedStack(Generic[T]):
    def __init__(self) -> None:
        self.head : LinkedNode[T] | None = None
        self.size = 0


    def push(self, data: T) -> None:
        if data is None:
            raise Exception('cannot push null data')
        
        newNode = LinkedNode[T](data)

        if self.head is not None:
            newNode.setNext(self.head)

        self.head = newNode
        self.size += 1


    def pop(self) -> T:
        if self.size == 0 or self.head is None:
            raise Exception('cannot pop from empty stack')
        
        temp = self.head

        self.head = self.head.getNext()
        self.size -= 1

        return temp.getData()
    

    def peek(self) -> T:
        if self.size == 0 or self.head is None:
            raise Exception('cannot peek into empty stack')
        
        return self.head.getData()


    ### TEST HELPERS

    def getHead(self) -> LinkedNode[T] | None:
        return self.head


    def getSize(self) -> int:
        return self.size
