"""
/help command handler
"""

from telegram import Update
from telegram.ext import ContextTypes

from config.logging import logger


# pylint: disable=unused-argument
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /help command.

    Args:
        update (Update): The update object containing data and methods about the incoming message.
        context (ContextTypes.DEFAULT_TYPE): The context object that provides data for the
                                             command execution.

    Returns:
        None

    Raises:
        None

    Sends a help message to the user and logs the command execution.
    """
    if update.message:
        await update.message.reply_text(
            _("This is the help text. Use /start to begin.")
        )
    logger.info(
        "Command /help executed by %s (%s)",
        getattr(update.effective_user, "username", None),
        getattr(update.effective_user, "id", None),
    )
