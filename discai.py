import openai
import requests
import io
from PIL import Image
import discord

openai.api_key = "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"

MESSAGE_CONNECTED = "Bot foi conectado como "
MESSAGE_GPT3 = "!gpt3"

client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f'{MESSAGE_CONNECTED} {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(MESSAGE_GPT3):
        previous_messages = []
        async for msg in message.channel.history(limit=50):
            if msg.author == client.user:
                continue
            previous_messages.append(msg.content)
        context = "\n".join(previous_messages)
        task = message.content[len(MESSAGE_GPT3)+1:]
        temperature = 0.5
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"{context}\n{task}",
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=temperature,
             )
            response_text = response["choices"][0]["text"]
            if len(response_text) > 2000:
                response_text = response_text[:2000] + "..."
            await message.channel.send(response_text)
        except:
            await message.channel.send("Desculpe, ocorreu um erro ao processar sua solicitação.")

        if message.content.startswith('!dalle'):
            intent = message.content[7:]
            response = openai.Image.create(
                model="image-alpha-001",
                prompt=f"{intent}"
            )
            image_url = response["data"][0]["url"]
            response = requests.get(image_url)
            image = Image.open(io.BytesIO(response.content))
            image_file = io.BytesIO()
            image.save(image_file, format='PNG')
            image_file.seek(0)
            await message.channel.send(file = discord.File(image_file, 'image.png'))

client.run("MTA2OTY0NzQ5MjU5MDg2NjU5Mw.GFkFFk.ZMN_4Adk4iDCN0QZ2pRECoZmU3nzzgpjMds6vQ")
