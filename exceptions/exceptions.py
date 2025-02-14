"""
Exceptions
"""


class UnauthorizedAccessError(Exception):
    """
    Custom exception for unauthorized access.

    Inherits from the base Exception class.
    """


class InvalidCommandError(Exception):
    """
    Custom exception for invalid commands.

    Inherits from the base Exception class.
    """


class InternalServerError(Exception):
    """
    Custom exception for internal server errors.

    Inherits from the base Exception class.
    """
