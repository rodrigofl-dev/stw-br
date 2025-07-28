import logging, os, discord
from logging.handlers import RotatingFileHandler
from discord import app_commands
from dotenv import load_dotenv

import config
from main import user_authentication

load_dotenv()

# log file
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%d-%m-%Y %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Intents and bot setup
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    s = await tree.sync()
    print(s)
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@tree.command(name="ping", description="Replies with Pong!")
async def ping_command(interaction: discord.Interaction):
    #await interaction.response.send_message(":ping_pong: Pong!")
    await interaction.response.send_message(f"Res: {interaction.user.id} | {interaction.user.name} | {interaction.user.global_name}")

@tree.command(name="code", description="Link para gerar o código de autorização.")
async def start_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"## Esse código é de uso único, o Bot não terá acesso à sua conta e nenhum dado será registrado.\
        \n\n - Certifique-se de estar com o navegador logado na conta que deseja verificar.\
        \n - [Acesse o seguinte link]({config.login_link.format(config.client_id)}).\
        \n - Em seguida copie o valor após `\"authorizationCode\":`.\
        \n - Após copiar, use o comando `/check` e cole o código (sem aspas).\
        \n\n OBS: Esse link é fixo, você pode salvar nos seus favoritos para gerar o código sem precisar desse comando."
    )

@tree.command(name="check", description="Compara os alertas de hoje com seu livro de coleção.")
@app_commands.describe(code = 'Cole o código gerado pelo comando `/code`')
async def ping_command(interaction: discord.Interaction, code: str):
    user_access_token, account_id, display_name = user_authentication(code,config.client_header)
    discord_id = interaction.user.id
    discord_name = interaction.user.name

    
    await interaction.response.send_message(f"xxx")


client.run(os.getenv('bot_token'), log_handler=None)
