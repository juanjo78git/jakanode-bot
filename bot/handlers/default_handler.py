"""
/default command handler
"""

from telegram import Update
from telegram.ext import ContextTypes


# pylint: disable=unused-argument
async def default(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    This is the handler that will be called when the command is not registered

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
    if update.message:
        await update.message.reply_text(_("Access denied."))
