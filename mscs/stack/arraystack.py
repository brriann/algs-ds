from typing import Generic
from mscs.common.typeparam import T

# TODO, pass capacity as a kwarg
INITIAL_CAPACITY = 9

class ArrayStack(Generic[T]):
    def __init__(self) -> None:
        self.backingArray: list[T | None] = [None] * INITIAL_CAPACITY
        self.size = 0

    def push(self, data: T) -> None:
        if data is None:
            raise Exception('cannot push null data')
        
        if self.isFull():
            self.doubleCapacity()

        self.backingArray[self.size] = data

        self.size += 1


    def pop(self) -> T:
        if self.size == 0:
            raise Exception('cannot pop from empty stack')

        popped = self.backingArray[self.size - 1]
        assert popped is not None

        self.backingArray[self.size - 1] = None

        self.size -= 1
        return popped


    def peek(self) -> T:
        if self.size == 0:
            raise Exception('cannot peek into empty stack')
        
        peeked = self.backingArray[self.size - 1]
        assert peeked is not None

        return peeked
    

    def isFull(self) -> bool:
        lastIndex = len(self.backingArray) - 1
        lastElt = self.backingArray[lastIndex]
        return lastElt is not None
    
        # one liner
        # return self.backingArray[len(self.backingArray) - 1] is not None


    def doubleCapacity(self) -> None:
        currentCapacity = len(self.backingArray)
        temp = self.backingArray

        self.backingArray = [None] * (2 * currentCapacity)

        # option 1
        # for idx, elt in enumerate(temp):
        #     self.backingArray[idx] = temp[idx]
        #     self.backingArray[idx] = elt

        # option 2
        for i in range(len(temp)):
            self.backingArray[i] = temp[i]


    ### TEST HELPERS

    def getBackingArray(self) -> list[T | None]:
        return self.backingArray


    def getSize(self) -> int:
        return self.size