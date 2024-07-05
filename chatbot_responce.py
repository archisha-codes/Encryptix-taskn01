def chatbot_response(user_input):
    user_input = user_input.lower()  # Normalize input to lowercase
    
    # Predefined responses based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help you!"
    elif "what is your name" in user_input:
        return "I'm ChatGPT, your virtual assistant."
    elif "what can you do" in user_input:
        return "I can answer your questions, chat with you, and provide information on various topics."
    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "what is the capital of france" in user_input:
        return "The capital of France is Paris."
    elif "who is the president of the united states" in user_input:
        return "As of my last update, the president of the United States is Joe Biden."
    elif "what is the time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have any other questions, feel free to ask."
    elif "goodbye" in user_input or "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "tell me a fact" in user_input:
        return "Did you know? The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion."
    elif "who are you" in user_input:
        return "I'm ChatGPT, a virtual assistant created by OpenAI."
    elif "what is the weather like" in user_input:
        return "I don't have real-time weather information, but you can check a weather website or app for the latest updates."
    elif "can you help me with my homework" in user_input:
        return "Sure, I'd be happy to help! What subject or topic are you working on?"
    elif "what is the meaning of life" in user_input:
        return "The meaning of life is a profound philosophical question. Many believe it is to find happiness and fulfillment."
    else:
        return "I'm sorry, I don't understand that question. Can you please rephrase?"

# Simulating a chat session
if __name__ == "__main__":
    print("ChatGPT: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"ChatGPT: {response}")
        if "goodbye" in user_input or "bye" in user_input:
            break
        