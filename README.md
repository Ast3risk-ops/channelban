# ChannelBan

This bot watches a channel and bans users if they post in it (with configurable role exclusions).

This bot requires the **Server Members** and **Message Content** intents configured in the [dev portal](https://discord.com/developers/applications).

In guilds it requires the `bot` scope, `Guild Install`, and the following permissions: **View Channels**, **Read Message History**, **Moderate Members**, and **Ban Members**.

Sample invite link: 

```
https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=1099511694340&integration_type=0&scope=bot
```

To run:

```
cd channelbans/
cp .env.example .env
```

edit `.env` with all the values specified in the comments.

`pipenv` is recommended.

```
pipenv install
pipenv run bot
```
