from tortoise import fields
from tortoise.models import Model

MAX_CHARFIELD_LENGTH = 50
MAX_ITEM_NAME_LENGTH = 100


class InventoryModel(Model):
    """
    Represents an inventory item.

    Attributes:
        id (int): The unique identifier of the inventory item.
        item_number (str): The item number of the inventory item.
        card_number (str): The card number associated with the inventory item.
        item_name (str): The name of the inventory item.
        warehouse_number (str): The warehouse number where the item is stored.
        shelf_number (str): The shelf number where the item is stored.
        storage_time (datetime): The time when the item was stored in the inventory.
        is_in_stock (bool): Indicates whether the item is currently in stock or not.
            True means "入库" (in stock), False means "出库" (out of stock).
    """

    id = fields.IntField(pk=True)
    item_number = fields.CharField(max_length=MAX_CHARFIELD_LENGTH)
    card_number = fields.CharField(max_length=MAX_CHARFIELD_LENGTH)
    item_name = fields.CharField(max_length=MAX_ITEM_NAME_LENGTH)
    warehouse_number = fields.CharField(max_length=MAX_CHARFIELD_LENGTH)
    shelf_number = fields.CharField(max_length=MAX_CHARFIELD_LENGTH)
    storage_time = fields.DatetimeField(auto_now_add=True)
    is_in_stock = fields.BooleanField(default=True)

    def __str__(self) -> str:
        return self.item_number
