#In this mission you should check if all elements in the given sequence are equal.
from typing import List, Any
def all_the_same(elements: List[Any]) -> bool:
    if not elements:
        return True
    return len(set(elements)) == 1