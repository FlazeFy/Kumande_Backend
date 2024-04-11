from telegram import Update
from telegram.ext import ContextTypes

async def login_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Kumande\nMake food scheduling, analyze it, tracking, and choose your meals for tommorrow')
    await update.message.reply_text('Type your username : ')
    
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('What do you want \n1. Show consume\n2. Add consume\n3. Update consume\n4. Delete consume\n5. Show schedule\n6. Edit schedule\n7. Show stats\n8. Show my profile\n9. Change password\n\n 0. Exit bot')