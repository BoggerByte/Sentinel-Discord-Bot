__all__ = ["DISCORD_TOKEN"]

import os

from dotenv import load_dotenv

load_dotenv("../.env", verbose=True)
load_dotenv("../app.env", verbose=True)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
