import os

from checkin.settings import settings


async def create_database() -> None:
    """Create a database."""
    if not settings.db_file.parent.exists():
        os.makedirs(settings.db_file.parent)
    if not settings.db_file.exists():
        with open(settings.db_file, "w") as file:
            file.write("")


async def drop_database() -> None:
    """Drop current database."""
    if settings.db_file.exists():
        os.remove(settings.db_file)
