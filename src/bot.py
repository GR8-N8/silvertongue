import discord
import responses
from dotenv import dotenv_values


async def send_message(message, username, user_message, is_private):
    try:
        if is_private:
            response = responses.handle_private_response(username, user_message)
            await message.author.send(response)
        else:
            response = responses.handle_general_response(username, user_message)
            await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):

        # prevents the bot from entering an infinite loop where it responds to itself
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said {user_message} (in channel {channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, username, user_message, is_private=True)
        else:
            await send_message(message, username, user_message, is_private=False)

    config = dotenv_values(".env")
    client.run(config['DISCORD_TOKEN'])
