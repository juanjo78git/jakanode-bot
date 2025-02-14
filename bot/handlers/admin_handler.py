"""
/admin command handler
"""

from telegram import Update
from telegram.ext import ContextTypes

from bot.actions import admin_actions
from bot.config.load_config import load_command_params
from config.logging import logger
from validators import admin_required


# pylint: disable=unused-argument
@admin_required
async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /admin command.

    Args:
        update (Update): The update object containing data and methods about the incoming message.
        context (ContextTypes.DEFAULT_TYPE): The context object that provides data for the
                                              command execution.

    Returns:
        None

    Raises:
        None

    The function processes the /admin command by checking for subcommands and their associated
    parameters. It also validates user permissions and executes the corresponding action if the
    subcommand is valid.
    """
    user = update.effective_user
    message_text = update.message.text if update.message else ""
    if user:
        logger.info("Command /admin executed by %s (%s)", user.username, user.id)

        # Load parameters from the JSON configuration
        command_params = load_command_params("admin")

        # Get the subcommand and additional parameters
        params = (message_text or "").split(" ", 2)
        if len(params) < 2:
            # If "/admin" was executed without a subcommand
            formatted_keys = "\n".join(
                f"- {key} ({value['desc']})" for key, value in command_params.items()
            )
            if update.message:
                await update.message.reply_text(_("Accessing admin section..."))
                await update.message.reply_text(formatted_keys)
            return

        subcommand = params[1]  # The subcommand after "/admin"
        additional_params = params[2].split(" ") if len(params) > 2 else []

        if subcommand in command_params:
            expected_params = command_params[subcommand]["params"]
            function_name = command_params[subcommand].get("function")

            if len(additional_params) != len(expected_params):
                if update.message:
                    await update.message.reply_text(
                        _("Incorrect number of parameters.")
                    )
                return

            # Create a dictionary with named parameters
            param_dict = {
                expected_params[i]: additional_params[i]
                for i in range(len(expected_params))
            }

            # Get the function from the admin_actions module
            if function_name and hasattr(admin_actions, function_name):
                command_func = getattr(admin_actions, function_name)
                await command_func(update, context, **param_dict)
            else:
                if update.message:
                    await update.message.reply_text(
                        _("Command recognized, but no valid function associated.")
                    )
        else:
            if update.message:
                await update.message.reply_text(_("Unrecognized command."))

    else:
        logger.warning(
            "Access denied. Attempt to execute /admin without user information."
        )
