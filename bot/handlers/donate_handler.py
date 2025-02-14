"""
/donate command handler
"""

from telegram import Update
from telegram.ext import ContextTypes

from bot.actions.donations_actions import donate_lnurl
from config.logging import logger


# pylint: disable=unused-argument
async def donate_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /donate command.

    Args:
        update (Update): The incoming update from Telegram, containing the message and user
                         information.
        context (ContextTypes.DEFAULT_TYPE): The context associated with the update, containing
                                              useful information about the command.

    Returns:
        None

    Raises:
        None
    """
    try:
        donated_amount = int(context.args[0]) if context.args else None
    except (ValueError, IndexError):
        donated_amount = None

    await donate_lnurl(update=update, context=context, amount=donated_amount)

    logger.info(
        "Command /donate executed by %s (%s) with param: %s",
        getattr(update.effective_user, "username", None),
        getattr(update.effective_user, "id", None),
        donated_amount,
    )
