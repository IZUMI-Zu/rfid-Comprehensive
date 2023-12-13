from datetime import datetime
from typing import List, Optional

from rfid_lab.db.models.inventory_model import InventoryModel


class InventoryDAO:
    """Class for accessing Inventory table."""

    async def create_inventory(  # noqa: WPS211
        self,
        item_number: str,
        card_number: str,
        item_name: str,
        warehouse_number: str,
        shelf_number: str,
        storage_time: datetime,
        item_status: bool,
    ) -> None:
        """
        Add single inventory item to session.

        :param item_number: Item number of the inventory item.
        :param card_number: Card number of the inventory item.
        :param item_name: Name of the inventory item.
        :param warehouse_number: Warehouse number where the inventory item is stored.
        :param shelf_number: Shelf number where the inventory item is stored.
        :param storage_time: The time when the inventory item was stored.
        :param item_status: The status of the inventory item.
        """
        await InventoryModel.create(
            item_number=item_number,
            card_number=card_number,
            item_name=item_name,
            warehouse_number=warehouse_number,
            shelf_number=shelf_number,
            storage_time=storage_time,
            item_status=item_status,
        )

    async def get_all_inventories(
        self,
        limit: int,
        offset: int,
    ) -> List[InventoryModel]:
        """
        Get all inventory items with limit/offset pagination.

        :param limit: Limit of inventory items.
        :param offset: Offset of inventory items.
        :return: Stream of inventory items.
        """
        return await InventoryModel.all().offset(offset).limit(limit)

    async def filter(
        self,
        item_number: Optional[str] = None,
        storage_time: Optional[datetime] = None,
    ) -> List[InventoryModel]:
        """
        Get specific inventory item.

        :param item_number: Item number of inventory instance.
        :param storage_time: The time when the inventory item was stored.
        :return: Inventory items.
        """
        query = InventoryModel.all()
        if item_number:
            query = query.filter(item_number=item_number)
        if storage_time:
            query = query.filter(storage_time=storage_time)
        return await query
