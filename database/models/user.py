"""
User Model
"""


def format_user_data(user_data):
    """
    Formats the user data to be presented or used in other parts of the application.

    Args:
        user_data (tuple): A tuple containing the user's data from the database.

    Returns:
        dict: A dictionary with the formatted user data or None if no data is provided.
    """
    if user_data:
        return {
            "id": user_data[0],
            "telegram_id": user_data[1],
            "is_admin": user_data[2],
            "username": user_data[3],
            "created_at": user_data[4],
            "updated_at": user_data[5],
            "status": user_data[6],
            "language": user_data[7],
            "cert": user_data[8],
        }
    return None
