


print("Chatbot: Hello! Welcome to my chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Chatbot: Hello! How are you?")

    elif "your name" in user:
        print("Chatbot: I am a simple Python chatbot.")

    elif "how are you" in user:
        print("Chatbot: I am fine. Thank you!")

    elif "college" in user:
        print("Chatbot: College is a great place to learn.")

    elif "help" in user:
        print("Chatbot: Sure! How can I help you?")

    elif "bye" in user:
        print("Chatbot: Goodbye! Have a nice day!")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")