"""
i18n (Internationalization)
"""

import gettext
import os

from config.logging import logger
from config.settings import DEFAULT_LANGUAGE


def set_language(language_code):
    """
    Sets the user's language.

    Args:
        language_code (str): The language code (e.g., 'en', 'es', etc.).

    Returns:
        None
    """
    logger.debug("Setting up i18n...")
    localedir = os.path.join(os.path.dirname(__file__), "locales")

    try:
        lang = gettext.translation(
            "messages", localedir=localedir, languages=[language_code], fallback=True
        )
        lang.install()
        logger.debug("User language set to: %s", language_code)
    except FileNotFoundError:
        lang = gettext.translation(
            "messages", localedir=localedir, languages=[DEFAULT_LANGUAGE], fallback=True
        )
        lang.install()
        logger.debug("Default language set")


# pylint: disable=unused-argument
async def apply_language_middleware_bot(update, context):
    """
    Global middleware that automatically sets the bot's user language.

    Args:
        update (Update): The Telegram update object.
        context (CallbackContext): The context of the current callback.

    Returns:
        None
    """
    logger.debug("Retrieving user language")
    user_language = update.effective_user.language_code or DEFAULT_LANGUAGE
    set_language(user_language)
    logger.debug("Language set to %s", user_language)


# Set the language to the default if no language is provided
set_language(DEFAULT_LANGUAGE)

# Force PyCharm to recognize the usage of _
_ = gettext.gettext

logger.debug("i18n configured.")

# Usage:
# _ = set_language('es')  # Change language to Spanish
# print(_("welcome"))  # Translates "welcome"
