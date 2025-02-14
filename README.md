# Jakanode-bot Project
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![pylint](https://img.shields.io/github/actions/workflow/status/juanjo78git/jakanode-bot/pylint.yml?branch=main&label=pylint&logo=python)
![Version](https://img.shields.io/github/v/release/juanjo78git/jakanode-bot)

A robust and versatile Telegram bot built with Python, designed to streamline automation and enhance user interaction.

## Installing and Setting Up

To set up *jakanode-bot*, follow these steps to create a virtual environment and install the required dependencies:

### Create a Virtual Environment

First, create a virtual environment in the project's root directory. 
You can do this by running the following command:

```bash
python3 -m venv venv
```
This will create a folder named `venv where the virtual environment will be stored.

### Activate the Virtual Environment

Before installing dependencies, activate the virtual environment:
```bash
source venv/bin/activate
```
After activation, your terminal prompt should change to indicate that the virtual environment is active.

### Install Dependencies

Once the virtual environment is activated, install the required dependencies by running:
```bash
pip install -r requirements.txt
```
This command will install all the necessary packages listed in the `requirements.txt` file for `jakanode-bot` to work properly.

### Verify the Installation

After installing the dependencies, you can verify that everything is installed correctly by checking the installed packages:
```bash
pip list
```
This will show a list of installed packages, and you should see the required ones from the `requirements.txt` file.

---

Now, your environment is ready for running jakanode-bot and executing commands like database migrations or running the bot itself.

## Environment Variables

This document explains the environment variables used in the `.env` file for configuring the Jakanode Telegram bot.

### Example `.env` File

```ini
# Telegram Bot Configuration
TOKEN=your-telegram-bot-token
USE_WEBHOOK_BOT=False
WEBHOOK_BOT_URL=https://your-webhook-url.com
WEBHOOK_BOT_PATH=/your-webhook-path
WEBHOOK_BOT_PORT=8443
WEBHOOK_BOT_CERT=/path/to/cert.pem
WEBHOOK_BOT_KEY=/path/to/key.pem

# Internationalization (i18n) Settings
DEFAULT_LANGUAGE=en

# Database Configuration
DB_NAME=db.sqlite3
DB_PATH=./database

# Admin User Configuration
ADMIN_USER_ID=123456789

# Logging Configuration
DEBUG=False
LOG_LEVEL=INFO

# Service and Deployment
SERVICE_NAME=jakanode-bot
USER=your-username
DEV_DIR=/home/your-username/jakanode-bot
PROD_DIR=/opt/jakanode-bot

# Donations
DONATION_LN_ADDRESS=jakanode@lnurl
DONATION_LN_URL=https://jakanode.lnurl
```

---

### Environment Variables Explanation

#### Telegram Bot Configuration

- `TOKEN`: The authentication token for your Telegram bot.
- `USE_WEBHOOK_BOT`: Set to `True` to enable webhook mode; otherwise, the bot will use polling.
- `WEBHOOK_BOT_URL`: The public URL where Telegram will send updates when using webhook mode.
- `WEBHOOK_BOT_PATH`: The specific endpoint path for webhook updates.
- `WEBHOOK_BOT_PORT`: The port used for webhook communication.
- `WEBHOOK_BOT_CERT`: Path to the SSL certificate required for webhook.
- `WEBHOOK_BOT_KEY`: Path to the private key associated with the SSL certificate.

#### Internationalization (i18n) Settings

- `DEFAULT_LANGUAGE`: Default language code used by the bot (e.g., `en`, `es`).

#### Database Configuration

- `DB_NAME`: The name of the SQLite database file.
- `DB_PATH`: Directory where the database file is stored.

#### Admin User Configuration

- `ADMIN_USER_ID`: The Telegram user ID of the bot administrator.

#### Logging Configuration

- `DEBUG`: Set to `True` to enable debug mode.
- `LOG_LEVEL`: Logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`).

#### Service and Deployment

- `SERVICE_NAME`: The name of the bot service.
- `USER`: The system username running the bot.
- `DEV_DIR`: The directory where the bot is located during development.
- `PROD_DIR`: The directory where the bot is deployed in production.

#### Donations

- `DONATION_LN_ADDRESS`: The Lightning Network address for receiving donations.
- `DONATION_LN_URL`: The public URL for the donation page.

---

#### How to Use the `.env` File

1. Create a `.env` file in the project root.
2. Copy and paste the example content above.
3. Replace the placeholder values with your actual configuration.
4. The bot will automatically load these settings when it starts.

For further assistance, refer to the bot's documentation or contact the maintainer. 🚀

## Database Migrations

To manage database schema changes and ensure your database is up-to-date with the latest structure,
*jakanode-bot* includes a migration system. This system allows you to automatically apply any pending migrations,
including creating new tables or altering existing ones.

### Creating SQLite3 Database

To create the SQLite3 database, run the following command from the root directory of the project. 
If the database doesn't exist, it will be automatically created:

```bash
sqlite3 db.sqlite3
```
Make sure that the database-related variables in the `.env` file are correctly configured. 
These variables define the database connection settings that *jakanode-bot* will use.

### Running Database Migrations

To execute all pending database migrations and apply any necessary changes to your database, 
run the following command from the root directory of your project:

```bash
python -m database.migrate
```
And verify that the changes have been applied successfully by checking the database:

```bash
sqlite3 db.sqlite3
```
```sql
.headers on
.mode column
SELECT * FROM migrations;
.tables
```

## Translations
To generate and update translations, follow these steps:

1. **Extract new text strings**: 
    First, extract all the translatable text strings from the source code into a .pot file. 
    Run the following command from the project's root directory:
    
    ```bash
    xgettext -L Python --from-code=UTF-8 -o i18n/locales/messages.pot $(find . -path ./venv -prune -o -name "*.py" -print)
    ```
    This command searches for all Python files `(*.py)`, excluding the `venv` folder (if you have a virtual environment), 
    and generates a `messages.pot` file containing all the text strings.

2. **Merge the new strings into existing `.po` files**: 
    If you already have translation files for languages like Spanish and English, 
    you need to merge the newly extracted strings into the corresponding `.po` files. 
    If the `.po` files don't already exist, create empty ones for each language before merging:

    ```bash
    touch i18n/locales/es/LC_MESSAGES/messages.po 
    touch i18n/locales/en/LC_MESSAGES/messages.po
    ```
    Then, merge the new strings into the `.po` files:

    ```bash
    msgmerge -U i18n/locales/es/LC_MESSAGES/messages.po i18n/locales/messages.pot 
    msgmerge -U i18n/locales/en/LC_MESSAGES/messages.po i18n/locales/messages.pot
    ```
3. **Generate the compiled `.mo` files**: 
    After updating the `.po` files with the translations, 
    compile them into `.mo` files that can be used by the project at runtime:
    
    ```bash
    msgfmt i18n/locales/es/LC_MESSAGES/messages.po -o i18n/locales/es/LC_MESSAGES/messages.mo 
    msgfmt i18n/locales/en/LC_MESSAGES/messages.po -o i18n/locales/en/LC_MESSAGES/messages.mo 
    ```
    The `.mo files are the ones jakanode-bot will use to load translations at runtime.

## Features

### Admin Features

**Only the admin can execute these commands**
These commands are exclusively available to the bot admin. 
For security reasons, admin options are concealed in the Telegram menu to prevent unauthorized access.

#### Script Management

These scripts can be triggered via the Telegram bot to automate various tasks.

##### Available Scripts

You can view the available scripts by using the command `/admin scripts`.

- `test.sh`: A test script to ensure that the bash script can be executed successfully.

- `system-info.sh`: Provides information about the system's status.
- `nginx-restart.sh`: Restarts the web server in a controlled manner.
- `system-restart.sh`: Restarts the system in a controlled manner.
- `system-stop.sh`: Shuts down the system safely.

- `bot-log.sh`: Displays the bot's logs to help diagnose any issues.
- `bot-restart.sh`: Restarts the bot service (SERVICE_NAME).
- `bot-stop.sh`: Stops the bot service (SERVICE_NAME).
- `bot-deploy.sh`: Deploys new versions to production environment (DEV -> PROD).

- `git-status.sh`: Shows the current status of the local repository (DEV).
- `code-quality.sh`: Checks the code quality in the local repository (DEV).
- `git-pull.sh`: Updates the local repository with the latest changes from the remote repository (DEV).
- `git-commit.sh`: Performs a commit in the local repository (DEV).
- `git-push.sh`: Pushes local changes to the remote repository (DEV).

To run any script, use the command `/admin run SCRIPT_NAME`.

#### User Management

These commands allow you to manage and view information about system users.

- `/admin users`: Lists all users on the system.
- `/admin user TELEGRAM_ID`: Displays detailed information about the user with the specified Telegram ID (`XXX`).

#### Referrals Management

These commands allow you to manage and view information about system users.

- `/admin new_referral REFERRAL_NAME REFERRAL_URL`: Adds a new referral link by specifying the referral's name and URL.


### Public Features

#### Bot Commands

These are commands available for all users to interact with the bot.

- `/start`: Initializes the bot and saves the user.
- `/help`: Displays the help information about the bot and how to use its features.
- `/donate`: Shows how to make a donation to support the bot. 
  Donations can be made via the Lightning Network. 
  You can optionally specify an amount (e.g., `/donate 10`).
- `/referrals`: Displays referral links that you can share with others to earn rewards.
