from abc import ABC, abstractmethod

class BaseProduct(ABC):

    @abstractmethod
    def __str__(self) -> str:
        ...

    @abstractmethod
    def __add__(self, other):
        ...
