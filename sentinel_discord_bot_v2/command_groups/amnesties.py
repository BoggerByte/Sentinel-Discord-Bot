__all__ = [
    "group"
]

import discord

group = discord.SlashCommandGroup("amnesties", "Tools to mercy people")


@group.command(name="mercy", description="Remove from user certain amount of warnings")
async def mercy(
        ctx: discord.ApplicationContext,
        user: discord.Option(discord.User, description="User | id"),
        level: discord.Option(int, description="Amount of removable warnings"),
) -> None:
    await ctx.respond(ctx.command)


@group.command(name="permit", description="Give access for person to some channel or group of them")
async def permit(
        ctx: discord.ApplicationContext,
        user: discord.Option(discord.User, description="User | id"),
        channels: discord.Option(discord.CategoryChannel, description="Select a channel"),
        time: discord.Option(str, description="Restriction time")
) -> None:
    await ctx.respond(ctx.command)
