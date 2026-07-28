from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os
from memory import add_message, get_history
from agent import solve


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def handle_message(update, context):
    print("Message received!")

    user_id = update.effective_user.id
    text = update.message.text

    print("User said:", text)

    try:
        add_message(user_id, "user", text)

        history = get_history(user_id)

        print("Calling Gemini...")

        answer = solve(text, history)

        print("Gemini replied:", answer)

        add_message(user_id, "assistant", answer)

        await update.message.reply_text(answer)

    except Exception as e:
        print("ERROR:", e)
        raise


def create_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    return app