"""
Referral Model
"""


def format_referral_data(referral_data):
    """
    Formats the referral data to be presented or used in other parts of the application.

    Args:
        referral_data (tuple): A tuple containing the referral's data from the database.

    Returns:
        dict: A dictionary with the formatted referral data or None if no data is provided.
    """
    if referral_data:
        return {
            "id": referral_data[0],
            "name": referral_data[1],
            "url": referral_data[2],
            "description": referral_data[3],
            "created_at": referral_data[4],
            "updated_at": referral_data[5],
            "status": referral_data[6],
        }
    return None
