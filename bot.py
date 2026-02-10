import discord
from discord.ext import commands
import os

# Intents necesarios para que el bot lea mensajes
intents = discord.Intents.default()
intents.message_content = True

# Prefijo para comandos
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento cuando el bot se conecta
@bot.event
async def on_ready():
    print(f"Estoy conectado como {bot.user}")

# Respuesta automática a mensajes normales
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Responder si alguien dice "hola"
    if message.content.lower() == "hola":
        await message.channel.send("¡Hola! ¿Qué tal estás?")

    # Responder si mencionan al bot
    if bot.user.mentioned_in(message):
        await message.channel.send("¡Me has llamado? Aquí estoy :)")

    # Procesar comandos (!hola, etc.)
    await bot.process_commands(message)

# Comando !hola
@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! ¿Cómo estás?")

# Iniciar el bot con el TOKEN de Render
bot.run(os.getenv("TOKEN"))
