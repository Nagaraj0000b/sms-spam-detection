def simple_chatbot():
    """
    A simple rule-based chatbot that responds to user input.
    """
    print("🤖 Hi! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        # Get user input
        user_input = input("You: ").lower() # Convert input to lowercase for easier matching

        # Check for user input and respond accordingly
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great!")
        elif "what is your name" in user_input:
            print("Chatbot: I am a simple AI agent.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break # Exit the loop and end the program
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

if __name__ == "__main__":
    simple_chatbot()