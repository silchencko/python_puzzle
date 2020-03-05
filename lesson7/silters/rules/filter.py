from abc import ABC, abstractmethod


class Filter(ABC):
    @abstractmethod
    def name(self) -> str:
        """Provides a name of the rule (like FP005)."""
        pass

    @abstractmethod
    def matches(self, line: str) -> bool:
        """
        Returns True if a given line matches the filter,
        otherwise, returns False.
        """
        pass
