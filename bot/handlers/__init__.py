"""
Telegram Bot Event Handlers Module.
"""

from .admin_handler import admin_command
from .default_handler import default
from .donate_handler import donate_command
from .help_handler import help_command
from .referrals_handler import referrals_command
from .start_handler import start

__all__ = [
    "start",
    "admin_command",
    "help_command",
    "referrals_command",
    "donate_command",
    "default",
]
