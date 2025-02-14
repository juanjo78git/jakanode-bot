"""
Referral service
"""

from database.db_referral_operations import (
    create_referral_db,
    fetch_referrals_db,
    get_referral_by_id_db,
)


def get_referral_list():
    """
    Retrieves all referrals.

    Returns:
        list: A list of referral records from the database.
    """
    return fetch_referrals_db()


def get_referral_by_id(referral_id):
    """
    Retrieves detailed information of a Referral.

    Args:
        referral_id (int): The  ID of the referral.

    Returns:
        dict or None: The referral record if found, otherwise None.
    """
    return get_referral_by_id_db(referral_id)


def register_referral(name, url, status="active"):
    """
    Registers a new referral.

    Args:
        name (str): The name of the referral.
        url (str): URL.
        status (str, optional): The user's account status (e.g., "active", "inactive").
                                 Defaults to "active".

    Returns:
        None
    """

    create_referral_db(
        name=name,
        url=url,
        status=status,
    )
