# -*- coding: utf-8 -*-
import discord
import os
import requests
from time import sleep
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL', '')
BAN_REASON = os.getenv('BAN_REASON', 'Posted in the ban channel >:)')


def parse_id_set(env_value):
    if not env_value:
        return set()
    parts = [p.strip() for p in env_value.split(',') if p.strip()]
    ids = set()
    for p in parts:
        ids.add(long(p))  # Python 2 uses long for big integers
    return ids


BAN_CHANNEL_IDS = parse_id_set(os.getenv("CHANNELS", ""))
IGNORE_ROLE_IDS = parse_id_set(os.getenv("IGNORE_ROLES", ""))

client = discord.Client()


def send_webhook(msg):
    if not WEBHOOK_URL:
        return
    try:
        requests.post(WEBHOOK_URL, data={'content': msg})
    except Exception as e:
        print("Webhook failed:", e)


@client.event
def on_ready():
    print("Logged in as {}!".format(client.user.name))


@client.event
def on_message(message):
    try:
        # Ignore DMs
        if not message.server:
            return
        # Ignore bots
        if message.author.bot:
            return

        if long(message.channel.id) not in BAN_CHANNEL_IDS:
            return

        member = message.author
        # Skip if member has ignored role
        member_roles = getattr(member, 'roles', [])
        for role in member_roles:
            if long(role.id) in IGNORE_ROLE_IDS:
                return

        # Ban the user and delete messages from last 7 days
        # Old discord.py API: delete_message_days max 7
        client.http.ban(member.id, message.server.id, 7, BAN_REASON)
        print("🔨 Banned {}".format(member.name))

    except Exception as e:
        print("Error:", e)
        send_webhook(str(e))


# Run the bot
client.run(TOKEN, bot=True)
