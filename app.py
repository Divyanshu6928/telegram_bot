from bot import create_bot

app = create_bot()

print("Bot started...")

app.run_polling()