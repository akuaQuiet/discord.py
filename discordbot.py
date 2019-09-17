# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')







@client.event
async def on_message(message):
    if message.content.startswith('/50020'):
        role = discord.utils.get(message.guild.roles, name='全問正解者')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 全問正解です！役職を付与します。'
        await message.channel.send(reply)


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
