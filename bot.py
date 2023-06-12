import logging
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram import ChatAction

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up OpenAI API
openai.api_key = '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'

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a chatbot. How can I assist you?")

# Define a function to handle incoming messages
def echo(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

    # Get user input
    user_input = update.message.text

    # Call OpenAI API to generate a response
    response = openai.Completion.create(
        engine='davinci',
        prompt=user_input,
        max_tokens=50
    )

    # Get the generated response from OpenAI
    generated_text = response.choices[0].text.strip()

    # Send the response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=generated_text)

def main():
    # Create an instance of the Updater class
    # Remember to replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
    updater = Updater(token='1796879062:AAGXbrKEy0SReCFCPLy_tjm6op0WrFumcCM', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
