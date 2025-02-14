"""
Telegram bot
"""

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot.handlers import (
    admin_command,
    default,
    donate_command,
    help_command,
    referrals_command,
    start,
)
from config.logging import logger
from config.settings import (
    TOKEN,
    USE_WEBHOOK_BOT,
    WEBHOOK_BOT_CERT,
    WEBHOOK_BOT_KEY,
    WEBHOOK_BOT_PATH,
    WEBHOOK_BOT_PORT,
    WEBHOOK_BOT_URL,
)
from exceptions.error_handler import handle_global_error
from i18n.i18n import apply_language_middleware_bot


def main():
    """
    Initializes the Telegram bot and registers event handlers.

    Raises:
        Exception: If there is an error during bot initialization or webhook setup.
    """
    # Create the application instance
    application = Application.builder().token(TOKEN).build()

    # Apply global middleware to all messages
    application.add_handler(
        MessageHandler(filters.ALL, apply_language_middleware_bot), group=-1
    )

    # Register commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("admin", admin_command))
    application.add_handler(CommandHandler("donate", donate_command))
    application.add_handler(CommandHandler("referrals", referrals_command))

    # Register the default handler for all unregistered commands
    application.add_handler(MessageHandler(filters.COMMAND, default))

    # Register global error handler
    application.add_error_handler(handle_global_error)

    logger.info("Bot started. Connecting to the server...")

    logger.info("Using webhook: %s", USE_WEBHOOK_BOT)
    if USE_WEBHOOK_BOT:
        logger.info(WEBHOOK_BOT_CERT)
        logger.info(WEBHOOK_BOT_KEY)
        logger.info(WEBHOOK_BOT_URL)
        logger.info(WEBHOOK_BOT_PATH)
        logger.info(WEBHOOK_BOT_PORT)
        # Begin receiving updates via webhook
        application.run_webhook(
            listen="0.0.0.0",
            port=WEBHOOK_BOT_PORT,  # Secure port for HTTPS
            url_path=WEBHOOK_BOT_PATH,  # Path associated with webhook
            webhook_url=WEBHOOK_BOT_URL + "/" + WEBHOOK_BOT_PATH,
            cert=WEBHOOK_BOT_CERT,
            key=WEBHOOK_BOT_KEY,
        )
    else:
        # Start receiving updates via polling
        application.run_polling()


if __name__ == "__main__":
    main()
