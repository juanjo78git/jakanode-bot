"""
Database operations for users
"""

from database.db_config import (
    close_db_connection,
    commit_db_connection,
    get_db_connection,
)
from database.models.user import format_user_data
from database.utils import validate_telegram_id


def is_registered(user_id):
    """
    Checks if a user is registered in the database.

    Args:
        user_id (int): The Telegram user ID to check.

    Returns:
        bool: True if the user is registered, otherwise False.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE telegram_id=?)", (user_id,))
    result = cursor.fetchone()[0]
    close_db_connection(conn)
    return bool(result)


def is_admin_user(user_id):
    """
    Checks if a user is an admin.

    Args:
        user_id (int): The Telegram user ID to check.

    Returns:
        bool: True if the user is an admin, otherwise False.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT is_admin FROM users WHERE telegram_id=?", (user_id,))
    result = cursor.fetchone()
    close_db_connection(conn)
    return result[0] == 1 if result else False


def create_user_db(telegram_id, username, is_admin=0, status="active", language="en"):
    """
    Creates a new user in the database.

    Args:
        telegram_id (int): The user's Telegram ID.
        username (str): The user's username.
        is_admin (int, optional): Indicates whether the user is an admin (default is 0).
        status (str, optional): The user's status (default is "active").
        language (str, optional): The user's language (default is "en").

    Raises:
        ValueError: If the Telegram ID is invalid.
    """
    if not validate_telegram_id(telegram_id):
        raise ValueError("Invalid Telegram ID")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
    INSERT INTO users (telegram_id, username, is_admin, status, language)
    VALUES (?, ?, ?, ?, ?)
    """,
        (telegram_id, username, is_admin, status, language),
    )
    commit_db_connection(conn)
    close_db_connection(conn)


def get_user_by_telegram_id_db(telegram_id):
    """
    Retrieves a user's information from the database by their Telegram ID.

    Args:
        telegram_id (int): The Telegram user ID to fetch.

    Returns:
        dict or None: A dictionary containing the user's data, or None if the user doesn't exist.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM users WHERE telegram_id = ?
        """,
        (telegram_id,),
    )
    user = cursor.fetchone()
    close_db_connection(conn)
    # Format the data before returning it
    if user:
        return format_user_data(user)
    return None


def update_user_status_db(telegram_id, status="inactive"):
    """
    Updates the status of a user in the database.

    Args:
        telegram_id (int): The Telegram user ID whose status is to be updated.
        status (str, optional): The new status (default is "inactive").

    Returns:
        None
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE users SET status = ?, updated_at = CURRENT_TIMESTAMP 
        WHERE telegram_id = ?
        """,
        (status, telegram_id),
    )
    commit_db_connection(conn)
    close_db_connection(conn)


def delete_user_db(telegram_id):
    """
    Deletes a user from the database.

    Args:
        telegram_id (int): The Telegram user ID to delete.

    Returns:
        None
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM users WHERE telegram_id = ?
        """,
        (telegram_id,),
    )
    commit_db_connection(conn)
    close_db_connection(conn)


def fetch_users_db():
    """
    Fetches all users from the database with their telegram_id, username, status, and admin status.

    Returns:
        list: A list of dictionaries containing user data, or an empty list if no users are found.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM users
        """
    )
    users = cursor.fetchall()
    close_db_connection(conn)

    # Format the data before returning it
    if users:
        formatted_users = []
        for user in users:
            formatted_users.append(format_user_data(user))
        return formatted_users
    return []
