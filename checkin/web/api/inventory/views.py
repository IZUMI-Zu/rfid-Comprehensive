from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from checkin.db.dao.inventory_dao import InventoryDAO
from checkin.db.models.inventory_model import InventoryModel
from checkin.web.api.inventory.schema import InventoryModelDTO, InventoryModelInputDTO

router = APIRouter()


@router.get("/", response_model=List[InventoryModelDTO])
async def get_inventory_models(
    limit: int = 10,
    offset: int = 0,
    inventory_dao: InventoryDAO = Depends(),
) -> List[InventoryModel]:
    """
    Retrieve all inventory objects from the database.

    :param limit: limit of inventory objects, defaults to 10.
    :param offset: offset of inventory objects, defaults to 0.
    :param inventory_dao: DAO for inventory models.
    :return: list of inventory objects from database.
    """
    return await inventory_dao.get_all_inventories(limit=limit, offset=offset)


@router.put("/")
async def create_inventory_model(
    new_inventory_object: InventoryModelInputDTO,
    inventory_dao: InventoryDAO = Depends(),
) -> None:
    """
    Creates inventory model in the database.

    :param new_inventory_object: new inventory model item.
    :param inventory_dao: DAO for inventory models.
    """
    await inventory_dao.create_inventory(
        item_number=new_inventory_object.item_number,
        card_number=new_inventory_object.card_number,
        item_name=new_inventory_object.item_name,
        warehouse_number=new_inventory_object.warehouse_number,
        shelf_number=new_inventory_object.shelf_number,
        storage_time=new_inventory_object.storage_time,
        is_in_stock=new_inventory_object.is_in_stock,
    )
