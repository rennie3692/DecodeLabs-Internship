# Simple rule-based chatbot
# This bot runs in a loop and responds to a few predefined phrases.

print("Welcome to the simple chatbot! Type 'help' for options or 'quit' to exit.")

while True:
    # Get user input and normalize it for matching.
    user_input = input("You: ").strip().lower()

    # Check for exit commands first.
    if user_input in ["quit", "exit", "bye"]:
        print("Chatbot: Goodbye! Have a great day.")
        break

    # Handle greetings.
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Chatbot: Hello! Nice to meet you.")

    # Handle asking how the bot is doing.
    elif "how are you" in user_input or "how are you doing" in user_input:
        print("Chatbot: I'm just a simple chatbot, but I'm doing well. Thanks for asking!")

    # Handle help requests.
    elif user_input == "help":
        print("Chatbot: I can respond to greetings, tell you how I'm doing, and say goodbye.")
        print("         Try typing 'hello', 'how are you', or 'quit'.")

    # Handle asking for bot name.
    elif "your name" in user_input or "what's your name" in user_input:
        print("Chatbot: I'm a small rule-based bot created to demonstrate simple Python logic.")

    # Default fallback response.
    else:
        print("Chatbot: I'm not sure how to respond to that. Try saying hello or type 'help'.")
