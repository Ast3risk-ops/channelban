import { Client, GatewayIntentBits, Partials } from 'discord.js';
import dotenv from 'dotenv';
import axios from 'axios';

dotenv.config();

const token = process.env.TOKEN;
const webhookUrl = process.env.WEBHOOK_URL || "";
const BAN_REASON = process.env.BAN_REASON || "Posted in the ban channel >:)";

// Helper: parse comma-separated IDs into a Set
function parseIdSet(value) {
  if (!value) return new Set();
  return new Set(
    value
      .split(',')
      .map(v => v.trim())
      .filter(v => v.length > 0)
      .map(v => BigInt(v))
  );
}

const BAN_CHANNEL_IDS = parseIdSet(process.env.CHANNELS);
const IGNORE_ROLE_IDS = parseIdSet(process.env.IGNORE_ROLES);

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.MessageContent
  ],
  partials: [Partials.Message, Partials.Channel, Partials.GuildMember]
});

// Optional webhook error reporter
async function reportError(error) {
  if (!webhookUrl) return;
  try {
    await axios.post(webhookUrl, {
      content: `⚠️ **Error:** ${error.stack || error}`
    });
  } catch (err) {
    console.error("Webhook error report failed:", err.message);
  }
}

client.on('ready', () => {
  console.log(`✅ Logged in as ${client.user.tag}`);
});

client.on('messageCreate', async message => {
  try {
    // Ignore DMs and bots
    if (!message.guild || message.author.bot) return;

    const channelId = BigInt(message.channel.id);
    if (!BAN_CHANNEL_IDS.has(channelId)) return;

    const member = message.member;
    if (!member) return;

    // Skip if the member has an ignored role
    if (member.roles.cache.some(role => IGNORE_ROLE_IDS.has(BigInt(role.id)))) {
      return;
    }

    // Ban user and delete last 7 days of messages (604800 seconds)
    await member.ban({ reason: BAN_REASON, deleteMessageSeconds: 604800 });
    console.log(`🔨 Banned ${member.user.tag} for posting in restricted channel`);
  } catch (error) {
    console.error("Error processing message:", error);
    await reportError(error);
  }
});

client.login(token);
