from typing import List, Optional

from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends

from checkin.db.dao.inventory_dao import InventoryDAO
from checkin.db.models.inventory_model import InventoryModel
from checkin.web.api.inventory.schema import InventoryModelDTO, InventoryModelInputDTO

router = APIRouter()


@router.get("/", response_model=List[InventoryModelDTO])
async def get_inventory_models(
    limit: Optional[int] = None,
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


@router.get("/{item_number}", response_model=InventoryModelDTO)
async def get_inventory_by_item_number(
    item_number: str,
    inventory_dao: InventoryDAO = Depends(),
) -> InventoryModel:
    """
    Get inventory model by item number.

    :param item_number: item number of inventory model to get.
    :param inventory_dao: DAO for inventory models.
    """

    inventory = await inventory_dao.get_inventory_by_item_number(
        item_number=item_number
    )
    if inventory is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return inventory


@router.put("/{item_number}")
async def update_inventory_model(
    inventory_object: InventoryModelInputDTO,
    inventory_dao: InventoryDAO = Depends(),
) -> None:
    """
    Updates inventory model in the database.

    :param inventory_model: new inventory model item.
    :param item_number: item number of inventory model to update.
    """
    await inventory_dao.update_inventory(
        item_number=inventory_object.item_number,
        card_number=inventory_object.card_number,
        item_name=inventory_object.item_name,
        warehouse_number=inventory_object.warehouse_number,
        shelf_number=inventory_object.shelf_number,
        storage_time=inventory_object.storage_time,
        is_in_stock=inventory_object.is_in_stock,
    )
