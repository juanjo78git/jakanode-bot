"""
/start command handler
"""

from telegram import Update
from telegram.ext import ContextTypes

from config.logging import logger
from services.user_service import register_user


# pylint: disable=unused-argument
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /start command that is triggered when a user starts a conversation with the bot.

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
        await update.message.reply_text(_("Hello! I am the jakanode bot."))
    logger.info(
        "Command /start executed by %s (%s)",
        getattr(update.effective_user, "username", None),
        getattr(update.effective_user, "id", None),
    )
    register_user(
        telegram_id=getattr(update.effective_user, "id", None),
        username=getattr(update.effective_user, "username", None),
        is_admin=0,
        status="active",
        language=getattr(update.effective_user, "language_code", None),
    )
