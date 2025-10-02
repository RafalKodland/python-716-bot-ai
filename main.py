import discord
from discord.ext import commands
from model import get_class
from os import remove

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def image(ctx):
    if len(ctx.message.attachments) > 0:
        for attachment in ctx.message.attachments:
            if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                await ctx.typing()
                file_path = f"./files/{attachment.filename}"
                await attachment.save(file_path)
                class_name, confidence = get_class(file_path)
                await ctx.send(f'Wykryto klasę: {class_name} z prawdopodobieństwem {confidence*100.0:.2f}%')
                remove(file_path)
            else:
                await ctx.send('Obrazek musi być w formacie PNG, JPG lub JPEG')
    else:
        await ctx.send('Komenda nie zadziała bez załączonego obrazka')
            

bot.run("")