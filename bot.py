import json
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Helpers
from packages.helpers.generators.greeting import start_command, login_command
from packages.helpers.responses.handlers import handle_menu

with open('configs/telegram.json', 'r') as config_file:
    config = json.load(config_file)

TOKEN: Final = config['TOKEN']

if __name__ == '__main__':
    print('Bot is running')
    app = Application.builder().token(TOKEN).build()

    # Command
    app.add_handler(CommandHandler('start', login_command))
    app.add_handler(CommandHandler('home', start_command))
    
    # app.add_handler(CommandHandler('help', help_command))
    # app.add_handler(CommandHandler('custom', custom_command))    

    # Response
    app.add_handler(MessageHandler(filters.TEXT, handle_menu))
    # app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)