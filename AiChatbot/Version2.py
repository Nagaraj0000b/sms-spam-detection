# A learning AI chatbot using the ChatterBot library

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot named 'MyChatBot'
# The logic_adapters tell the bot how to pick a response.
# 'chatterbot.logic.BestMatch' finds the closest match to the user's input from the training data.
bot = ChatBot(
    'MyChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)


# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot on the english corpus
# This is a large dataset of general English conversations.
# This step might take a few moments the first time you run it.
print("Training the bot...")
trainer.train(
    "chatterbot.corpus.english"
)
print("Training complete!")


# Start a conversation
print("🤖 Hello! I am a learning chatbot. Type 'quit' to exit.")
while True:
    try:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break

        # Get a response from the bot
        bot_response = bot.get_response(user_input)
        print(f"Chatbot: {bot_response}")

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
