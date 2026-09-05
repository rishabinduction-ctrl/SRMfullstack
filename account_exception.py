"""Root domain exception class for the Global Digital Bank (GDB) application core."""

class AccountException(Exception):
    """Root base checked exception for all GDB domain failures.
    
    Inheriting from Python's standard Exception class forces caller code to handle
    or declare banking operations errors explicitly.
    """
    def __init__(self, message: str) -> None:
        """Initialize AccountException with a diagnostic message string."""
        super().__init__(message)
        self.message = message
