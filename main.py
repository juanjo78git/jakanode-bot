"""
Main entry point
"""

from bot.bot import main
from database.db_config import init_db

if __name__ == "__main__":
    init_db()
    main()
