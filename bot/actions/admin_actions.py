"""
Users actions
"""

from telegram import Update
from telegram.ext import ContextTypes

from bot.actions.referrals_actions import add_referral
from services.script_service import get_scripts, run_script
from services.user_service import get_user_by_telegram_id, get_user_list


# pylint: disable=unused-argument
async def users_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Retrieves and formats the list of all users.

    Args:
        update (Update): The update object that contains the message and context.
        context (ContextTypes.DEFAULT_TYPE): The context for the command handler.

    Returns:
        None: Sends a formatted message with user information.

    Raises:
        None: No exceptions are raised.
    """
    users = get_user_list()
    if users:
        user_list_message = _("User list:\n\n")
        for user in users:
            user_list_message += _(
                "ID: {id}\n"
                "Telegram ID: {telegramid}\n"
                "Username: {username}\n"
                "Status: {status}\n"
                "Admin: {admin}\n\n"
            ).format(
                id=user["id"],
                telegramid=user["telegram_id"],
                username=user["username"],
                status=user["status"],
                admin=user["is_admin"],
            )
        if update.message:
            await update.message.reply_text(user_list_message)
    else:
        if update.message:
            await update.message.reply_text(_("No users found."))


# pylint: disable=unused-argument
async def user_detail(
    update: Update, context: ContextTypes.DEFAULT_TYPE, telegram_id
) -> None:
    """
    Retrieves and formats the details of a user by their Telegram ID.

    Args:
        update (Update): The update object containing the message and context.
        context (ContextTypes.DEFAULT_TYPE): The context for the command handler.
        telegram_id (int): The Telegram ID of the user.

    Returns:
        None: Sends a message with the user's details.

    Raises:
        None: No exceptions are raised.
    """
    user_info = get_user_by_telegram_id(telegram_id)
    if user_info:
        formatted_info = "\n".join(
            [
                f"- {key.capitalize()}: {value if value is not None else 'N/A'}"
                for key, value in user_info.items()
            ]
        )
        if update.message:
            await update.message.reply_text(formatted_info)
    else:
        if update.message:
            await update.message.reply_text(_("No users found."))


# pylint: disable=unused-argument
async def exec_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Retrieves and formats the list of executable scripts.

    Args:
        update (Update): The update object that contains the message and context.
        context (ContextTypes.DEFAULT_TYPE): The context for the command handler.

    Returns:
        None: Sends a message with the list of available scripts.

    Raises:
        None: No exceptions are raised.
    """
    script_list = get_scripts()
    if script_list:
        # Sort the list alphabetically
        script_list.sort()
        # Format the list to make it clearer
        formatted_list = "\n".join(f"- {script}" for script in script_list)
        if update.message:
            await update.message.reply_text(formatted_list)
    else:
        if update.message:
            await update.message.reply_text(_("No scripts found."))


# pylint: disable=unused-argument
async def exec_script(
    update: Update, context: ContextTypes.DEFAULT_TYPE, script_name
) -> None:
    """
    Executes a script.

    Args:
        update (Update): The update object containing the message and context.
        context (ContextTypes.DEFAULT_TYPE): The context for the command handler.
        script_name (str): The name of the script to execute.

    Returns:
        None: Sends a message with the script execution result.

    Raises:
        None: No exceptions are raised.
    """
    result = run_script(script_name)
    if result:
        if update.message:
            await update.message.reply_text(result)
    else:
        if update.message:
            await update.message.reply_text(_("Unrecognized command."))


# pylint: disable=unused-argument
async def new_referral(
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
    await add_referral(update=update, context=context, name=name, url=url)
