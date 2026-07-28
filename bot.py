from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os
import json
from memory import add_message, get_history
from agent import Agent


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

agent = Agent()


async def handle_message(update, context):
    print("Message received!")

    user_id = update.effective_user.id
    text = update.message.text

    print("User said:", text)

    try:
        add_message(user_id, "user", text)

        history = get_history(user_id)

        print("Calling Agent...")

        result = agent.solve(text)

        print("Agent replied:", result)

        add_message(user_id, "assistant", json.dumps(result))

        await update.message.reply_text(
            json.dumps(result, indent=2)
        )

    except Exception as e:
        print("ERROR:", e)
        raise


def create_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    return app