from typing import Generic
from mscs.common.typeparam import T
from mscs.common.linkednode import LinkedNode

class LinkedQueue(Generic[T]):
    def __init__(self) -> None:
        self.head: LinkedNode[T] | None = None
        self.tail: LinkedNode[T] | None = None
        self.size = 0

    
    def enqueue(self, data: T) -> None:
        if data is None:
            raise Exception('cannot enqueue null data')
        
        newNode = LinkedNode[T](data)

        if self.size == 0:
            self.head = newNode
        else:
            assert self.tail is not None
            self.tail.setNext(newNode)

        self.tail = newNode
        self.size += 1



    def dequeue(self) -> T:
        if self.size == 0 or self.head is None:
            raise Exception('cannot dequeue from empty queue')
        
        temp = self.head.getData()

        self.head = self.head.getNext()

        if self.size == 1:
            self.tail = None
        
        self.size -= 1

        return temp


    def peek(self) -> T:
        if self.size == 0 or self.head is None:
            raise Exception('cannot peek into empty queue')
        
        return self.head.getData()


    def empty(self) -> bool:
        return self.size == 0

    ### TEST HELPERS

    def getHead(self) -> LinkedNode[T] | None:
        return self.head
    
    def getTail(self) -> LinkedNode[T] | None:
        return self.tail

    def getSize(self) -> int:
        return self.size
