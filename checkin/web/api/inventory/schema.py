from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class InventoryModelDTO(BaseModel):
    """
    DTO for inventory models.

    It returned when accessing inventory models from the API.
    """

    id: int
    item_number: str
    card_number: str
    item_name: str
    warehouse_number: str
    shelf_number: str
    storage_time: datetime
    is_in_stock: bool
    model_config = ConfigDict(from_attributes=True)


class InventoryModelInputDTO(BaseModel):
    """DTO for creating new inventory model."""

    item_number: str = Field(..., description="The item number of the inventory")
    card_number: str = Field(..., description="The card number of the inventory")
    item_name: str = Field(..., description="The name of the inventory item")
    warehouse_number: str = Field(
        ...,
        description="The warehouse number where the item is stored",
    )
    shelf_number: str = Field(
        ...,
        description="The shelf number where the item is stored",
    )
    storage_time: datetime = Field(
        ...,
        description="The time when the inventory item was stored",
    )
    is_in_stock: bool = Field(..., description="The status of the inventory item")
