__all__ = [
    "group"
]

import discord

group = discord.SlashCommandGroup("punishments", "Tools to punish people")


@group.command(name="ban", description="Advanced ban")
async def ban(
        ctx: discord.ApplicationContext,
        user: discord.Option(discord.User, description="User | id"),
        time: discord.Option(str, description="Ban time"),
        reason: discord.Option(str, description="Reason of ban", default="Reason not given")
) -> None:
    await ctx.respond(ctx.command)


@group.command(name="mute", description="Mute person in voice or in regular chat or both")
async def mute(
        ctx: discord.ApplicationContext,
        user: discord.Option(discord.User, description="User | id"),
        time: discord.Option(str, description="Mute time"),
        channel_type: discord.Option(str, choices=[
            discord.OptionChoice("Voice", "v"),
            discord.OptionChoice("Text", "t"),
            discord.OptionChoice("Both", "vt")
        ]),
        reason: discord.Option(str, description="Reason of mute", default="Reason not given")
) -> None:
    await ctx.respond(ctx.command)


@group.command(name="restrict", description="Restrict access for person to some channel or group of them")
async def restrict(
        ctx: discord.ApplicationContext,
        user: discord.Option(discord.User, description="User | id"),
        channels: discord.Option(discord.CategoryChannel, description="Select a channel"),
        time: discord.Option(str, description="Restriction time"),
        reason: discord.Option(str, description="Reason of restriction", default="Reason not given")
) -> None:
    await ctx.respond(ctx.command)


@group.command(name="warn", description="Give user certain amount of warnings")
async def warn(
        ctx: discord.ApplicationContext,
        user: discord.Option(discord.User, description="User | id"),
        level: discord.Option(int, description="Amount of warnings"),
        reason: discord.Option(str, description="Reason of warning", default="Reason not given")
) -> None:
    await ctx.respond(ctx.command)


@group.command(name="judge", description="Start a court for user")
async def judge(
        ctx: discord.ApplicationContext,
        user: discord.Option(discord.User, description="User | id"),
        channel: discord.Option(discord.TextChannel, description="Channel where message will be posted"),
        expiration: discord.Option(str, description="Vote expiration time"),
        options: discord.Option(str, description="Write options separated by ; sign"),
        description: discord.Option(str, description="Court description"),
        anonymous: discord.Option(bool, default=True, description="Can user view vote owners?"),
        retrieve: discord.Option(bool, default=False, description="Can user retrieve a vote?")
) -> None:
    await ctx.respond(ctx.command)
