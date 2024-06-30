import os
import discord
import sys
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

if __name__ == '__main__':
    pass

# .envファイルから環境変数を読み込む
load_dotenv()

# Discordボットのトークン
TOKEN = os.getenv("DISCORD_TOKEN")
# Intentsを設定
intents = discord.Intents.default()
intents.messages = True  # メッセージコンテンツを取得するために必要
if sys.platform == "win32":
    intents.message_content = True
# ボットを作成
bot = commands.Bot(command_prefix='!',intents=intents)

#s ボットの準備ができたときの処理
@bot.event
async def on_ready():
    print(f'{bot.user.name} が接続しました!')
@bot.event
async def on_disconnect():
    print('ボットが切断されました。')
# メッセージを受信したときの処理
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!ping'):
        await message.channel.send('Pong!')

# イベントループの取得と開始
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(bot.start(TOKEN))
except KeyboardInterrupt:
    loop.run_until_complete(bot.close())
finally:
    loop.close()