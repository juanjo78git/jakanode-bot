"""
Database utilities
"""


def validate_telegram_id(telegram_id):
    """
    Validates the Telegram ID. You can add more complex logic here if needed.

    Args:
        telegram_id (int): The Telegram user ID to validate.

    Returns:
        bool: True if the Telegram ID is a positive integer, otherwise False.
    """
    return isinstance(telegram_id, int) and telegram_id > 0
