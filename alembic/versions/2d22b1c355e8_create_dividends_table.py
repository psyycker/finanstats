"""create dividends table

Revision ID: 2d22b1c355e8
Revises:
Create Date: 2023-05-26 15:43:59.682051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d22b1c355e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "dividends",
        sa.Column('date', sa.Date, primary_key=True),
        sa.Column('amount', sa.Float),
        sa.Column('ticker', sa.String, primary_key=True)
    )


def downgrade() -> None:
    pass
