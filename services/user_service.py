"""
User service
"""

from database.db_user_operations import (
    create_user_db,
    fetch_users_db,
    get_user_by_telegram_id_db,
)


def get_user_list():
    """
    Retrieves all registered users.

    Returns:
        list: A list of user records from the database.
    """
    return fetch_users_db()


def register_user(telegram_id, username, is_admin=0, status="active", language="en"):
    """
    Registers a new user if they do not already exist.

    Args:
        telegram_id (int): The Telegram ID of the user.
        username (str): The username of the user.
        is_admin (int, optional): Whether the user is an admin (1) or not (0). Defaults to 0.
        status (str, optional): The user's account status (e.g., "active", "inactive").
                                 Defaults to "active".
        language (str, optional): The preferred language of the user. Defaults to "es" (Spanish).

    Returns:
        None
    """
    if get_user_by_telegram_id_db(telegram_id) is None:
        create_user_db(
            telegram_id=telegram_id,
            username=username,
            is_admin=is_admin,
            status=status,
            language=language,
        )


def get_user_by_telegram_id(telegram_id):
    """
    Retrieves detailed information of a registered Telegram user.

    Args:
        telegram_id (int): The Telegram ID of the user.

    Returns:
        dict or None: The user record if found, otherwise None.
    """
    return get_user_by_telegram_id_db(telegram_id)
