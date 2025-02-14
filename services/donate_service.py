"""
Donate service
"""

from config.settings import DONATION_LN_ADDRESS, DONATION_LN_URL


def get_ln_donation_address():
    """
    Retrieves the Lightning Network donation address.

    Returns:
        str: The Lightning Network donation address.
    """
    return DONATION_LN_ADDRESS


def get_ln_payment_link(amount):
    """
    Generates a Lightning Network payment URL with an optional amount.

    Args:
        amount (int or None): The amount to be included in the payment request.
                              If None, no amount is specified.

    Returns:
        str: A Lightning Network payment URL.
    """
    ln_address = get_ln_donation_address()
    if amount is None:
        address_link = f"lightning:{ln_address}"
    else:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number")
        address_link = f"lightning:{ln_address}?amount={amount}"
    return address_link


def get_ln_donation_page_url():
    """
    Retrieves the Lightning Network donation page URL.

    Returns:
        str: The URL for the donation page.
    """
    return DONATION_LN_URL
