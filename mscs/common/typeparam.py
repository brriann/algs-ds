from typing import TypeVar, Protocol

class Comparable(Protocol):
    def __lt__(self, other: "Comparable") -> bool:
        return self < other
    
    def __gt__(self, other: "Comparable") -> bool:
        return self > other
    

T = TypeVar('T', bound=Comparable)
