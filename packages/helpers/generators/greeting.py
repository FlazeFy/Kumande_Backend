from telegram import Update
from telegram.ext import ContextTypes

async def login_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Kumande\nMake food scheduling, analyze it, tracking, and choose your meals for tommorrow')
    await update.message.reply_text('Type your username : ')
    
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('What do you want \n1. Show consume history\n2. Show my calorie needs\n3. Add consume\n4. Update consume\n5. Delete consume\n6. Show schedule\n7. Edit schedule\n8. Show stats\n9. Show my profile\n10. Change password\n\n 0. Exit bot')