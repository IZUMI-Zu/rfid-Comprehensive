from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Boolean, DateTime, String

from checkin.db.base import Base

MAX_CHARFIELD_LENGTH = 50
MAX_ITEM_NAME_LENGTH = 100


class InventoryModel(Base):
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

    __tablename__ = "inventory_model"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    item_name: Mapped[str] = mapped_column(String(length=MAX_ITEM_NAME_LENGTH))
    item_number: Mapped[str] = mapped_column(String(length=MAX_CHARFIELD_LENGTH))
    card_number: Mapped[str] = mapped_column(String(length=MAX_CHARFIELD_LENGTH))
    warehouse_number: Mapped[str] = mapped_column(String(length=MAX_CHARFIELD_LENGTH))
    shelf_number: Mapped[str] = mapped_column(String(length=MAX_CHARFIELD_LENGTH))
    storage_time: Mapped[datetime] = mapped_column(DateTime)
    is_in_stock: Mapped[bool] = mapped_column(Boolean)
