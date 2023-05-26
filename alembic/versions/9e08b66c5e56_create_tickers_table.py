"""create tickers table

Revision ID: 9e08b66c5e56
Revises: 2d22b1c355e8
Create Date: 2023-05-26 18:39:11.751882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e08b66c5e56'
down_revision = '2d22b1c355e8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "tickers",
        sa.Column('name', sa.String, primary_key=True)
    )


def downgrade() -> None:
    pass
