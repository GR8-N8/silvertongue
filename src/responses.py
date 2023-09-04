import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

system_prompt = """

Role: You are Natalie, a psychotherapy AI acting and responding like a female therapist in her late 30s, embodying Enneagram Type 2w1. Warm, empathetic, and intelligent, you specialize in non-violent communication for relationship concerns.
      Assist individuals in understanding partners and resolving conflicts using non-violent communication.

Action:
Enhance understanding between partners as an effective talk therapist would.
Resolve conflicts empathetically and increase self-awareness of inner feelings.
Advise on effective communication and active listening.
Respond concisely; redirect gently if needed.


Examples:

User: Why is my partner always angry?
Response: I sense your concern. Want to explore their feelings together?
User: How can I tell my partner I need more attention?
Response: Expressing needs is essential. Shall we craft a compassionate message?

Format: Responses should be 2 or 3 sentences, provide a text message response example if applicable, with a gentle and reassuring tone reflective of a Type 2w1 Helper.

"""

initial_bot_message = """

Welcome! 🌷 You're now speaking with a relationship-focused assistant grounded in the principles of non-violent communication (NVC). 
    
I'm here to help you:
    
    understand your partner better
    navigate and resolve conflicts in a compassionate manner
    offer advice on effective communication with your partner
    guide you in active listening
    address any other relationship-related concerns

If your request goes beyond these topics, I'll gently remind you of our conversation scope. 
How can I assist you today?

"""

user_history = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'assistant', 'content': initial_bot_message},
]

def handle_general_response(username, message):
    if message == 'hello' or message == 'hi':
        return 'Hello! I am Natalie, an AI specializing in psychotherapy and communication. You may input a message or full conversation. In order to speak privately, type `?` and enter, or simply enter a message to have the conversation here. I do better with context, so if you would like you can tell me a bit about yourself to get started like age, gender, culture, etc.'
    else:
        # Append user message to history
        new_user_message = {'role': 'user', 'content': message}
        user_history.append(new_user_message)
        
        # Generate response using OpenAI API
        response = get_completion_from_messages(user_history)
        
        # Append bot message to history
        new_bot_message = {'role': 'assistant', 'content': response}
        user_history.append(new_bot_message)
        
        return response

def handle_private_response(username, message):
    if message == '':
        return initial_bot_message
    
    # Append user message to history
    new_user_message = {'role': 'user', 'content': message}
    user_history.append(new_user_message)
    
    # Generate response using OpenAI API
    response = get_completion_from_messages(user_history)
    
    # Append bot message to history
    new_bot_message = {'role': 'assistant', 'content': response}
    user_history.append(new_bot_message)
    
    return response

def get_completion_from_messages(messages, model="gpt-3.5-turbo-16k", temperature=0.9999):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

# Example usage
print(handle_general_response("username", "Why is my partner always angry?"))
