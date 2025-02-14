# pylint: disable=invalid-name
# pylint: disable=R0801
"""
migrations/0001_create_users_table.py

Run:
python -m database.migrations.0001_create_users_table upgrade

Run rollback:
python -m database.migrations.0001_create_users_table downgrade
"""

import sys

from database.db_config import (
    close_db_connection,
    commit_db_connection,
    get_db_connection,
)


def upgrade():
    """
    Create the users table

    Raises:
        sqlite3.DatabaseError: If there is an error executing the SQL query.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE NOT NULL,
            is_admin BOOLEAN DEFAULT 0,
            username TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'active',
            language TEXT DEFAULT 'en',
            cert TEXT DEFAULT NULL
        );
        """
    )

    commit_db_connection(connection)
    close_db_connection(connection)
    print("Migration applied successfully!")


def downgrade():
    """
    Drop the users table (if you need to rollback the migration)

    Raises:
        sqlite3.DatabaseError: If there is an error executing the SQL query.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DROP TABLE IF EXISTS users;
        """
    )

    commit_db_connection(connection)
    close_db_connection(connection)
    print("Migration rolled back successfully!")


if __name__ == "__main__":
    # Get the command (upgrade or downgrade) from command line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "upgrade":
            upgrade()
        elif command == "downgrade":
            downgrade()
        else:
            print("Invalid command. Use 'upgrade' or 'downgrade'.")
    else:
        print("Please specify 'upgrade' or 'downgrade'.")
