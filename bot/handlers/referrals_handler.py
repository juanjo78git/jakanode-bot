"""
/referrals command handler
"""

from telegram import Update
from telegram.ext import ContextTypes

from bot.actions import referrals_actions
from config.logging import logger


# pylint: disable=unused-argument
async def referrals_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /referrals command.

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

    await referrals_actions.referrals_list(update, context)

    logger.info(
        "Command /referrals executed by %s (%s)",
        getattr(update.effective_user, "username", None),
        getattr(update.effective_user, "id", None),
    )
