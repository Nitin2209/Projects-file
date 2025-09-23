
# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler
# from telegram.ext import filters  # Use this for version 20+
# from telegram.constants import ParseMode
# import requests
# import logging
# import os

# # Set up logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# # Define Hugging Face API token and Telegram Bot token
# HUGGINGFACE_API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')
# TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# # Check if tokens are available
# if not HUGGINGFACE_API_TOKEN or not TELEGRAM_BOT_TOKEN:
#     logger.error("Error: Environment variables are not set properly!")
# else:
#     logger.info("Environment variables loaded successfully.")

# # Start command handler
# async def start(update: Update, context) -> None:
#     await update.message.reply_text(
#         "Hello! I'm an AI-powered bot. Send me a prompt, and I will generate an image for you. For example:\n\n"
#         "'A futuristic city skyline at sunset.'"
#     )

# # Image generation using Hugging Face API
# async def generate_image(prompt: str) -> str:
#     headers = {
#         'Authorization': f'Bearer {HUGGINGFACE_API_TOKEN}',
#         'Content-Type': 'application/json'
#     }
#     data = {'inputs': prompt}

#     try:
#         response = requests.post(
#             'https://api-inference.huggingface.co/models/artificialguybr/3DRedmond-V1',
#             headers=headers,
#             json=data
#         )
#         response.raise_for_status()

#         content_type = response.headers.get('Content-Type')
#         logger.info(f"Received content type: {content_type}")

#         if 'image' in content_type:
#             image_path = 'output_image.png'
#             with open(image_path, 'wb') as f:
#                 f.write(response.content)
#             return image_path
#         else:
#             logger.error(f"Unexpected content type received: {content_type}")
#             return f"Error: Unexpected content type received: {content_type}"

#     except requests.exceptions.RequestException as e:
#         logger.error(f"Error during API request: {e}")
#         return f"Error: {str(e)}"

# # Message response handler
# async def respond(update: Update, context) -> None:
#     user_message = update.message.text.strip()
#     if not user_message:
#         return

#     await update.message.reply_text("Generating your image... Please wait.", parse_mode=ParseMode.HTML)
#     image_path = await generate_image(user_message)

#     if os.path.exists(image_path):
#         await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(image_path, 'rb'))
#         os.remove(image_path)
#     else:
#         await update.message.reply_text(image_path)

# # Help command handler
# async def help_command(update: Update, context) -> None:
#     await update.message.reply_text(
#         "Commands:\n"
#         "/start - Welcome message\n"
#         "Just send me a prompt to generate an image.\n"
#         "/help - Show this help message"
#     )

# # Main bot function
# def create_bot():
#     app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

#     # Add handlers for start, help, and text message
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("help", help_command))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

#     return app

import os
import logging
import requests
import asyncio
from io import BytesIO
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)
from telegram.constants import ParseMode

# Load environment variables from .env file
load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

if not HUGGINGFACE_API_TOKEN or not TELEGRAM_BOT_TOKEN:
    logger.error("Environment variables are not set properly!")
else:
    logger.info("Environment variables loaded successfully.")


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! I am an AI-powered bot.\n"
        "Send me a prompt and I will generate an image.\n\n"
        "Example: A futuristic city skyline at sunset."
    )


# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help message\n\n"
        "Send me any text prompt and I will generate an image."
    )


# Generate image using Hugging Face API
async def generate_image(prompt: str) -> BytesIO | str:
    def _call_api():
        headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
            "Content-Type": "application/json",
        }
        data = {"inputs": prompt}
        response = requests.post(
            "https://api-inference.huggingface.co/models/artificialguybr/3DRedmond-V1",
            headers=headers,
            json=data,
            timeout=120,
        )
        response.raise_for_status()
        return response

    try:
        response = await asyncio.to_thread(_call_api)
        content_type = response.headers.get("Content-Type", "")

        if "image" in content_type:
            return BytesIO(response.content)  # return in-memory image
        else:
            return f"Unexpected response: {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


# Handle user messages
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.strip()
    if not user_message:
        return

    await update.message.reply_text("Generating your image... Please wait.")
    result = await generate_image(user_message)

    if isinstance(result, BytesIO):
        result.seek(0)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=result)
    else:
        await update.message.reply_text(result)


# Main bot function
def create_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))
    return app


if __name__ == "__main__":
    bot_app = create_bot()
    bot_app.run_polling()
