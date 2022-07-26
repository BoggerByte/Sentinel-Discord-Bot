import aiohttp

import schemas


class SentinelBackend:
    __discord_api = "/discord_bot_api/v1"

    def __init__(self, address: str, api_secret: str) -> None:
        self.__address = address
        self.__headers = {"Authorization": api_secret}

    async def get_guilds_configs(self) -> list[schemas.GuildConfig]:
        async with aiohttp.ClientSession(base_url=self.__address, headers=self.__headers) as client:
            response = await client.get(f"{self.__discord_api}/guilds/configs")
            json = await response.json()
            return [schemas.GuildConfig(**guild_config_db_json["json"]) for guild_config_db_json in json]

    async def get_guild_config(self, discord_id: str) -> schemas.GuildConfig:
        async with aiohttp.ClientSession(base_url=self.__address, headers=self.__headers) as client:
            response = await client.get(f"{self.__discord_api}/guilds/{discord_id}/config")
            json = await response.json()
            return schemas.GuildConfig(**json["json"])

    async def get_guild_config_preset(self, preset: schemas.GuildConfigPreset) -> schemas.GuildConfig:
        async with aiohttp.ClientSession(base_url=self.__address, headers=self.__headers) as client:
            response = await client.get(f"{self.__discord_api}/guilds/configs/presets/{preset.value}")
            json = await response.json()
            return schemas.GuildConfig(**json)

    async def create_or_update_guilds(self, guilds: list[schemas.Guild]) -> None:
        async with aiohttp.ClientSession(base_url=self.__address, headers=self.__headers) as client:
            json = {
                "guilds": [guild.json() for guild in guilds]
            }
            response = await client.post(f"{self.__discord_api}/guilds", json=json)
            print(await response.json())
            assert response.status == 200


if __name__ == "__main__":
    pass
