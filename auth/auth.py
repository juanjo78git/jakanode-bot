"""
Authentication logic and user validation
"""

from config.settings import ADMIN_USER_ID
from database.db_user_operations import is_admin_user, is_registered


def authenticate_user(user_id):
    """
    Checks if the user is registered.

    Args:
        user_id (int): The ID of the user to check.

    Returns:
        bool: True if the user is registered, False otherwise.
    """
    return user_id == ADMIN_USER_ID or is_registered(user_id)


def authenticate_admin(user_id):
    """
    Checks if the user is an admin.

    Args:
        user_id (int): The ID of the user to check.

    Returns:
        bool: True if the user is an admin, False otherwise.
    """
    return user_id == ADMIN_USER_ID or is_admin_user(user_id)
