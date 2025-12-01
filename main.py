import discord
import ezcord
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('TOKEN')
def parse_id_set(env_value: str):
    if not env_value:
        return set()
    parts = [p.strip() for p in env_value.split(",") if p.strip()]
    ids = set()
    for p in parts:
        ids.add(int(p))
    return ids

BAN_CHANNEL_IDS = parse_id_set(os.getenv("CHANNELS", ""))
IGNORE_ROLE_IDS = parse_id_set(os.getenv("IGNORE_ROLES", ""))
BAN_REASON = os.getenv("BAN_REASON", "Posted in the ban channel >:)")
webhookurl = os.getenv("WEBHOOK_URL", "")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # required to see member roles

bot = ezcord.Bot(
    language="en", error_webhook_url=webhookurl, intents=intents
)

@bot.event
async def on_message(message: discord.Message):
    # Ignore DMs and bots
    if message.author is None:
        return
    if message.author.bot:
        return
    if message.guild is None:
        return

    channel_id = message.channel.id

    if channel_id not in BAN_CHANNEL_IDS:
        return


    member: discord.Member = message.author
    for role in getattr(member, "roles", []):
        if role.id in IGNORE_ROLE_IDS:
            return


    await message.guild.ban(message.author, delete_message_seconds=604800, reason=BAN_REASON)





if __name__ == '__main__':
    bot.run(token)
    
