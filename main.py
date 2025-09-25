import discord
from discord.ext import commands

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
                await attachment.save(f"./files/{attachment.filename}")
                await ctx.send(f'Zapisano obrazek: {attachment.filename}')
            else:
                await ctx.send('Obrazek musi być w formacie PNG, JPG lub JPEG')
    else:
        await ctx.send('Komenda nie zadziała bez załączonego obrazka')
            

bot.run("")