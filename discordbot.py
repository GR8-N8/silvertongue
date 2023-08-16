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
         f"Participant A has expressed the following concerns:\n{participant_a_story}\n"
        f"Participant B has expressed the following concerns:\n{participant_b_story}\n"
        "Based on non-violent communication principles, please help them understand each other's needs and feelings. "
        "Identify the underlying causes of their disagreement, and suggest ways they might reach a common agreement. "
        "Include an analysis of emotions, communication styles, and opportunities for compassionate understanding."
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
