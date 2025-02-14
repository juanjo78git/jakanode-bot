"""
Database operations for referrals
"""

from database.db_config import (
    close_db_connection,
    commit_db_connection,
    get_db_connection,
)
from database.models.referral import format_referral_data


def get_referral_by_id_db(referral_id):
    """
    Retrieves a referral's information from the database by their ID.

    Args:
        id (int): The referral ID to fetch.

    Returns:
        dict or None: A dictionary containing the referral's data,
                      or None if the referral doesn't exist.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM referrals WHERE id = ?
        """,
        (referral_id,),
    )
    referral = cursor.fetchone()
    close_db_connection(conn)
    # Format the data before returning it
    if referral:
        return format_referral_data(referral)
    return None


def fetch_referrals_db():
    """
    Fetches all referrals from the database with their id, name, url, and description.

    Returns:
        list: A list of dictionaries containing referrals data,
              or an empty list if no referrals are found.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM referrals
        where status = 'active'
        """
    )
    referrals = cursor.fetchall()
    close_db_connection(conn)

    # Format the data before returning it
    if referrals:
        formatted_referrals = []
        for referral in referrals:
            formatted_referrals.append(format_referral_data(referral))
        return formatted_referrals
    return []


def create_referral_db(name, url, status="active"):
    """
    Creates a new referral in the database.

    Args:
        name (str): The referral's name.
        url (str): URL.
        status (str, optional): The user's status (default is "active").

    Returns:
        None
    """

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO referrals (name, url, status)
        VALUES (?, ?, ?)
        """,
        (name, url, status),
    )
    commit_db_connection(conn)
    close_db_connection(conn)
