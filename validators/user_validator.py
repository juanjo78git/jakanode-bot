"""
User validation
"""

from functools import wraps

from telegram import Update
from telegram.ext import CallbackContext

from auth import authenticate_user
from exceptions.exceptions import UnauthorizedAccessError


def user_required(func):
    """
    Decorator to allow command execution only for registered users.

    Args:
        func (function): The original handler function.

    Returns:
        function: A decorated function that checks user registration before execution.
    """

    @wraps(func)
    def wrapper(update: Update, context: CallbackContext, *args, **kwargs):
        """
        Wrapper to validate registered user permissions.

        Args:
            update (Update): The incoming Telegram update.
            context (CallbackContext): The context of the current callback.
            *args: Additional positional arguments for the handler function.
            **kwargs: Additional keyword arguments for the handler function.

        Returns:
            Any: The result of the original handler function if the user is registered.

        Raises:
            UnauthorizedAccessError: If the user is not registered.
        """
        user_id = getattr(update.effective_user, "id", None)

        if user_id is not None and authenticate_user(user_id):
            return func(update, context, *args, **kwargs)
        raise UnauthorizedAccessError(_("Access denied."))

    return wrapper
