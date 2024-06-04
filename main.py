import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

# .envファイルから環境変数を読み込む
load_dotenv()

# Discordボットのトークン
TOKEN = os.getenv("DISCORD_TOKEN")

# ボットを作成
bot = commands.Bot(command_prefix='!')

#s ボットの準備ができたときの処理
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# メッセージを受信したときの処理
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send('Pong!')

# ボットを実行
bot.run(TOKEN)