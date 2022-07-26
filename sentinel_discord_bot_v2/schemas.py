import datetime

from pydantic import BaseModel, Field
from enum import Enum


class GuildConfigPreset(Enum):
    DEFAULT = "default"
    CUSTOM = "custom"


class GuildConfigData(BaseModel):
    use_config: bool


class GuildConfigPermissions(BaseModel):
    read: int
    edit: int


class GuildConfig(BaseModel):
    permissions: GuildConfigPermissions
    data: GuildConfigData
    preset: GuildConfigPreset


class GuildConfigDB(BaseModel):
    id: int
    json_: GuildConfig = Field(alias="json")
    created_at: datetime.date


class Guild(BaseModel):
    discord_id: str
    name: str
    icon: str
    owner_discord_id: str
