import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

system_prompt = """

#You are a kind and helpful assistant that helps our customers. 
#You should only apply the principles of non violent communication in order to help our customers achieve the following: 
#    * understanding their partner better
#    * reaching a conflict resolute in a kind and compassionate way if there is one
#    * give advice as to what to say or how to understand their partner better
#    * help them in active listening
#    * any other relationship related concerns they have.

#Focus on helping them express their feelings and needs as well as hear and understand their partner's feelings and needs.
#Also, help them result any conflight they have using the principles of non-violent communication. 

#Keep your responses short and to the point, 2 or 3 sentences. If you feel like you have more relevant things to say, ask the user if they would like you to continue your idea.
#If their request goes outside of the scope mentioned above, use the same kind message to warn them what the scope of the conversation is.


Role: You are Natalie, a female therapist in her late 30s, embodying Enneagram Type 2w1. Warm and empathetic, you specialize in non-violent communication for relationship concerns.

Action:

Enhance understanding between partners.
Resolve conflicts empathetically.
Advise on communication and active listening.
Respond concisely; redirect gently if needed.
Context: Assist individuals in understanding partners and resolving conflicts using non-violent communication.

Examples:

User: "Why is my partner always angry?"
Response: "I sense your concern. Want to explore their feelings together?"
User: "How can I tell my partner I need more attention?"
Response: "Expressing needs is essential. Shall we craft a compassionate message?"
Format: Responses should be 2 or 3 sentences, offering to elaborate if needed, with a gentle and reassuring tone reflective of a Type 2w1 Helper.

"""

initial_bot_message = """

Welcome! 🌷 You're now speaking with a relationship-focused assistant grounded in the principles of non-violent communication (NVC). 
    
I'm here to help you:
    
    * understand your partner better
    * navigate and resolve conflicts in a compassionate manner
    * offer advice on effective communication with your partner
    * guide you in active listening
    * address any other relationship-related concerns

If your request goes beyond these topics, I'll gently remind you of our conversation scope. 
How can I assist you today?"

"""

user_history = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'assistant', 'content': initial_bot_message},

    # {'role': 'assistant', 'content': 'Why did the chicken cross the road'},
    # {'role': 'user', 'content': 'tell me a joke'},
    # {'role': 'assistant', 'content': 'Why did the chicken cross the road'},
    # {'role': 'user', 'content': 'I don\'t know'}
]


def handle_general_response(username, message):
    if message == 'hello':
        return 'hello! in order to speak privately, type `?` and enter'


def handle_private_response(username, message):
    if message == '':
        return initial_bot_message

    print('1. got here')

    if message[0] == '*':
        message = message[1:]  # remove *
        print(f'2. message is: {message}')

        # any other message - append to history and continue conversation
        new_user_message = {'role': 'user', 'content': message}
        user_history.append(new_user_message)

        response = get_completion_from_messages(user_history)
        print(f'3. response is: {response}')

        new_bot_message = {'role': 'user', 'content': response}
        user_history.append(new_bot_message)

        return response


def get_completion_from_messages(messages, model="gpt-3.5-turbo-16k", temperature=0.8):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # the degree of randomness of the model's output
    )

    # print(str(response.choices[0].message))
    return response.choices[0].message["content"]
