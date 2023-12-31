from datetime import datetime
from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from checkin.db.dependencies import get_db_session
from checkin.db.models.inventory_model import InventoryModel


class InventoryDAO:
    """Class for accessing inventory table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_inventory(
        self,
        item_name: str,
        item_number: str,
        card_number: str,
        warehouse_number: str,
        shelf_number: str,
        storage_time: datetime,
        is_in_stock: bool,
    ) -> None:
        """
        Add single Inventory to session.

        item_number (str): The item number of the inventory item.
        card_number (str): The card number associated with the inventory item.
        item_name (str): The name of the inventory item.
        warehouse_number (str): The warehouse number where the item is stored.
        shelf_number (str): The shelf number where the item is stored.
        storage_time (datetime): The time when the item was stored in the inventory.
        is_in_stock (bool): Indicates whether the item is currently in stock or not.
            True means "入库" (in stock), False means "出库" (out of stock).

        """
        self.session.add(
            InventoryModel(
                item_name=item_name,
                item_number=item_number,
                card_number=card_number,
                warehouse_number=warehouse_number,
                shelf_number=shelf_number,
                storage_time=storage_time,
                is_in_stock=is_in_stock,
            ),
        )

    async def get_all_inventories(
        self,
        limit: Optional[int] = None,
        offset: int = 0,
    ) -> List[InventoryModel]:
        """
        Get all inventory models with limit/offset pagination.

        :param limit: limit of inventory.
        :param offset: offset of inventory.
        :return: stream of inventory.
        """
        if limit is None:
            inventory_dummies = await self.session.execute(
                select(InventoryModel).offset(offset),
            )
        else:
            inventory_dummies = await self.session.execute(
                select(InventoryModel).limit(limit).offset(offset),
            )

        return list(inventory_dummies.scalars().fetchall())

    async def filter(
        self,
        name: Optional[str] = None,
        storage_time: Optional[datetime] = None,
    ) -> List[InventoryModel]:
        """
        Get specific inventory model.

        :param name: name of inventory instance.
        :param storage_time: storage time of inventory instance.
        :return: inventory models.
        """
        query = select(InventoryModel)
        if name:
            query = query.where(InventoryModel.item_name == name)
        if storage_time:
            query = query.where(InventoryModel.storage_time == storage_time)
        rows = await self.session.execute(query)
        return list(rows.scalars().fetchall())

    async def update_inventory(
        self,
        item_number: str,
        card_number: str,
        item_name: str,
        warehouse_number: str,
        shelf_number: str,
        storage_time: datetime,
        is_in_stock: bool,
    ) -> InventoryModel:
        """
        Update inventory model in the database.

        """
        query = select(InventoryModel)
        if item_number:
            query = query.where(InventoryModel.item_number == item_number)

        result = await self.session.execute(query)
        inventory = result.scalars().first()

        if inventory:
            # Update the existing inventory model
            inventory.card_number = card_number
            inventory.item_name = item_name
            inventory.warehouse_number = warehouse_number
            inventory.shelf_number = shelf_number
            inventory.storage_time = storage_time
            inventory.is_in_stock = is_in_stock
        else:
            # Create a new inventory model
            inventory = InventoryModel(
                item_number=item_number,
                card_number=card_number,
                item_name=item_name,
                warehouse_number=warehouse_number,
                shelf_number=shelf_number,
                storage_time=storage_time,
                is_in_stock=is_in_stock,
            )
            self.session.add(inventory)

        # Commit the changes
        await self.session.commit()

        # Refresh the instance to get the updated values
        await self.session.refresh(inventory)

        return inventory

    async def get_inventory_by_item_number(
        self,
        item_number: str,
    ) -> Optional[InventoryModel]:
        """Get inventory model by item number."""
        query = select(InventoryModel).where(InventoryModel.item_number == item_number)
        result = await self.session.execute(query)
        inventory = result.scalars().first()

        return inventory
