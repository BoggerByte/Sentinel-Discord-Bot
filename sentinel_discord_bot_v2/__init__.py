__version__ = "0.1.0"
__all__ = []

import discord
from loguru import logger

import config
from command_groups import punishments, amnesties
from sentinel_backend import SentinelBackend

bot = discord.Bot(debug_guilds=[827116545724383242])
bot.add_application_command(punishments.group)
bot.add_application_command(amnesties.group)


@bot.event
async def on_ready():
    logger.success("bot is ready")


@bot.event
async def on_connected():
    logger.success("connected to discord")


@bot.event
async def on_error(event: str):
    match event:
        case "on_connect":
            logger.error(f"{event}: Failed to connect to discord servers")
            await bot.close()
        case _:
            logger.error(f"{event}: Error occurred")


if __name__ == "__main__":
    bot.run(token=config.DISCORD_TOKEN)
