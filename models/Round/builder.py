from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def get_items():
        raise NotImplementedError

    @abstractmethod
    def get_enemies():
        raise NotImplementedError
    
    @abstractmethod
    def get_bosses():
        raise NotImplementedError