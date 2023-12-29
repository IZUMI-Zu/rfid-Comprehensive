import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.anyio
async def test_inventory_creation(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbsession: AsyncSession,
) -> None:
    """Tests inventory instance creation."""
    # url = fastapi_app.url_path_for("create_inventory_model")
    # test_name = uuid.uuid4().hex
    # response = await client.put(
    #     url,
    #     json={
    #         "name": test_name,
    #     },
    # )
    # assert response.status_code == status.HTTP_200_OK
    # dao = InventoryDAO(dbsession)
    # instances = await dao.filter(name=test_name)
    # assert instances[0].name == test_name


@pytest.mark.anyio
async def test_inventory_getting(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbsession: AsyncSession,
) -> None:
    """Tests inventory instance retrieval."""
    # dao = InventoryDAO(dbsession)
    # test_name = uuid.uuid4().hex
    # await dao.create_inventory(name=test_name)
    # url = fastapi_app.url_path_for("get_inventory_models")
    # response = await client.get(url)
    # inventories = response.json()

    # assert response.status_code == status.HTTP_200_OK
    # assert len(inventories) == 1
    # assert inventories[0]["name"] == test_name
