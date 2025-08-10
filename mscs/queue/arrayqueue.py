from typing import Generic
from mscs.common.typeparam import T

# TODO, pass capacity as a kwarg
INITIAL_CAPACITY = 9

class ArrayQueue(Generic[T]):
    def __init__(self) -> None:
        self.backingArray: list[T | None] = [None] * INITIAL_CAPACITY
        self.size = 0
        self.front = 0
    

    def enqueue(self, data: T) -> None:
        if data is None:
            raise Exception('cannot enqueue null data')
        
        if self.isFull():
            self.doubleCapacity()

        nextIndex = self.front + self.size
        wrappedNextIndex = nextIndex % len(self.backingArray)
        self.backingArray[wrappedNextIndex] = data

        # one liner
        # self.backingArray[(self.front + self.size) % len(self.backingArray)] = 
        
        self.size += 1


    def dequeue(self) -> T:
        if self.size == 0:
            raise Exception('cannot dequeue from empty queue')

        temp = self.backingArray[self.front]
        self.backingArray[self.front] = None

        self.front += 1
        self.size -= 1

        assert temp is not None
        return temp
    

    def peek(self) -> T:
        if self.size == 0:
            raise Exception('cannot peek into empty queue')
        
        temp = self.backingArray[self.front]

        assert temp is not None
        return temp


    def empty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == len(self.backingArray)


    def doubleCapacity(self) -> None:
        currentCapacity = len(self.backingArray)
        temp = self.backingArray

        self.backingArray = [None] * (2 * currentCapacity)

        # option 1
        for i in range(len(temp)):
            wrappedIndex = (self.front + i) % len(temp)
            self.backingArray[i] = temp[wrappedIndex]

            # one liner
            # self.backingArray[i] = temp[(self.front + i) % len(temp)]

        # option 2
        # for idx, elt in enumerate(temp):
        #     self.backingArray[idx] = temp[idx]
        #     self.backingArray[idx] = elt

        self.front = 0


    ### TEST HELPERS

    def getBackingArray(self) -> list[T | None]:
        return self.backingArray
    

    def getFront(self) -> int:
        return self.front


    def getSize(self) -> int:
        return self.size