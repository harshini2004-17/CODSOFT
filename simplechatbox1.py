def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I assist you?")
        elif user_input in ["how are you?", "how are you doing?", "what's up?"]:
            print("Chatbot: I'm just a program, but thanks for asking! How can I help you?")
        elif user_input in ["what is your name?", "who are you?"]:
            print("Chatbot: I'm a simple chatbot created to assist you.")
        elif user_input in ["help", "can you help me?", "i need help"]:
            print("Chatbot: Sure! What do you need help with?")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
