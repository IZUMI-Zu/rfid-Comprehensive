from typing import Awaitable, Callable

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.test import finalizer, initializer

from rfid_lab.db.config import MODELS_MODULES, TORTOISE_CONFIG
from rfid_lab.settings import settings


def register_startup_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application startup.

    This function uses fastAPI app to store data
    in the state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("startup")
    async def _startup() -> None:  # noqa: WPS430
        app.middleware_stack = None
        app.middleware_stack = app.build_middleware_stack()

        # Try init db
        try:
            initializer(
                MODELS_MODULES,
                db_url=str(settings.db_url),
                app_label="models",
            )
            await Tortoise.init(config=TORTOISE_CONFIG)
        except Exception as e:
            print(e)
        pass  # noqa: WPS420

    return _startup


def register_shutdown_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application's shutdown.

    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("shutdown")
    async def _shutdown() -> None:  # noqa: WPS430
        # Try close db
        try:
            await Tortoise.close_connections()
            finalizer()
        except Exception as e:
            print(e)
        pass  # noqa: WPS420

    return _shutdown
