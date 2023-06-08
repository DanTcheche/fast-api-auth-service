from abc import ABC, abstractmethod
from typing import List, Optional


class BaseRepository(ABC):
    """An interface for a basic repository that provides CRUD (Create, Read, Update, Delete) operations."""

    @abstractmethod
    def create(self, obj) -> object:
        pass

    @abstractmethod
    def read(self, _id) -> Optional[object]:
        pass

    @abstractmethod
    def update(self, obj, _id) -> object:
        pass

    @abstractmethod
    def delete(self, _id) -> object:
        pass

    @abstractmethod
    def read_all(self, params) -> List[object]:
        pass
