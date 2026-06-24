# Task 4: Basic Chatbot

def get_response(user_input):
    """
    Returns a response based on user input.
    """
    # Convert to lowercase for case-insensitive matching
    user_input = user_input.lower().strip()
    
    # Return appropriate response
    if user_input == "hello":
        return "Hi there! How can I help you?"
    elif user_input == "how are you":
        return "I'm doing great, thanks for asking!"
    elif user_input == "bye":
        return "Goodbye! Have a nice day!"
    else:
        return "I didn't understand that. Try 'hello', 'how are you', or 'bye'"


def main():
    """
    Main chatbot loop.
    """
    print("Welcome to CodeAlpha Chatbot!")
    print("Type 'bye' to exit.\n")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Get bot response
        response = get_response(user_input)
        
        # Print response
        print(f"Bot: {response}")
        
        # Exit loop if user says "bye"
        if user_input.lower().strip() == "bye":
            break


# Run the chatbot
if __name__ == "__main__":
    main()