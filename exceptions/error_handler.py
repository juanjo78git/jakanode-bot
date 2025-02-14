"""
Error handler
"""

from telegram import Update
from telegram.ext import ContextTypes

from config.logging import logger
from exceptions.exceptions import UnauthorizedAccessError


async def handle_global_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Global error handling.

    Args:
        update (Update): The Telegram update object.
        context (ContextTypes.DEFAULT_TYPE): The context of the current callback.

    Returns:
        None
    """
    # Captura el tipo de error
    error = context.error

    # If the error is UnauthorizedAccessError, redirect to the authorization handler
    if isinstance(error, UnauthorizedAccessError):
        await handle_unauthorized_access(update, context)
    else:
        # Handle other errors as generic errors
        logger.error("Unexpected error: %s", error)

        # Check if `update` and `update.message` exist before attempting to access `update.message`
        if update and update.message:
            await update.message.reply_text(
                _("An unexpected error occurred. Please try again later.")
            )
        else:
            logger.error(
                "Error not related to a user message. Unable to send error message."
            )


# pylint: disable=unused-argument
async def handle_unauthorized_access(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """
    Handles unauthorized access errors.

    Args:
        update (Update): The Telegram update object.
        context (ContextTypes.DEFAULT_TYPE): The context of the current callback.

    Returns:
        None
    """
    if update and update.message:
        logger.warning(
            "Access denied for %s (%s)",
            getattr(update.effective_user, "username", None),
            getattr(update.effective_user, "id", None),
        )
        await update.message.reply_text(_("Access denied."))
    else:
        logger.warning("Access denied, but no user message is available.")
