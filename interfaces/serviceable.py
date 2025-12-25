from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def provide_service(self) -> str:
        pass
