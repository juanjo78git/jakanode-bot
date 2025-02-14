"""
Referrals actions
"""

from telegram import Update
from telegram.ext import ContextTypes

from services.referral_service import get_referral_list, register_referral


# pylint: disable=unused-argument
async def referrals_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Retrieves and formats the list of all referrals.

    Args:
        update (Update): The update object that contains the message and context.
        context (ContextTypes.DEFAULT_TYPE): The context for the command handler.

    Returns:
        None: Sends a formatted message with referral information.

    Raises:
        None: No exceptions are raised.
    """
    referrals = get_referral_list()

    response_text = _("Here are your referral links:\n\n")
    for referral in referrals:
        response_text += f"*{referral['name']}*\n"
        response_text += f"[{referral['url']}]({referral['url']})\n"
        # response_text += f"{referral['description']}\n\n"

    if update.message:
        await update.message.reply_text(
            response_text, parse_mode="Markdown", disable_web_page_preview=True
        )


# pylint: disable=unused-argument
async def add_referral(
    update: Update, context: ContextTypes.DEFAULT_TYPE, name, url
) -> None:
    """
    Add a new referral

    Args:
        update (Update): The update object that contains the message and context.
        context (ContextTypes.DEFAULT_TYPE): The context for the command handler.
        name (str): The name of the referral.
        url (str): URL.

    Returns:
        None

    Raises:
        None: No exceptions are raised.
    """
    register_referral(name, url)

    if update.message:
        await update.message.reply_text(_("Request registered"))
