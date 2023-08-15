import discord
import openai

# Replace with your OpenAI API key
openai_api_key = 'your-api-key-here'
openai.api_key = openai_api_key

# Function to analyze conversation and provide nonviolent communication response
def analyze_conversation(conversation):
    participants = conversation.split('\n')
    dialogue = " ".join(participants)

    prompt = (
        f"This is a conversation between two individuals:\n{dialogue}\n"
        "Please provide an analytic breakdown of the conversation, identifying the following:"
        "\n1. Recognize the primary emotions exhibited by each participant using Emotional Intelligence."
        "\n2. Identify areas for clarification and encourage open-ended questions through Active Listening."
        "\n3. Detect passive or aggressive language and suggest open but respectful communication with Assertiveness Training."
        "\n4. Uncover negative thought patterns and provide alternative ways of thinking using Cognitive-Behavioral Techniques."
        "\n5. Encourage presence, engagement, and empathy through Mindfulness."
        "\n6. Translate charged language into compassionate communication, identifying the giraffe and jackal aspects, using Nonviolent Communication."
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )

    return response.choices[0].text


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    statement = message.content
    response = analyze_conversation(statement)
    await message.channel.send(f"Nonviolent Communication: {response}")

# Replace with your bot token
client.run('your-bot-token-here')
