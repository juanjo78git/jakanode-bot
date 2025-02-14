"""
Donations actions
"""

from telegram import Update
from telegram.ext import ContextTypes

from services.donate_service import (
    get_ln_donation_address,
    get_ln_donation_page_url,
    get_ln_payment_link,
)


# pylint: disable=unused-argument
async def donate_lnurl(
    update: Update, context: ContextTypes.DEFAULT_TYPE, amount=None
) -> None:
    """
    Donation to a Lightning Address.

    Args:
        update (Update): The update object that contains the message and context.
        context (ContextTypes.DEFAULT_TYPE): The context for the command handler.
        amount (Optional[int]): The donation amount (if provided).

    Returns:
        None: Sends a formatted message with referral information.

    Raises:
        None: No exceptions are raised.
    """

    if amount is None:
        # If no amount is provided, thank the user and provide the Lightning Address
        response_text = _(
            "You can send donations to the following Lightning Address: [{address}]({link})"
        ).format(address=get_ln_donation_address(), link=get_ln_payment_link(None))
        response_text += "\n\n" + _(
            "Alternatively, you can donate through this web link: [{url_name}]({url})"
        ).format(url_name=get_ln_donation_page_url(), url=get_ln_donation_page_url())
        response_text += "\n\n" + _("Thank you for your donation!")
    else:
        # Generate the LNURL payment link with the specified amount
        response_text = _(
            "You can send your donation via this Lightning link: [{address}]({link})"
        ).format(address=get_ln_donation_address(), link=get_ln_payment_link(amount))
        response_text += "\n\n" + _(
            "Alternatively, you can donate through this web link: [{url_name}]({url})"
        ).format(url_name=get_ln_donation_page_url(), url=get_ln_donation_page_url())
        response_text += "\n\n" + _("Thank you for your donation of {amount}!").format(
            amount=amount
        )

    if update.message:
        await update.message.reply_text(
            response_text, parse_mode="Markdown", disable_web_page_preview=True
        )
