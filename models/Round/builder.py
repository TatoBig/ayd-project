from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def set_items() -> None:
        raise NotImplementedError

    @abstractmethod
    def set_enemies() -> None:
        raise NotImplementedError
    
    @abstractmethod
    def set_time() -> None:
        raise NotImplementedError

    @abstractmethod
    def reset() -> None:
        raise NotImplementedError
    
