from typing import List # python 3.8
from abc import ABC, abstractmethod
from src.models.sqlite.entities.pets import PetsTable

class PetsRepositoryInterface(ABC):

    @abstractmethod
    def list_pets(self) -> List[PetsTable]:
        pass

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass
