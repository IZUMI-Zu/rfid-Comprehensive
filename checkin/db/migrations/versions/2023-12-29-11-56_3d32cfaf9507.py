"""empty message

Revision ID: 3d32cfaf9507
Revises: 819cbf6e030b
Create Date: 2023-12-29 11:56:20.192781

"""
import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy import Boolean, DateTime, Integer, MetaData, String, column, table

# revision identifiers, used by Alembic.
revision = "3d32cfaf9507"
down_revision = "819cbf6e030b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    meta = MetaData()
    meta.reflect(bind=op.get_bind())
    if "inventory_model" not in meta.tables:
        op.create_table(
            "inventory_model",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("item_number", sa.String(50), nullable=False),
            sa.Column("card_number", sa.String(50), nullable=False),
            sa.Column("item_name", sa.String(100), nullable=False),
            sa.Column("warehouse_number", sa.String(50), nullable=False),
            sa.Column("shelf_number", sa.String(50), nullable=False),
            sa.Column("storage_time", sa.DateTime, default=datetime.datetime.utcnow),
            sa.Column("is_in_stock", sa.Boolean, default=True),
        )

    # Define the table structure
    inventory_model = table(
        "inventory_model",
        column("id", Integer),
        column("item_number", String),
        column("card_number", String),
        column("item_name", String),
        column("warehouse_number", String),
        column("shelf_number", String),
        column("storage_time", DateTime),
        column("is_in_stock", Boolean),
    )

    # insert data for testing
    op.bulk_insert(
        inventory_model,
        [
            {
                "id": 1,
                "item_number": "MNB34",
                "card_number": "0xCAFEBABE09876543",
                "item_name": "Pliers, adjustable",
                "warehouse_number": "WH-002",
                "shelf_number": "D3-5",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-11T08:56:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": True,
            },
            {
                "id": 2,
                "item_number": "HJK56",
                "card_number": "0x1357924680FEDCBA",
                "item_name": "Level, 24-inch",
                "warehouse_number": "WH-003",
                "shelf_number": "A1-3",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-10T17:20:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": False,
            },
            {
                "id": 3,
                "item_number": "UYT12",
                "card_number": "0x4568123498765432",
                "item_name": "Screwdriver set, 6-piece",
                "warehouse_number": "WH-001",
                "shelf_number": "C2-1",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-09T11:44:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": True,
            },
            {
                "id": 4,
                "item_number": "VBN78",
                "card_number": "0x0F1E2D3C4B5A6B78",
                "item_name": "Safety glasses",
                "warehouse_number": "WH-002",
                "shelf_number": "B4-2",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-08T06:08:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": True,
            },
            {
                "id": 5,
                "item_number": "QWE90",
                "card_number": "0xABCDEF1234567890",
                "item_name": "Hammer, 16 oz",
                "warehouse_number": "WH-004",
                "shelf_number": "A2-6",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-07T14:30:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": False,
            },
            {
                "id": 6,
                "item_number": "ASD67",
                "card_number": "0x1234567890ABCDEF",
                "item_name": "Tape measure, 25 ft",
                "warehouse_number": "WH-005",
                "shelf_number": "B1-4",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-06T09:15:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": True,
            },
            {
                "id": 7,
                "item_number": "ZXC34",
                "card_number": "0x9876543210FEDCBA",
                "item_name": "Drill bit set, 13-piece",
                "warehouse_number": "WH-006",
                "shelf_number": "C3-2",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-05T04:00:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": True,
            },
            {
                "id": 8,
                "item_number": "RTY56",
                "card_number": "0xFEDCBA0987654321",
                "item_name": "Work gloves, size L",
                "warehouse_number": "WH-007",
                "shelf_number": "D4-5",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-04T22:45:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": False,
            },
            {
                "id": 9,
                "item_number": "FGH23",
                "card_number": "0x234567890ABCDEFF",
                "item_name": "Circular saw, 7-1/4 in",
                "warehouse_number": "WH-008",
                "shelf_number": "E5-7",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-03T18:30:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": True,
            },
            {
                "id": 10,
                "item_number": "JKL45",
                "card_number": "0x567890ABCDEF1234",
                "item_name": "Cordless drill, 20V",
                "warehouse_number": "WH-009",
                "shelf_number": "F6-8",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-02T14:15:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": False,
            },
            {
                "id": 11,
                "item_number": "CVB67",
                "card_number": "0x890ABCDEF1234567",
                "item_name": "Reciprocating saw, corded",
                "warehouse_number": "WH-010",
                "shelf_number": "G7-9",
                "storage_time": datetime.datetime.strptime(
                    "2023-12-01T10:00:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": True,
            },
            {
                "id": 12,
                "item_number": "NMQ89",
                "card_number": "0xBCDEF1234567890A",
                "item_name": "Miter saw, 12 in",
                "warehouse_number": "WH-011",
                "shelf_number": "H8-10",
                "storage_time": datetime.datetime.strptime(
                    "2023-11-30T05:45:00",
                    "%Y-%m-%dT%H:%M:%S",
                ),
                "is_in_stock": True,
            },
        ],
    )


def downgrade() -> None:
    op.drop_table("inventory_model")
