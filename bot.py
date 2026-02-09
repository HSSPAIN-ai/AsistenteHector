import discord
from discord.ext import commands
import os

# Activar intents para que el bot pueda leer mensajes
intents = discord.Intents.default()
intents.message_content = True

# Prefijo para comandos
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento cuando el bot se conecta
@bot.event
async def on_ready():
    print(f"Estoy conectado como {bot.user}")

# Comando simple: !hola
@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! ¿Cómo estás?")

# Responder a cualquier mensaje que lo mencione
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        await message.channel.send("¿Me has llamado? Aquí estoy.")

    await bot.process_commands(message)

# Iniciar bot con el TOKEN de Render
bot.run(os.getenv("TOKEN"))

