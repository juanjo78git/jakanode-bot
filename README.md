# Jakanode Project

This is a simple built with Python.

## .env file
```
# Bot configuration
TOKEN=your_telegram_bot_token
USE_WEBHOOK_BOT=true
WEBHOOK_BOT_URL=webhook_url
WEBHOOK_BOT_PATH=webhook_path
WEBHOOK_BOT_PORT=webhook_port
WEBHOOK_BOT_CERT=webhook_ssl_cert
WEBHOOK_BOT_KEY=webhook_ssl_key

# Admin user
ADMIN_USER_ID=your_telegram_id

DEFAULT_LANGUAGE=en

# Database configuration
DB_NAME=db.sqlite3
DB_PATH=./database

# Environment configuration
DEBUG=True
LOG_LEVEL=INFO
```

## Translations
```
# Get the new texts
xgettext -L Python --from-code=UTF-8 -o i18n/locales/messages.pot $(find . -path ./venv -prune -o -name "*.py" -print)
# Merge them into the current .po files
touch i18n/locales/es/LC_MESSAGES/messages.po 
touch i18n/locales/en/LC_MESSAGES/messages.po 
msgmerge -U i18n/locales/es/LC_MESSAGES/messages.po i18n/locales/messages.pot 
msgmerge -U i18n/locales/en/LC_MESSAGES/messages.po i18n/locales/messages.pot 
# Generate the compiled .mo files
msgfmt i18n/locales/es/LC_MESSAGES/messages.po -o i18n/locales/es/LC_MESSAGES/messages.mo 
msgfmt i18n/locales/en/LC_MESSAGES/messages.po -o i18n/locales/en/LC_MESSAGES/messages.mo 
```

## Create Database Tables
```
python -m database.migrations.0001_create_users_table upgrade
```
