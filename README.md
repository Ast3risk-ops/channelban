# ChannelBan

This bot watches specific channels and **automatically bans any user who posts in them**, unless they have one of the ignored roles.  
All configuration is done through a simple `.env` file.

---

## ⚙️ Features
- Watches specific channels (configurable in `.env`)
- Bans users who post there
- Optionally ignores users with certain roles
- Sends error reports to a webhook (optional)
- Deletes the last 7 days of messages
- Written in **Python 2.7** using `discord.py 0.16.12`

---

## 🔑 Required Discord Intents
Make sure the bot has the following:
- **Server Members Intent**
- **Message Content Intent**

In the guild, it also needs:
- View Channels  
- Read Message History  
- Moderate Members  
- Ban Members  

---

## 🚀 Setup

```bash
cd channelbans/
cp .env.example .env
```

Edit `.env` and fill in the required values.

---

## 🧩 Environment Variables

| Variable | Description |
|-----------|-------------|
| `TOKEN` | Your bot token |
| `WEBHOOK_URL` | (Optional) Webhook URL for error reporting |
| `CHANNELS` | Comma-separated list of channel IDs to watch |
| `IGNORE_ROLES` | Comma-separated list of role IDs to ignore |
| `BAN_REASON` | (Optional) Custom ban reason |

---

## 🧰 Installation

You’ll need [Python 2.7](https://www.python.org/downloads/release/python-2718/) installed.

```bash
# Optional: create a virtual environment for Python 2
virtualenv -p python2 py2env
source py2env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the Bot

```bash
python main.py
```

---

## 🧾 Example `.env`

```ini
WEBHOOK_URL=https://discord.com/api/webhooks/...
TOKEN=your_bot_token_here
CHANNELS=123456789012345678,987654321098765432
IGNORE_ROLES=112233445566778899
BAN_REASON=Posted in the restricted channel
```

---

## 🧱 License
MIT License © 2025 Your Name
