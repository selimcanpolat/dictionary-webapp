from abc import ABC, abstractmethod

class Page(ABC):
    """This is an abstract class inheriting from ABC"""
    @abstractmethod
    def serve(self):  # Abstract method decorated with @abstractmethod
        pass