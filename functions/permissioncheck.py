from typing import Any
from discord.utils import get


def rolecheck(ctx: Any) -> bool:
    role = get(ctx.message.guild.roles, id=992610328766586930)
    if role in ctx.author.roles:
        return True
    else:
        return False