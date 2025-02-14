"""
Admin validation
"""

from functools import wraps

from telegram import Update
from telegram.ext import CallbackContext

from auth import authenticate_admin
from exceptions.exceptions import UnauthorizedAccessError


def admin_required(func):
    """
    Decorator to allow command execution only for admin users.

    Args:
        func (function): The original handler function.

    Returns:
        function: A decorated function that checks admin permissions before execution.
    """

    @wraps(func)
    def wrapper(update: Update, context: CallbackContext, *args, **kwargs):
        """
        Wrapper to validate admin user permissions.

        Args:
            update (Update): The incoming Telegram update.
            context (CallbackContext): The context of the current callback.
            *args: Additional positional arguments for the handler function.
            **kwargs: Additional keyword arguments for the handler function.

        Returns:
            Any: The result of the original handler function if the user is an admin.

        Raises:
            UnauthorizedAccessError: If the user is not an admin.
        """
        user_id = getattr(update.effective_user, "id", None)

        if user_id is not None and authenticate_admin(user_id):
            return func(update, context, *args, **kwargs)
        raise UnauthorizedAccessError(_("Access denied."))

    return wrapper
