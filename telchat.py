import telebot
import random
import re

# Replace with your actual Telegram bot token
#pip install pyTelegramBotAPI

token = ""

bot = telebot.TeleBot(token)

# Handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hey, how are you?")

# Handle the /help command
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, '''
    Available Commands:
    
    /start -> Greeting the user
    /help -> List all available commands

    /calculate [expression] -> Perform calculation (e.g., /calculate 3 * 5)
    /joke -> Get a random joke

    Simply type any of the commands to use them!
    ''')

# Handle the /calculate command
@bot.message_handler(commands=['calculate'])
def calculate(message):
   
    # Extract the expression from the message
    expression = message.text[len("/calculate "):].strip()
    try:


        # Use a regular expression to ensure the input is a valid mathematical expression
        if re.match(r'^\d+(\s*[\+\-\*\/]\s*\d+)+$', expression):
            try:
                # Evaluate the expression
                result = eval(expression)
                bot.reply_to(message, f"The result of {expression} is: {result}")
            except Exception as e:
                bot.reply_to(message, f"Error in calculation: {e}")
        else:
            bot.reply_to(message, "Please enter a valid mathematical expression like '/calculate 3 * 5'.")

    except Exception as e:
        print(e)

# Handle the /joke command
@bot.message_handler(commands=['joke'])
def joke(message):
    # List of jokes
    jokes = [
        "Why don't skeletons fight each other? Because they don't have the guts! 😄",
        "Why don’t some couples go to the gym? Because some relationships don’t work out! 😅",
        "I told my wife she was drawing her eyebrows too high. She looked surprised! 😂",
        "Why don't eggs tell jokes? They might crack up! 🥚",
        "What do you call fake spaghetti? An impasta! 🍝"
    ]
    # Choose a random joke
    selected_joke = random.choice(jokes)
    bot.reply_to(message, selected_joke)

# Function to start the bot polling
def run_bot():
    bot.polling()

if __name__ == "__main__":
    run_bot()
