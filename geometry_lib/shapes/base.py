from typing import Protocol, runtime_checkable


@runtime_checkable
class Shape(Protocol):
    """Interface for geometric shapes."""

    @property
    def area(self) -> float:
        """Calculate shape's area."""
        ...

    def is_right_angled(self) -> bool:
        """Check if shape is right-angled."""
        ...