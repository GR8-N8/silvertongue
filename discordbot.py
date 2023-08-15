import discord
import openai

# Replace with your OpenAI API key
openai_api_key = 'your-api-key-here'
openai.api_key = openai_api_key

# Function to analyze conversation and provide nonviolent communication response
def analyze_conversation(statement):
    prompt = f"Please translate the following emotionally charged statement into nonviolent communication: {statement}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60
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
